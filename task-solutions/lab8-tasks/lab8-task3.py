def are_sides_construct_triangle(side1,side2,side3):
    if side1 + side2 > side3 and side2 + side3 > 1 and side1 + side3 > side2:
        return True
    return False

def check_sides_of_right_triangle(side1,side2,side3):
    if are_sides_construct_triangle(side1,side2,side3):
        if side1 > side2 and side1 > side3:
            if side1 * side1 == side2 * side2 + side3 * side3:
                return True
            return False

        if side2 > side1 and side2 > side3:
            if side2 * side2 == side1 * side1 + side3 * side3:
                return True
            return False

        if side3 > side2 and side3 > side1:
            if side3 * side3 == side2 * side2 + side1 * side1:
                return True
            return False


first_edge = int(input("Enter an edge: "))
second_edge = int(input("Enter an edge: "))
third_edge = int(input("Enter an edge: "))

if check_sides_of_right_triangle(first_edge,second_edge,third_edge):
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")

