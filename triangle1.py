from this import d

print("Welcome to Bunmi's Triangle Calculator!")
running = True
while running:

    print("Perimeter = A")
    print("Area = B")
    print("Both = C")
    user_input = input("Select A,B or C: ")

    class Triangle:
        def __init__(self, a,b,c,) :
            self.a = a
            self.b = b
            self.c = c
        



        def perimeter(self):
            perimeter = self.a + self.b + self.c
            return perimeter
            
        def area(self, height):
        
            self.height = height
            area = 0.5 * self.c * self.height
            return area


    side1 = int(input("First Side = "))
    side2 = int(input("Second Side = "))
    base = int(input("Base = "))
    height = int(input("Height = "))

    triangle_sides = Triangle (side1, side2, base) 

    if user_input == "A":
        per = triangle_sides.perimeter()
        print("The perimeter of the triangle is ", per)

    if user_input == "B":
        area = triangle_sides.area(height)
        print("The area of the triangle is ", area)

    if user_input == "C":
        per = triangle_sides.perimeter()
        area = triangle_sides.area(height)
        print("The perimeter of the triangle is ", per)
        print("The area of the triangle is ", area)

    option = input("Do you want to use this service again: ")
    if option == "Yes":
        pass
    elif option == "YES":
        pass
    elif option == "No":
        running = False
    elif option == "NO":
        running = False 
    else:
        running = False
print("Thank you.")            