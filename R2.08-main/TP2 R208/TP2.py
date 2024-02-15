class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    def __str__(self):
        return f"Rectangle(width={self.__width},height={self.__height})"

    def set_width(self, width):
        self.__width = width
    def set_height(self, height):
        self.__height = height
    def get_area(self):
        print(self.__width * self.__height)
    def get_perimeter(self):
        print(2 * (self.__width + self.__height))
    def get_diagonal(self):
        print((self.__width ** 2 + self.__height ** 2) ** 0.5)
    def get_picture(self):
        if self.__height > 50 or self.__width > 50:
            print("Trop grand pour faire une image.")
        else:
            print(('* ' * self.__width + '\n') * self.__height, end='')
    def get_amount_inside(self, form_width, form_height):
        print((self.__width * self.__height) // (form_width * form_height))


