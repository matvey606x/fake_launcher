from termcolor import colored
import tkinter as tk
from PIL import Image, ImageTk
import os
import time

def show_image():
    """Функция для отображения изображения на весь экран"""
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    try:
        image = Image.open("image.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.image = photo  # Сохраняем ссылку на изображение
        label.pack(expand=True, fill="both")
        root.mainloop()
    except Exception as e:
        print(colored(f"Ошибка при загрузке изображения: {e}", "red"))
        root.destroy()

def print_help():
    """Функция для вывода списка команд"""
    print(colored("Доступные команды:", "yellow"))
    print("version - Отобразить версию лаунчера")
    print("play - Играть")
    print("exit - Выйти из лаунчера")
    print("help - Показать это сообщение")

def main():
    print(colored("Добро пожаловать в Grand Theft Auto VI Launcher", "blue", attrs=["bold"]))
    print(colored("Введите команду (help для списка команд):", attrs=["bold"]))
    
    while True:
        try:
            command = input().strip().lower()
            
            if command == "play":
                try:
                    os.system("sound.mp3")
                    time.sleep(2)
                    os.system("VulkanAPI.bat")
                    show_image()
                except Exception as e:
                    print(colored(f"Ошибка при запуске игры: {e}", "red"))
            
            elif command == "help":
                print_help()
            
            elif command == "version":
                print(colored("Версия лаунчера: 1.0", "green"))
            
            elif command == "exit":
                print(colored("Выход из лаунчера...", "magenta"))
                break
                
            else:
                print(colored("Неизвестная команда. Введите help для списка команд.", "red"))
                
        except KeyboardInterrupt:
            print(colored("\nВыход из лаунчера...", "magenta"))
            break
        except Exception as e:
            print(colored(f"Произошла ошибка: {e}", "red"))

if __name__ == "__main__":
    main()