import math
def area_triangle():
    base=int(input("Enter the base of the triangle: "))
    height=int(input("Enter the height of the triangle: "))
    area=0.5*base*height
    print('The are of the triangle is: ',area)
    
def area_circle():
    radius=float(input("Enter the radius: "))
    area=math.pi*radius*radius
    print("The area of the cirle is: ", area)

def area_square():
    length=float(input("Enter the length of the square: "))
    area=length*length
    print('The area of squire is: ',area)
    
def user_manual():
    print('User Manual.')
    print("""
    Choose 1 to calculate the area of a Triangle
    Choose 2 to calculate the area of a Square
    Choose 3 to calculate the area of a Circle
    """)
    
print("WELCOME TO G&A AREA CALCULATOR")


continue_choice="Y"
while continue_choice.lower()=='y':
   user_manual()
   choice=int(input("Enter your choice: "))
   if choice==1:
        area_triangle()
   elif choice==2:
        area_square()
   elif choice==3:
        area_square()
   else:
        print("Invalid choice")
   continue_choice=input("Do you want to continue? (Y/N)")
   
   
    
        
