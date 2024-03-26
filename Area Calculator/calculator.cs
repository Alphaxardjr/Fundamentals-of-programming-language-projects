using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("WELCOME TO G&A AREA CALCULATOR");

        char continue_choice = 'Y';
        while (Char.ToLower(continue_choice) == 'y')
        {
            UserManual();
            Console.Write("Enter your choice: ");
            int choice = Convert.ToInt32(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    AreaTriangle();
                    break;
                case 2:
                    AreaSquare();
                    break;
                case 3:
                    AreaCircle();
                    break;
                default:
                    Console.WriteLine("Invalid choice");
                    break;
            }

            Console.Write("Do you want to continue? (Y/N): ");
            continue_choice = Convert.ToChar(Console.ReadLine());
        }
    }

    static void AreaTriangle()
    {
        Console.Write("Enter the base of the triangle: ");
        int baseValue = Convert.ToInt32(Console.ReadLine());
        Console.Write("Enter the height of the triangle: ");
        int height = Convert.ToInt32(Console.ReadLine());
        double area = 0.5 * baseValue * height;
        Console.WriteLine("The area of the triangle is: " + area);
    }

    static void AreaCircle()
    {
        Console.Write("Enter the radius: ");
        double radius = Convert.ToDouble(Console.ReadLine());
        double area = Math.PI * radius * radius;
        Console.WriteLine("The area of the circle is: " + area);
    }

    static void AreaSquare()
    {
        Console.Write("Enter the length of the square: ");
        double length = Convert.ToDouble(Console.ReadLine());
        double area = length * length;
        Console.WriteLine("The area of the square is: " + area);
    }

    static void UserManual()
    {
        Console.WriteLine("User Manual.");
        Console.WriteLine("Choose 1 to calculate the area of a Triangle");
        Console.WriteLine("Choose 2 to calculate the area of a Square");
        Console.WriteLine("Choose 3 to calculate the area of a Circle");
    }
}
