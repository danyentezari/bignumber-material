#### Topics
1. Pointers & Variables
2. Lists

<br/><br/>
#### Glossary

| Term               | Definition
|------------------- | ---------------------------------------------
| Pointer            | Address of some data in memory (or register)
| Variable           | Data that refers to other data in memory
| Reference          | The data of a variable
| Dereference        | The data of a pointer 


<br/><br/>
#### 1. Pointers & Variables

This section will give you an example for you to understand the terms better.

This is variable
```
int price = 100;
```

This is reference
```
cout << price; // gives you data 100
```

This is address of reference (i.e, pointer)
```
cout << &price // gives you address 0x**************
```

This is dereference
```
cout << *(&price) // gives you data 100 (again)
```

<br/><br/>
**1.1 Example in C++**
```
#include <iostream>

using namespace std;

int main()
{
    int price = 100;                    // set variable to data
    int *price_ptr = &price;            // set variable to address (pointer variable)
    
    *price_ptr = 200;                   // change the data at the address
    cout << price; cout << "\n";        // print the value of price
    cout << price_ptr; cout << "\n";    // print the value of price_ptr
    cout << &price;                     // print the address of price

    return 0;
}
```