import tkinter as tk  # Імпорт бібліотеки tkinter для створення GUI

from shape_objects_editor import ShapeObjectsEditor  # Імпорт класу ShapeObjectsEditor, який буде нашим додатком

if __name__ == "__main__":
    root = tk.Tk()  # Створення головного вікна tkinter
    app = ShapeObjectsEditor(root)  # Ініціалізація додатку з головним вікном як параметр
    root.mainloop()  # Запуск головного циклу програми для відображення GUI
