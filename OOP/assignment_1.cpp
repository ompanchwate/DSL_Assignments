/*      Assignment no. 1
Implement a class Complex which represents the Complex Number data type. Implement the
following
1. Constructor (including a default constructor which creates the complex number 0+0i).
2. Overload operator+ to add two complex numbers.
3. Overload operator* to multiply two complex numbers.
4. Overload operators << and >> to print and read Complex Numbers.
*/
#include <iostream>
using namespace std;

class Complex
{
    public:
        int real,img;
};

int main() {
    Complex a, b, c ;
    cout << "Enter a and b where a + ib is the first complex number.";
    cout << "\na = ";
    cin >> a.real;
    cout << "b = ";
    cin >> a.img;
    cout << "Enter c and d where c + id is the second complex number.";
    cout << "\nc = ";
    cin >> b.real;
    cout << "d = ";
    cin >> b.img;

    c.real = a.real + b.real;
    c.img = a.img + b.img;

    cout << "Sum of two complex numbers = " << c.real << " + " << c.img << "i";
}