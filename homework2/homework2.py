# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
"""
Git is a tool to track code changes.
GitHub runs/hosts remote repositories
GitBash runs your local repositories and command line (terminal); Bash is a shell 
language on Git.
"""
# 2) What’s the difference between the terminal and the command line?
"""
Terminal is the application (including GitBash), command line is 
the actual code (in our case, Git commands) ran inside the terminal.
"""
# 3) How does Windows PowerShell differ from Git Bash?
"""
Powershell is its own separate language that is standard to windows computers (like this one!), 
while Git Bash (or Bash) is a different language using Git Linux commands that basically everyone else
uses except Windows, which is why I had to get Git Bash as a separate terminal application and then
connected it to my terminal app so that its default language is Bash and not Powershell. 
"""
# 4) What’s the difference between Anaconda, conda, and Python?
"""
Anaconda is a distribution package that includes Python, conda, and tools like Jupyter Lab
(which I use for ULAB). conda manages and runs Python and other installed programs in environments
(for example, I have a "base" environment and a "MAVEN" environment in conda within my Anaconda 
Navigator that run different versions of Python with their own packages). Python is the programming language
that the code is in (apart from Git commands in the terminal).
"""
# 5) What is VS Code?
"""
Visual Studio Code, described in lecture as Google Docs for coding, lets you code and run files 
(and see/manipulate directories), including its own built-in terminal and option for extensions.
For example, we do most of the lecture demos in VS Code and need the Python Extension to do so.
"""
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
"""
I use Jupyter Lab almost weekly for ULAB, and I especially like that I can have multiple files open at once;
but Jupyter Notebook is the original, older version where you only have one file open/working at a time.
There is no terminal, and code runs in each individual cell, which makes it different from (and more beginner-friendly 
than) VS Code.
"""
# 7) What does ~/ mean?
"""
The ~/ stands for the home directory. For example, opening up terminal
should show ~ to signal that you are in the home directory, and if you
aren't upon opening or need to get back to it, you can call cd ~ to get
back home.
"""
# 8) What’s the difference between an absolute path and a relative path?
"""
The absolute path is your path (or call pwd) from the home directory (~) to where you are/ where you want to go. 
The relative path is the path from where you are to where you want to go. 
"""
# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
"""
Absolute Path: /c/Users/Hanna/python_decal_sp26/course_assignments/homework_2
Relative Path: cd ../course_assignments/homework2

The Absolute Path shows the full path to the desired directory (hoemwork 2) from home, 
while the Relative Path shows how to get to homework2 from where I am, which is in my 
"hannah" folder, so I would need to call "cd .." first to get back to the main python_decal_sp26 
directory and then enter course assignments then homework 2 from there. cd is versatile so rather
than having separate commands, I can call the entire relative path to move.  
"""
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
"""
Command: cd ..
Rationale: Going from course_assignments/homework2/ to /course_assignments/ is a simple backwards step, so I'd only need to 
run "cd .."
"""
# 11) What would rm ./ do in your current directory? (Don’t try it!)
"""
rm ./ would try to delete your current directory. rm is the command learned last week to remove/delete,
and from working with cd, ./ is meant to signify your current directory/location.
"""
# 12) What do the following commands do?
# git add 
"""
adds new/ changed files (essentially updates based on changes you've made)/ signals what will be saved.
Usually we run it as git add . to note all changes. (aka staging)
"""
# git commit  
"""
Saves all changes on your computer/ local repository. 
"""
# git push 
"""
Saves all changes/ takes all local saved changes and updates your remote repository (GitHub).
"""

# 13) What's the difference between "git add ." and "git add <file>"?
"""
git add . is a general command saving all changes / recognizing all changes in current directory, 
meant to then be reinforced and saved with git commit.
git add <file> is the same command but only for that specific file (for minute and specific changes).
"""
# 14) What do "git status" and "git log -1" do?
"""
git status shows you the current changes (aka your status) including stages. git log -1 shows your 
most recent commit history (git log for commit history, -1 flag for most recent). One shows the current
situation, one shows what has already been done. 
"""
# 15) What’s the difference between cloning a repository and pulling from it?
"""
Cloning a repository, like what we did with course assignments, is akin to copying a shared folder in Google Drive
and making your own personal copy from the downloads.  (looks at a GitHub repository and gives you your own new
local version)
Pulling from it will sync your copy with any updates (looks at a GitHub repository and applies changes to what you 
already have).
"""
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
"""
The most frustrating and confusing error was my issue with my GitHub and SSH key, and how it didn't connect to my computer 
even though the first time I did this in September it (allegedly) worked. I got help from Brianna and Katie, and the 
ultimate fix to avoid deleting everything or redoing my SSH key was removing the "connecting" and trying to reconnect 
my local and remote repositories (complete with "maybe push?" named commits) by redoing teh git init and push steps.
Still unlcear on what caused the error in the first place, but now we have a fix!
"""
# 17) What’s a question you still have? What’s something you’re confused about?
"""
I'm still confused as to why when I press enter or shift+enter to try and run code in VS code that the terminal "gets mad"
at me and hits me with errors that don't quite make sense to me... but also the instructors (at least a couple of them) seemed 
to have similar issues so I guess its a VS Code quirk and that's why we only click the play button to run. 

Also a little miffed honestly (not at any instructors/ real person) as to why I felt like I was told somewhere that Windows would
serve me better in college in general, including being more powerful to run code, only to learn (not just through here; again, 
not upset with anyone here just a general idea) through experience that most coding things are catered to apple/ not windows (terminal, 
code, etc)... basically what I'm trying to say is RIP Windows users (myself included). Though I do like having a touchscreen so overall
still pretty happy with what I've got.
"""
# 18) Tell me a fun fact!
"""
I don't know if you wanted a python fun fact but this is computer-related. I just learned/discovered for myself
(maybe you already knew) that if you type in the name of a (well-known) font into Google, the result isn't just normal 
quick answer info/ relevant websites, but everything is IN THAT FONT. 
"""
# 19) Print your favorite math expression you've learned in Python so far.
# (Hint: Use print() and add a comment explaining what it does.)

print(42 % 4) 
"""
the modulus, or %, is the remainder after doing clean
integer division. I happened to like it since it's a newer sort of
expression compared to traditional arithematic operators common in
even the most basic calculators. This particular expression should
output 2, because 40 is cleanly divisible by 4 and 42-40 = 2.
"""

