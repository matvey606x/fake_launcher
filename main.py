from termcolor import colored
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
import requests
from packaging import version
import webbrowser

# Конфигурация GitHub
REPO_OWNER = "matvey606x"
REPO_NAME = "fake_launcher"
GITHUB_TOKEN = "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"  # Замените на реальный токен
CURRENT_VERSION = "1.1"

def check_for_updates():
    try:
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        latest_release = response.json()
        latest_version = latest_release["tag_name"].lstrip('v')
        
        if version.parse(latest_version) > version.parse(CURRENT_VERSION):
            print(colored(f"🔔 Доступно обновление: {latest_version}", "green"))
            print(colored(f"Описание: {latest_release.get('body', 'Нет описания')}", "yellow"))
            return latest_release["html_url"]
        else:
            print(colored("✅ У вас актуальная версия лаунчера!", "blue"))
            return None
            
    except requests.exceptions.RequestException as e:
        print(colored(f"❌ Ошибка при проверке обновлений: {e}", "red"))
        return None

print(colored("Добро пожаловать в Grand Theft Auto VI Launcher", "blue", attrs=["bold"]))
print(colored("Введите play чтобы начать играть. help для просмотра комманд", attrs=["bold"]))

while True:
    a = str(input("> ")).strip().lower()
    
    if a == "play":
        os.system("sound.mp3")
        time.sleep(2)
        
        
        root = tk.Tk()
        root.attributes('-fullscreen', True)  
        image = Image.open("image.jpg")  
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.pack(expand=True, fill="both")
        root.mainloop()
        
    elif a == "help":
        print(colored("Доступные команды:", "yellow"))
        print("version - Отобразить версию лаунчера")
        print("play - Играть")
        print("update - Проверить обновления")
        print("exit - Выйти из лаунчера")
        
    elif a == "version":
        print(colored(f"Текущая версия лаунчера: {CURRENT_VERSION}", "cyan"))
        
    elif a == "update":
        update_url = check_for_updates()
        if update_url:
            choice = input(colored("Хотите открыть страницу загрузки? (y/n): ", "yellow")).lower()
            if choice == 'y':
                webbrowser.open(update_url)
        
    elif a == "exit":
        print(colored("До свидания!", "magenta"))
        break
        
    else:
        print(colored("Неизвестная команда. Введите 'help' для списка команд", "red"))