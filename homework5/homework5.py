# File: Homework 5 -- Review
"""
Vocab Review:
1. Git vs GitHub: Git is the software/ language running in my command line/ terminal (connected to my local repository), GitHub is an online application that runs my remote repository.
2. Terminal vs Command Line: Terminal is the application (I just open terminal and select GitBash or Anaconda prompt depending on what I want to do) and the Command line si the actual line in the terminal where you run code/commands.
3. Local vs Remote Repository: The local repository is yoru code/ files/directories stored on you personal computer, while the remote repository is online/ on a server, like GitHub, allowing others to access your code too.
4. Version Control: tracks changes to code and files (history) 
5. Staging Area: in Git, a place to "prep" code changes before committing, aka where the first step of git add takes place.
6. git add: first step of saving changes to repository. Specifically, stages changes in the aforementioned staging area. If done correctly, no output.
7. git commit: secomd step of saving changes to LOCAL repository. Running it (with message so that you know your steps/ what was committed when) should output what has been changed/created.
8. git push: third step of saving changes to REMOTE repository. Running this requires your SSH Key to access your Github repos. 
9. git status: outputs information about the current staging area (which branch, changes made)
10. git pull: updates a local repository based on the new version of a remote repository. For example, when the course assignments section of the remote repo for the decal is updated, we run this to get pertinent info for our homework that week (to be able to copy files).
11. pwd: print working directory, shows you your absolute path
12. ls: lists the contents of your current working directory
13. cd: change directory, use it to move in and out of folders
14. nano: allows you to edit files in the command line. running nano and a new file name also will create a file then open it.
15. touch: allows you to create files in the command line, but not edit
16. mv: move. used to both move files/ directories and able to change their names as well (for example, I use it a lot to change the names of screenshots but my fatal flaw is forgetting to add .png so O can open them)
17. rm: remove. can use it to delete files/directories, but be careful!
18. cat: concatenate. when run, lists all the code and text in a file, so that rather than just running python3 in terminal to get outputs, running cat will show outputs, code, and comments!
"""
# --- Directory Tree ---
"""
pwd will tell you the path to your current working directory
ls will show you all files and folders in that directory
I would call cd ../brianna_repo to directly move to that repository, and then I'd call git pull (and origin depends on the branch of repo)
mv homework.py ../judy_decal/homework should move the copied new homework file to the desired folder
I would also then call cd ../judy_decal/homework
to open a python file in terminal, I could either say cat and then the file name to show the text/code/comments, or if I wanted to RUN the contents, I could go ahead and just call python3 <file>
git add .; git commit -m "done with homework from this week!"; git push origin main (assuming it is the branch main and that homework has no number attached)
try git pull origin main first to see where the discrepancies lie (remote repository isn't synced/ doesn't match what you have apart from the changes you are trying to make), so you have to finish adding to your local (pull) before you can push again.
Recents is ~/Recents, so I'd need to call cd .. thrice to then cd into Recents. (aka cd ../../../Recents)
"""
# --- HW Review
def check_datatypes(input):
    print(type(input))

# check_datatypes(True)  # returns bool
# check_datatypes(45.09) # returns float

def even_or_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
# even_or_odd(42) # returns even

numbers = [1, 2, 3, 4, 5]
def sum_with_loop(list):
    count = 0
    for num in list:
        count += num
    print(count)

# sum_with_loop(numbers) # 15

alphabet = ["a", "b", "c", "d"]
def duplicate_lists(list):
    new_list = []
    for item in list:
        new_list += 2*item
    print(new_list)

# duplicate_lists(alphabet) # returns desired outcome

def square(num):
    return(num*num)
# Debugging: The error was the missing colon after the def name statement
# print(square(25)) # returns 625
