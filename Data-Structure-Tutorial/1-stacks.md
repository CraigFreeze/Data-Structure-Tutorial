# Stacks

Imagine you lost your keys, and you had to retrace your steps! All too often, we cannot even remember the very last things that we did. Rather than aimlessly wandering, it would nice to go back through our motions once distict piece at a time. 

Much like a stack of plates the data structure, "Stacks", helps us to not only organize items that we need to record or document, but it also helps us to reverse through the elements that we have added.

A stack in Python is a way that the programmer can leverage a (`list[]`).  In the example below, we will begin by adding items to our 'Stack' (List). This is accomplished by using the traditional `.append(value)` function. **Note, for a reason that you will soon see, it is signficiant that .append() adds the value to the END of the list**:

```python
my_stack = [] #Create List
my_stack.append(1) #Add the number 1 to List (Stack)
my_stack.append(2) #Add the number 2 to List (Stack)
my_stack.append(3) #Add the number 3 to List (Stack)
print(my_stack)

#Output: [1, 2, 3]
```

This code snippet will result in adding an item to the end of the list. Just like a stack of plates `.append()` adds the value (plate) to the top of the stack (or in our case, end of the list). You should be start to understand why the Data Structure in focus is referred to as a "Stack".

Much like a stack in the real world (stacks of books, plate, paper) the last item to go on the stack should be the first item to be removed from the stack (In the real world if you tried pulling from the middle the items higher in the stack would fall; in programming, it would disregard the whole reason of building a stack).

In Python, we use the `list.pop()` function to "Pop Off" (aka remove) the top item in the stack (last element in the list). **Note, not only does `pop()` remove the last item in the list, but it also returns its value! (It's kinda like you are holding the top plate in your hand)** See this being done:

```python
#Continuation of Code Snippet above
print(my_stack.pop()) #Removes and returns the number 3
print(my_stack.pop()) #Removes and returns the number 2
print(my_stack.pop()) #Removes and returns the number 1

#Output:
# 3
# 2
# 1
```


## LIFO - **L**ast **I**n, **F**irst **O**ut

Stacks should always follow the acronym, LIFO (Last in First Out). The last item that you added to the stack will be the first one to come off. One way to think about this is the UNDO function on computers (Keyboard: CONTROL Z). Whenever you do something on the computer, your action gets appended to a stack. And when you need to reverse your action, the *Last Action* becomes the *First Out*. In other words, the last thing to be added is the first thing to be removed.



## Syntax Review

|  Python Code   |      Description      |
| :-----: | :------------: |
|  my_stack = []  |     Create a Stack (List)     |
| my_stack.append(value) | Add Value to top of the stack |
|  value = my_stack.pop()  |     Remove last item added from stack     |
|  *Other List Functions*   |    *Functions that relate to stacks*     |

Using the syntax above consider why the output of the following code is what it is:

```Python
my_stack = []

my_stack.append("Dog")
my_stack.pop()
my_stack.append("Cat") 
my_stack.append("Rat") 
my_stack.append("Bird") 
my_stack.pop()
my_stack.pop()

print(my_stack)

#Output: ["Cat"]
```

#### **Explanation - When the code runs, it will follow this sequence:**
1. Create a new list (aka stack) entitled `my_stack`
2. Add "Dog" to the stack
3. Remove "Dog" from the 
4. Add "Cat" to the stack
5. Add "Rat" to the stack
6. Add "Bird" to the stack
7. Remove "Bird" from the stack
8. Remove "Rat" from the stack
9. Print the stack - which leaves you with just `["Cat"]`

Sometimes programmers think that `append(value)` will add the value to the front of the list, but this is not the case! When using `append(value)` and `pop()` It is always adding and taking from the back of the list.

## Problem to Solve : Retracing your Steps!

You know that you lost your keys at the location you were at right before you went to the library. Write a program that stores your days path in a stack and then pops off values until you find the solution directly before the library! You need to retrace your steps!

_The Path that you should take is as follows:_

|   Order   |      Path      |
| :-----: | :------------: |
| 1 | Bedroom |
| 2 |    Gas Station      |
| 3 |     The Office      |
| 4 |     The Library     |
| 5 | Restaurant |

You can test your program by verifying that your program prints off the location just prior to "The Library". In otherwords it will need to print to the screen the string, "The Office":

You can check your code with the solution here: [Solution](retrace_steps.py)



[Back to Welcome Page](0-welcome.md)



