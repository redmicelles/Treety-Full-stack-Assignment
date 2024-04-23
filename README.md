Problem:
Given an array of string. Where each string is an interdependent algebraic formula built using space
separated operands and operators. Each formula has a left hand side (LHS) and a right hand side (RHS)
separated by an equal-to sign. The LHS is a single operand and the RHS is an algebraic formula built using
operator and operand always separated by a single space.
formulae
Sort the array of formulae in an order in which they can be solved. Which can also mean the the formula
which has the least dependency will be solved first.
Example
1. x = ( a + b ) - ( c * d )
2. y = x / k
3. z1 = y / 100
4. a = 100 + ( 5 * 20000 )
Note that operands with the same name have the same reference, meaning if you have to calculate the value
of y in the 2nd formula you will need the value of x. So you can never solve the 2nd formula without solving
the 1st one.
Every expression is built with the following
1. Brackets - which can be ( or )
2. Variables - which can be x, y, z1, xyz, etc
3. Constants - which are numbers like 5, 100, 40244, etc
4. Operators - which can either +, -, * and /
======================================================================
Now, based on the type of input you can have possibly 2 types of outputs.
1. When the input has a dependency cycle, in the example below we cannot calculate x without calculating y
and cannot calculate y without calculating x which creates a dependency cycle.
Example input:
["x = a * y", "y = x * 5"]
output:
["cyclic_dependency"]
2. When the input has no error, return the same list of expressions sorted in the order in which they can be
solved considering the dependency.
Example input:
["x = y + 6", "y = 7 * 4", "z = ( x * y )"]
output:
["y = 7 * 4", "x = y + 6", "z = ( x * y )”]
Treety Full stack Assignment - Sort Expression 4/16/2024
1/2
Your submission must be of the following method signature,
JAVA:
public Array<String> sortExpressions(Array<String> expressions){
return expressions
}
Python:
def sortExpressions(expressions: list):
return expressions
