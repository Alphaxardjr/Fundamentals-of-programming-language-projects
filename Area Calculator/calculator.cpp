#include <iostream>
#include <cmath>

using namespace std;

void area_triangle() {
    int base, height;
    cout << "Enter the base of the triangle: ";
    cin >> base;
    cout << "Enter the height of the triangle: ";
    cin >> height;
    double area = 0.5 * base * height;
    cout << "The area of the triangle is: " << area << endl;
}

void area_circle() {
    double radius;
    cout << "Enter the radius: ";
    cin >> radius;
    double area = M_PI * radius * radius;
    cout << "The area of the circle is: " << area << endl;
}

void area_square() {
    double length;
    cout << "Enter the length of the square: ";
    cin >> length;
    double area = length * length;
    cout << "The area of the square is: " << area << endl;
}

void user_manual() {
    cout << "User Manual." << endl;
    cout << "Choose 1 to calculate the area of a Triangle" << endl;
    cout << "Choose 2 to calculate the area of a Square" << endl;
    cout << "Choose 3 to calculate the area of a Circle" << endl;
}

int main() {
    cout << "WELCOME TO G&A AREA CALCULATOR" << endl;

    char continue_choice = 'Y';
    while (tolower(continue_choice) == 'y') {
        user_manual();
        int choice;
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice) {
            case 1:
                area_triangle();
                break;
            case 2:
                area_square();
                break;
            case 3:
                area_circle();
                break;
            default:
                cout << "Invalid choice" << endl;
                break;
        }
        cout << "Do you want to continue? (Y/N): ";
        cin >> continue_choice;
    }

    return 0;
}
