# Junk File Organiser
Arranging files on your computer is just like arranging anything else. Say you want to organize your clothes. You might arrange each type of clothes into separate stacks or you could throw everything into one place and hope you can find the right pair of clothes when you need it. And that's how we typically treat our files: we save files randomly to our Desktop and Documents folders, then waste time searching for files every day.
This is very useful for Lazy programmer who keeps bunch of files and folders at one location and sometimes he is in lot of confusion about
which files are present. It is very boring task to manually arrange all the files into one folder.So This a python programm to organise everything in the single go in a blink of an eye.

We have a directory named ***organized*** inside which all the files of respective types are present in the respective folders

### prerequisites
- python 3.8 (Install this from the  official website https://www.python.org/)
- Basic knowledge of how to use command prompt, how to copy and paste files ..
### How to run
- Copy the setup.py to the desired location where we want to organise the folders.
- After that double click on the Setup.py file. That's it.
- We can run the script using command line too...

### Screenshots:
- Before running the script:
![](https://github.com/attainu/Manindra-au7/blob/dev/Project/before.JPG)
- After running the script:
![](https://github.com/attainu/Manindra-au7/blob/dev/Project/after.JPG)

### Requirements:
- usage of os module
- usage of shutil module
- File handling in python
- recursion

### Approach:
1. Create different folders based on type of files we are going to segregate into different folders using dictionaries.
2. Create the map of file types into their respective folders.
3. Create a function to filter file types into their respective folders
4. Use os module of python to recursively list out all the files that are present in the folders with their relative and absolute path 
5. Using Shutil module of python, move all the folders into a newly created "organized" folder.
6. After running the above setup in the required destination, the output will be something iike as shown in the above image.
7. A folder named "organized" is created inside which all the sub-folders based on the respective type are present. 

### Built using:
1. Python language
2. The code is built according to the standard pep8 rules and regulations.
