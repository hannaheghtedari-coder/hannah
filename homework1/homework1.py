# File: homework1.py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, so a whole number without decimal pts
b = 1.5
print(b)
print(type(b)) # b is a float, aka a number that is either a fraction or decimal
c = 3j
print(c)
print(type(c)) # c is a complex, which is a real number and the imaginary number (j)
d = "hello"
print(d)
print(type(d)) # d is a string, which is a series of letters/ words (apparently it can include #s)
e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, which is denoted by the [] square brackets, and its order can be changed
f = {"name": "Hannah", "favorite fruit": "watermelon"}
print(f)
print(type(f)) # f is a dict, or dictionary, where the key (like a term) can't be changed but the value (definition) can
g = (1,2)
print(g)
print(type(g)) # g is a tuple, which is marked with the () parentheses, and the order is fixed
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is another list, like e, but a list of strings rather than integers
i = True
print(i)
print(type(i)) # i is a bool, which includes True/False and evaluates "truth value" CASE SENSITIVE
j = None
print(j)
print(type(j)) # j is a NoneType, signifying the absence of there being a value (no other input in this type)
k = [True, "blue", 12]
print(k)
print(type(k)) # k is another list, note the brackets
l = str(14)
print(l)
print(type(l)) # l is a string even though the "14" looks like an integer because of the str string function... there is something similar with dict
m = 1e4
print(m)
print(type(m)) # m is a float because the e stands for exponent and even though this seems like a large integer, python adds a decimal (even .0) in this function format, making it a float
""" 
Questions:
1. I found a total of 9 datatypes, as some of the variables were repeats menat to show how dynamic a datatype is. (lists, especially)
2. 9 datatypes found: integer, string, float, complex, tuple, bool, NoneType, dict, and list.
3. e, h and k are all lists. both b and m are floats. d and l are strings.
4. l is a string and not an integer, despite print(l) outputting 14, because the str() function converts whatever is inside the parentheses to a string. Also, strings can include numbers, but if there are no letters and no str() function, numbers will (likely) default to int/float. 
"""
# 5. 
n = {1, 2, 3, 4}
print(n)
print(type(n)) # n is a set, which is naturally unordered but also immutable in that it can't be changed later, and also cannot contain duplicates

# --- Booleans --- 
print(10 > 9) # True: 10 is greater than 9
print(10 ==  9) # False: 10 is not equal to 9
print(10 <= 9) # False: 10 is not less than or equal to 9
print(bool("abc")) # True: the string is not empty
print(bool(123)) # True: 123 is non-zero
print(bool(["apple", "cherry", "banana"])) # True: the list is not empty
print(bool(True)) # True: true is already true
print(bool(False)) # False: false is already false
print(bool(0)) # False: zero is not non-zero (0 is 0), also apparently in binary 0 is false and 1 is true
print(bool("")) # False: the string is completely empty
print(bool(" ")) # True: the space in the string makes it not empty
print(bool(())) # False: the parentheses just convey an empty tuple, even though they are within each other
print(bool([])) # False: the brackets convey an empty list (and empty is inherently false)
print(bool({})) # False: similarly, the curly brackets are also false as an empty set (look at my variable n from before)
print(bool(True and False)) # False: something cannot be true and false at the same time. If both options are true, it is true. if one or both are false, it is false. (kind of like convergence/divergence operations in calculus)
print(bool(True and True)) # True: both arguments are true
print(bool(False and False)) # False: both are false, it is not like negatives where two make a positive, more like double negatives in spanish language (just reinforces the negative rather than cancelling it out)
print(bool(True or False)) # True: at least one of these two values is true (apparently overriding the false)
print(bool(True or True)) # True: at least one of the two is true (in this case, both are)
print(bool(False or False)) # False: at least one of the two is false (in this case, both because the one or the other defaults to true)
print(bool(not(False))) # True: True is the opposite of False (not will negate the inner argument)
print(bool(not(True))) # False: False is the opposite of True, which the not canceled out. 
"""
Questions:
1. I notice that whenever something is empty or non-zero, it is false. Expressions with values tend to be true since they are neither zero nor empty, except of course for the blatantly false expressions, like 10 = 9.  The and/or/not statements seem pretty straightforward once you think about it like statistics. 
2. True or False surprised me the most because I didn't know which output would result seeing as there was one of each (and I though the or meant at least one)... now I've learned that in the 'or' commands, true will override false.
"""
#3
print(bool(12 != 7)) # True: the != means not equal to, and 12 is not equal to 7.
#4
print(bool(not(True or False))) # False: we learned that in the or expressions, True will override False. The not will negate that, resulting in the opposite, so the final result is False.

# --- Operators ---
# Arithmetic
print(10+5) # 15, + performs addition
print(10-5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division (and has float output)
print(5 % 2) # 1, %, or modulus, performs divison on integers and outputs the remainder  
print(3 ** 2) # 9, ** raises the following value to the exponent, so it is 3*3, or 9
print(15 // 2) # 7, // performs division on integers and will round the result down, or in other words, leave out the modulus, unlike traditional division (hence the float in regular division)
# Comparison
print(5==2) # False: 5 is not equal to 2
print(10 != 10) # False: 10 is equal to 10, so saying it is not equal to itself was false
print(2 < 5) # True: 2 is less than 5
print(12 > 5) # True: 12 is greater than 5
print(5 <= 6) # True: 5 is less than or equal to 6
print(1 >= 10) # False: 1 is not greater than or equal to 10
# Assignments
x = 5
x += 5
print(x) # 10: 5 + 5 = 10 (the equals sign will change the value of x)
x = 5
x -= 4
print(x) # 1: 5 - 4 = 1 (the equals sign assigns this new value to the variable)
x = 5
x *= 3
print(x) # 15: 5 * 3 = 15 (assignment again, note the overriding of the previous x)
# Logical
# 1. "and" will require that both (or multiple) arguments agree. Thinking of a Venn Diagram, "and" only works for the overlap
y = 7
print((y == 7) and (y >= 4)) # True: 7 equals itself and is greater than (or equal to) 4.
print((y != 7) and (y > 6)) # False: 7 is greater than 6 but it cannot be unequal to itself, and due to the "and", both statements need to be true.
# 2. "or" only needs one of the two (or more) expressions to be true to output "true". Thinking of a Venn Diagram, "or" is the area that encompasses both circles. However, for an or statement to be false, both/all must be false.
print((y == 7) or (y == 5)) # True: even though 7 is not equal to 5, it is equal to 7.
print((y < 2) or (y > 8)) # False: 7 is neither less than 2 nor graeter than 8.
# 3. "not" will negate the inner argument/ make the output the opposite. In a Venn Diagram, "not" would be whatever is outside the target argument (if A, everything outside the A circle; the same for B; if A and B, then everything besides the overlap, if A or B, then just the part outside the circles)
print(not(y == 3)) # True: 7 is not equal to 3, so instead of false, the not makes it true.
print(not(y == 7)) # False: 7 is equal to 7, so the not turns the true into a false. 
"""
Questions:
1. / is traditional division, which will result in a float and includes/divides the remainder. // is integer divison, which leaves out the remainder, effectively rounding down to the highest integer that the statement is divisible by.
2. % and // are like the two pieces of /. The modulus (%) is the remainder, and the integer division (//) is the quotient. Traditional divison is the quotient plus the modulus divided up regularly (into a fraction or decimal)
3. I would use the %, or modulus, to calculate the remainder when dividing two numbers, such as 20 divided by 3. 20 % 3 would output in 2, as 3*6 = 18 is the highest clean quotient, and 20-18 is the remainder of 2. 
4. Assignment operators work to reassign a variable a new value, essentially updating it. For example, isntead of printing x + 5 and having to remember that in the erst of my code, I can use the assignment operator  x += 5 to make the new value of x as 5 greater than it was previously, so that when I call print(x), I get this new value.
"""

# --- Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h, the first letter of the string
print(my_string[1]) # Prints: e, 2nd letter of my_string
print(my_string[2]) # Prints: l, 3rd letter of my_string
print(my_string[3]) # Prints: l, 4th letter of my_string
print(my_string[4]) # Prints: o, the 5th letter of my_string
print(my_string[-1]) # Prints: o, last letter, OR the first letter of my_string BACKWARD
print(my_string[1:3]) # Prints: el, the 2nd and 3rd letters, as the "3" boundary is excluded
print(my_string[0:5:2]) # Prints: hlo, starting from the 1st letter to the non-existent 6th (so that the 5th letter o is included!), taking every other (every 2nd) letter.
print(len(my_string)) # Prints: 5, since my_string has 5 characters/letters (doesn't start at 0 since this is an issue of quantity, not position indexing like before)
print(my_string + ", goodbye") # Prints: hello, goodbye because I used the addition operator to add to the printed string, and within the quotation marks I added a comma and space, otherwise the result is: hellogoodbye. 
print(my_string * 7) # Prints: hellohellohellohellohellohellohello, aka my_string 7 consecutive times.
'''
Questions:
1. Slicing means taking individual characters/letters from a string/sequence, not taking a range of all values. I sliced my_string in the operations where indexing  with [] also used a colon : to select specific individual letters. (aka subproblems 8 and 9)
'''
# 2.
name = "Oski"
print("Hello, my name is", name) # Prints: Hello, my name is Oski; requiring a separation between the code and string of text
# 3.
name = "Oski"
print(f"Hello, my name is {name}") # Prints: Hello my name is Oski; allowing for code to be inputted among text using {curly brackets}. 
# 4. A regular string needs to use operators to join variables and text, and when using longer strings, is less efficient. F-Strings allow users to embed variables/code into the strings of text, not requiring operators but just {curly brackets}!

# --- Terminal Commands ---
'''
1. cd 
 1.1 cd stands for change directory (navigate folders)
 1.2 I can use it to go within another folder by calling cd with the name of the folder, or go backward by doing cd ..
 1.3 cd Screenshots
2. ls
 2.1 lists contents.
 2.2 Use it to see the titles of folders or files within a directory
 2.3 ls -a (shows hidden files like in lecture)
3. ls -a 
 3.1 lists hidden files as well.
 3.2 Okay so I was a little trigger/keyboard happy before. I guess for 2.3 I could just call it after doing cd into an appropriate directory. And I can use ls -a to see hidden files like a git repository.
 3.3 ls -a in homework directory to see hidden git repository too. 
4. mkdir
 4.1 make directory (makes folders)
 4.2 I can use it to make additional folders within a directory.
 4.3 mkdir homework 1 inside my name inside the decal directory
5. cat
 5.1 concatenate: display the contents of a file (or join together items)
 5.2 Use it to show all the code in a file, such as the datatypes.py one from the first lecture
 5.3 cat datatypes.py (would show the code written in the file)
6. pwd 
 6.1 print working directory (shows entire folder path)
 6.2 I can use it to check which directory I am currently in, as well as the outer "nesting dolls" of the directories encompassing it.
 6.3 pwd in /hannah/ would show /c/Users/Hanna/python_decal_sp26/hannah
7. cd ..
 7.1 Changes Directories outward (or backward)
 7.2 Use it to get out of the directory you are currently in and go back to its parent directory.
 7.3 cd .. to leave the hannah folder and go back to the main decal one
8. cd .
 8.1  current directory
 8.2 Doesn't change your location, but good for later applications of keeping track of current directory or recovering it after changes have been made.
 8.3 cd . to stay in current directory
9. cd ~ 
 9.1 Home directory
 9.2 Use it to change your working directory back to the home directory, sometimes specified with your user name
 9.3 cd ~, I end up having to call it every time I open Git as I don't know if I've done something, but it is never ready to start in the home directory but require me to open it up first.
10. cp
 10.1 Copies files or directories
 10.2 Use it to duplicate files and move them to new directories
 10.3 cp -R homework1 python_decal_sp26 (meant to copy contents of folder/file of homework 1 into the general decal directory... still a little lost on recursive flag)
11. mv
 11.1 Moves Directories
 11.2 Use it to move a directory or rename it
 11.3 mv homework1 hw_1 (meant to change the name of the directory from homework1 to hw_1)
12. rm
 12.1 Remove Directory/ Files
 12.2 meant to remove  files and (empty?) directories
 12.3 rm unnamed_file would get rid of that file
13. clear
 13.1 Clears your terminal
 13.2 Use it to get a blank slate on the terminal, as was done on Monday's lecture, without undoing the previous code
 13.3 clear in terminal to refresh the page and continue (not restart) on a blank terminal
14. grep
 14.1 Searches for Text in a File
 14.2 Use it like effectively like a CTRL F for the terminal to find patterns in files/code/text
 14.3 grep "hello, world!" datatypes.py would search that file for that exact, case-sensitive text (so it wouldn't find anything, as I capitalized it in the file)

Questions:
1. 3 other commands
1.1. head, shows the first ten lines of a file, which would be especially useful if your titles aren't descriptive enough and you need to remember the contents
 1.1.1 head datatypes.py would show the first couple of lines of the code
1.2 exit, closes out the terminal session, probably better than just closing the tab itself. 
 1.2.1 exit  would end the session
1.3 nano, would allow you to go in and edit a file through the terminal (a window pops up, like in class)
 1.3.1 nano datatypes.py would let me write new code in that file in terminal rather than opening VS code

2. ls just shows traditional files, typically ones you've directly made (If you go in the file explorer, you can easily see them). ls -a would show those files as well as hidden contents of a directory, such as the git repository and ./..
3. A hidden file includes dot files and repositories (like git), not hidden due to security but just because they likely aren't useful to an average user (case in point: this class is how I found out you can see such files). The dot files hot things like settings/ preferences for configuration.
4. 
 -i is a flag that you could apply to grep and make it case insensitive, so it would now show results for the previous example.
 -R, Recursive Listing, is a flag that would allow for recursive listing or copying through the directory pathway (see cp -r example)
 -l, for Long Format Listing, is a flag that would not only list the contents but would include more details. (especially useful if files have similar names and need to quickly differentiate)
'''
# checkoff : GitBash