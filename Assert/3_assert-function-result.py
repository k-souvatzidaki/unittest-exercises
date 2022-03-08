def area(width, height):
    return width * height

assert area(4,10) == 40
assert area(5,6) == 30

def area(width, height):
    """The function returns the area of the rectangle."""
    if not (isinstance(width, int) and isinstance(height, int)):
        raise TypeError('The width and height must be of type int.')
    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')
    return width * height
 
assert area('5', '4') == 20 # TypeError
assert area(-4,5) == 20 # ValueError