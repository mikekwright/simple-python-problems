Problem 2 - Simple Calculator
=====================================

In this problem we are going to go a little farther into the python ecosystem and
make sure that we understand how to use `if/elif/else` statements as well as how
we can use the standard input/output functions in python (they are `input(..)` and
`print(...)`).

Problem
-----------------------------------

1. Create a function for reading a number from the user
  * This function should return a float
2. Create a function for reading the operation from the user
  * This function should return a string
  * Possible options: +, -, *, /
    * `+` add the two numbers together
    * `-` subtract the second number from the first number
    * `*` multiply the two numbers together
    * `/` divide the first number by the second number
3. Create a function for asking user if they want to continue
  * This function should return a bool
  * yes should return True, anything else returns False
4. Create a function that shows the output of the operation
  * This function should have 4 arguments
    * first number
    * operation
    * second number
    * total
  * This should just print the output to screen
  * The output should be: Answer <first number> <operation> <second number> = <total>

* Create the main function
* Ask the user the first number using the function you created in step 1
* Ask the user the operation to run using the function you created in step 2
* Ask the user for another number using the function you created in step 1
* Calculate the result
* Print the result
* Ask the user if they want to do it again

Example:
--------------------------------------

```
What is your first number: 5
What operation: -
What is your second number: 3
Answer: 5 - 3 = 2
Would you like to try again: yes
What is your first number: 3
What operation: *
What is your second number: 3
Answer: 3 * 3 = 9
Would you like to try again: no
```

