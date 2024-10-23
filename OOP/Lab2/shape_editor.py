from abc import ABC  # Імпортуємо базовий клас для абстрактних класів з модуля abc
from editor import Editor  # Імпортуємо клас Editor, від якого будемо успадковувати

class ShapeEditor(Editor, ABC):
    def __init__(self):
        super().__init__()  # Викликає конструктор батьківського класу Editor

    def on_mouse_down(self, event):
        pass  # Метод для обробки події натискання миші

    def on_mouse_up(self, event):
        pass  # Метод для обробки події відпускання миші

    def on_mouse_move(self, event):
        pass  # Метод для обробки події переміщення миші

    def on_paint(self, canvas):
        pass  # Метод для малювання на полотні

    def on_init_menu_popup(self, canvas):
        pass  # Метод для ініціалізації контекстного меню

    def clear_canvas(self):
        pass  # Метод для очищення полотна
