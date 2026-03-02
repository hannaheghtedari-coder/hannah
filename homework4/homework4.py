# File Name: homework 4 python decal
# --- Lists ---
# Favorite Foods
fav_foods = ["cotton candy ice cream", "watermelon", "ramen", "tacos", "cucumbers"]
print(fav_foods[1]) # python starts at 0, so 2nd item is 1
print(fav_foods[-1]) # negative indexing starts at -1 from the back
fav_foods.append("bananas")
fav_foods.insert(0, "apple")
fav_foods.remove("watermelon") # RIP watermelon, was previously the 2nd item (printed), got deleted as the insert made it the new 3rd item
print(len(fav_foods)) # expect len = 6 ; initially got len = 7 because i forgot to remove the third item
for item in fav_foods:
    print(item.upper())
"""
I encountered this error:
Attribute Error: list object has no attribute
I originally wrote: for item in fav_foods.upper():
                        print(item)
I didn't use the upper function properly and then when I tried fixing it, I accidentally kept the parentheses and got a syntax error for a list not being callable.
Fixed it by putting .upper in the body of the for loop and removing parentheses from beginning
"""
modified_fav_foods = fav_foods[0:6:5] # takes first value, then skips 5 since total length is 6 
print(modified_fav_foods) # expect apple and bananas

if "potato" in fav_foods:
    print("A potato!")
else: 
    print("No potato!")

# Slicing and Striding
numbers = list(range(0,21))
def get_first_15(numbers_list):
    return numbers_list[:15]

def get_every_5th(lst):
    # Slicing with a step of 5
    return lst[::5]

def reverse_and_stride(lst):
    # Reverse the list like in lecture
    reversed_list = lst[::-1]
    # Return every 3rd element of the reversed list
    return reversed_list[::3]

# Putting it All Together
step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step3) # expect 10 as the output (step 1 is 0-14, step 2 is 0, 5, 10, and step 3 is 10, 5, 0 then just 10 since the list is every 3rd and is only 3 long)


# Nested Lists (Like Arrays?)
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numbers_nested = [list_1, list_2, list_3] # renamed the list to numbers_nested because the previous problem uses numbers and that is honestly just confusing and I'm sure it would result in errors later on
print(numbers_nested[2]) # should print 7, 8, 9
"""
I encountered this error:
No Output
I originally wrote: numbers_nested[2]
I forgot the print() statement because I was going off the lecture slides and they don't have a print statement but honestly I don't know why I didn't just use common sense but oh well. (I mean the problem literally says print but I just decided to be baffled for a good couple of minutes about no output)
"""
print(numbers_nested[1][1]) # should print 5
list_4 = [10, 11, 12]
numbers_nested.append(list_4)
def sum_nested(nested_data):
    count = 0
    for item in nested_data:
        if isinstance(item, list):
            count += sum_nested(item) # goes through lists first, then sums all numbers per row (list)
        else: 
            count += item
    return count
print(sum_nested(numbers_nested)) # should expect 78
# 5x5 Lists
def five_by_five():
     nested_list= []
     count = 1
     for i in range(5):
         row = []
         for j in range(5):
             row.append(count)
             count += 1
         nested_list.append(row)
     return nested_list
# print(five_by_five()) I could/ did  do this, but it just strings along the lists and doesn't format in rows and columns besides the brackets
for row in five_by_five():
    print(row)
"""
I encountered this error:
Indentation Error: nested_list.append(row) does not match indent
I originally wrote nested_list.append(row) after changing the count, so I pressed enter and then backspace,
and even though it looks in line with the for j in range/ for i in range, it needs an extra space to match indent and run properly.
"""
def replace(grid):
    new_grid = []
    for row in grid():
        new_row = ["?" if num % 3 == 0 else num for num in row] 
        new_grid.append(new_row)
    return new_grid
for row in replace(five_by_five):
    print(row)    # did it in class on 2/26 with Katie's help!

def sum_of_replace(grid):
    count = 0
    for row in grid:
        for value in row:
            if value != "?":      # hopefully skips the question marks
                count += value
    return count

print(sum_of_replace(replace(five_by_five))) # expected = 217



# --- Dictionaries ---

ages = {"Katie": 30, "Mariam": 42, "Safia": 25, "Mira": 48}
print(f"Katie's Age: {ages["Katie"]}")
"""
I encountered this error:
Type Error: object is not subscriptable
I originally wrote: print[f"Katie's Age: {ages["Katie"]}"]
I accidentally put brackets for the print statement and not parentheses. 
"""
"""
I encountered this error:
Name Error: "ages" is not defined
After fixing the print issue, I got a little keyboard happy and pressed shift enter to run instead of clicking the triangle to run all,
which meant that just that line ran and so the terminal didn't recognize the previous lines of code/ defined dictionary. Running it again correctly fixed this.
"""
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for key, value in ages.items():
    print(f"{key} = {value}") # expected: Katie: 30; Safia: 25, Mira: 100, Milana: 52
