# CheckEmail

Write the function `valid_email(...)` to check if the input string is a valid email address or not.

An email is a string (a subset of ASCII characters) separated into two parts by @ symbol, a “user_info” and a
domain_info, that is personal_info@domain_info:
in case of correct email the function should be displayed the corresponding message – "Email is valid"
in case of incorrect email the function should be displayed the corresponding message – "Email is not valid"

Note: in the function you must use the "try except" construct.

Function example:

`valid_email("trafik@ukr.tel.com")`          #output:   "Email is valid"

`valid_email("trafik@ukr_tel.com")`        #output:   "Email is not valid"

`valid_email("tra@fik@ukr.com")`           #output:   "Email is not valid"

`valid_email("ownsite@our.c0m")`         #output:   "Email is not valid"

# DayOfWeek

Write the function day_of_week(day) whose input parameter is a number or string representation of number. The function
returns the corresponding day of the week if the input parameter is in the range of 1 to 7, namely

* in the case when the input parameter is 5 the function should be displayed the message – "Friday"

* in the case when the input parameter is not in the range of 1 to 7 the function should be displayed the message – "
  There is no such day of the week! Please try again."

* in the case of incorrect data the function should be displayed the message - "You did not enter a number! Please try
  again."

Note: in the function you must use the "try except" construct.

Function example:

`day_of_week(2)`                     # output:   "Tuesday"

`day_of_week(11)`                     # output:  "There is no such day of the week! Please try again."

`day_of_week("Monday")`       # output:   "You did not enter a number! Please try again."

# EvenOddNumber

Write the function `check_odd_even(number)` whose input parameter is an integer number. The function checks whether the
set number is even or odd:

* in the case of an even number the function should be displayed the corresponding message - "Entered number is even";

* in the case of an odd number the function should be displayed the corresponding message -  "Entered number is odd";

* in the case of incorrect data the function should be displayed the message - "You entered not a number."

* Note: in the function you must use the "try except" construct.

Function example:

`check_odd_even (24)`     #output:    "Entered number is even"

`check_odd_even (19)`     #output:     "Entered number is odd"

# DivideNumber

Write the function `divide(numerator, denominator)` the two input parameters of which are numbers. The function returns
the result of dividing two numbers.

* in case of correct data the function should be displayed the corresponding message – "Result is numerator /
  denominator"

* in the case of division by zero the function should be displayed the corresponding message – "Oops, numerator /
  denominator, division by zero is error!!!"

* in the case of incorrect data the function should be displayed the message – "Value Error! You did not enter a
  number!"

Note: in the function you must use the "try except" construct.

Function example:

divide(8, 16)        #output:   "Result is 0.5"

divide (5, 0)        #output:   "Oops, 5 / 0 denominator, division by zero is error!!!"

divide_number("25", 5)    #output:   "Value Error! You did not enter a number!"

divide_number("abc", 9)  #output:    "Value Error! You did not enter a number!"

# NumberOfGroup

Write the function `check_number_group(number)` whose input parameter is a number. The function checks whether the set
number is more than number 10:

* in case the number is more than 10 the function should be displayed the corresponding message - "Number of your group
  input parameter of function is valid";
* in case the number is less than or equal to 10 the function should be raised the exception of your own class
  ToSmallNumberGroupError and displayed the corresponding message - "We obtain error: Number of your group can't be less
  than 10";
* in the case of incorrect data the function should be displayed the message - "You entered incorrect data. Please try
  again."

Function example:

`check_number_group(4)`       #output:    "We obtain error: Number of your group can't be less than 10 "

`check_number_group(59)`    #output:     "Number of your group 59 is valid"

`check_number_group("25")`                #output:    "Number of your group 25 is valid"

`check_number_group("abc")`              #output:     "You entered incorrect data. Please try again."

# PositiveNumber

Write the function `check_positive(number)` whose input parameter is a number. The function checks whether the set
number is positive or negative:

* in the case of a positive number the function should be displayed the corresponding message - " You input positive
  number: input parameter of function";
* in the case of a negative parameter the function should be raised the exception of your own class MyError and
  displayed the corresponding message - "You input negative number: input parameter of function. Try again.";
* in the case of incorrect data the function should be displayed the message - "Error type: ValueError!"

Function example:

`check_positive(24) `     #output:    "You input positive number: 24"

`check_positive(-19) `    #output:     "You input negative number: -19. Try again."

`check_positive("38") `   #output:    "You input positive number: 38"

`check_positive("abc")`  #output:     "Error type: ValueError!"

# Equation

Write the function `solve_quadric_equation(a, b, c)` the three input parameters of which are numbers. The function
should return
the solution of quadratic equation ax2+bx+c=0, where coefficients a, b, c are input parameters of the function
solve_quadric_equation:

* in case of correct data the function should displayed the corresponding message – "The solution are x1=… and x2=…"

* in the case of division by zero the function should displayed the corresponding message – "Zero Division Error"

* in the case of incorrect data the function should displayed the message – "Could not convert string to float"

Note: in the function you must use the "try except" construct.

Function example:

`solve_quadric_equation(1, 5, 6)   `         #output:   " The solution are x1=(-2-0j) and x2=(-3+0j)"

`solve_quadric_equation(0, 8, 1) `           #output:   "Zero Division Error"

`solve_quadric_equation(1,”abc”, 5)`       #output:   "Could not convert string to float"