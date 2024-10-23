from shape import Shape  # Імпортуємо базовий клас Shape, від якого будемо успадковувати

class PointShape(Shape):
    def draw(self, canvas):
        # Малює точку як маленький овал на полотні
        canvas.create_oval(self.start_x - 2, self.start_y - 2, self.start_x + 2, self.start_y + 2, fill="black")

    def __str__(self):
        # Повертає строкове представлення об'єкта для зручного відображення
        return f"PointShape at ({self.start_x}, {self.start_y})"
