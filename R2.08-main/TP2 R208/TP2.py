class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle(width={self.width},height={self.height})"

    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
       return 2 * (self.width + self.height)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            print("Trop grand pour faire une image.")
        else:
            return ('* ' * self.width + '\n') * self.height
    def get_amount_inside(self, form):
        return (self.width * self.height) // (form.width * form.height)

class Carree(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, self.side, self.side)

    def __str__(self):
        return f"Carree(side={self.side})"
    def set_side(self, newside):
        self.side = newside
        Rectangle.__init__(self, self.side, self.side)

