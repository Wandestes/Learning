from shape import Shape

class LineShape:
    def __init__(self):
        self.start_x = 0  # Початкова координата X лінії
        self.start_y = 0  # Початкова координата Y лінії
        self.end_x = 0    # Кінцева координата X лінії
        self.end_y = 0    # Кінцева координата Y лінії

    def draw(self, canvas, dash=None):
        if dash:
            # Малює лінію з пунктирною лінією, якщо dash заданий
            canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y, fill="black", dash=dash)
        else:
            # Малює лінію з суцільною лінією, якщо dash не заданий
            canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y, fill="black")
