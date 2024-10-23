from shape_editor import ShapeEditor
from point_shape import PointShape


class PointEditor(ShapeEditor):
    def __init__(self, canvas, shapes):
        super().__init__()
        self.shape = None  # Змінна для поточної фігури

        self.canvas = canvas  # Полотно для малювання
        self.shapes = shapes  # Список для зберігання фігур

    def on_mouse_down(self, event):
        # Створює новий об'єкт PointShape
        self.shape = PointShape()
        # Встановлює початкову координату X точки
        self.shape.start_x = event.x
        # Встановлює початкову координату Y точки
        self.shape.start_y = event.y
        # Малює точку на полотні, вказаному в event.widget
        self.shape.draw(event.widget)
        # Повертає створену фігуру для подальшого використання
        return self
    def on_mouse_up(self, event):
        if self.shape:
            # Додаємо точку до списку фігур
            self.shapes.append(self.shape)
            # Виводимо фігуру для перевірки
#            print(f"Added shape: {self.shape}")

            result_shape = self.shape
            self.shape = None

            return result_shape

    def on_mouse_move(self, event):
        pass

    def on_paint(self, canvas):
        pass
