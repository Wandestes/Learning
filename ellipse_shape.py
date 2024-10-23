from shape import Shape

class EllipseShape(Shape):
    def __init__(self):
        super().__init__()  # Викликає конструктор батьківського класу Shape
        self.center_y = None  # Ініціалізує змінну для збереження координати Y центру еліпса
        self.center_x = None  # Ініціалізує змінну для збереження координати X центру еліпса

    def draw(self, canvas, dash=None):
        # Обчислює радіуси еліпса по осям X і Y
        radius_x = abs(self.end_x - self.center_x)
        radius_y = abs(self.end_y - self.center_y)
        if dash:
            # Малює еліпс з пунктирною лінією, якщо dash заданий
            canvas.create_oval(
                self.center_x - radius_x,
                self.center_y - radius_y,
                self.center_x + radius_x,
                self.center_y + radius_y,
                outline="black",
                fill="orange",
                dash=dash
            )
        else:
            # Малює еліпс з суцільною лінією, якщо dash не заданий
            canvas.create_oval(
                self.center_x - radius_x,
                self.center_y - radius_y,
                self.center_x + radius_x,
                self.center_y + radius_y,
                outline="black",
                fill="orange"
            )

    def __str__(self):
        # Обчислює радіуси еліпса для представлення інформації
        radius_x = abs(self.end_x - self.center_x)
        radius_y = abs(self.end_y - self.center_y)
        # Повертає строкове представлення об'єкта для зручного відображення
        return f"EllipseShape (center=({self.center_x}, {self.center_y}), radius_x={radius_x}, radius_y={radius_y})"
