class RectShape:
    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0

    def draw(self, canvas, dash=None):
        # Обчислюємо координати кута охоплюючого прямокутника
        left = min(self.start_x, self.end_x)
        top = min(self.start_y, self.end_y)
        right = max(self.start_x, self.end_x)
        bottom = max(self.start_y, self.end_y)
        if dash:
            # Малює пунктирний прямокутник, якщо dash заданий
            canvas.create_rectangle(left, top, right, bottom, outline="black", fill="", dash=dash)
        else:
            # Малює суцільний прямокутник, якщо dash не заданий
            canvas.create_rectangle(left, top, right, bottom, outline="black", fill="")