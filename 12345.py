def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

# Example usage:
base = 10
height = 5
area = calculate_triangle_area(base, height)
print(f"The area of the triangle is {area}")