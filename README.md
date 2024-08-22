# WELCOME TO FILESPLITTER
Cut down those large files of yours!

## PREREQUISITES
- EXE / Binary version in "Releases"
FileSplitter works for large files with one entry per line, of any length. Something like this:

![Example of what a file should look like for FileSplitter to work ](https://github.com/lmmcntsh/FileSplitter/assets/112915632/d5d2bb22-fe5e-4ef5-b5ae-bd9cf3e38641)


## USAGE
### Running The Program
Download the program, navigate to the directory where it is stored, and run it using Python. (EXAMPLES BELOW SHOW BOTH LINUX AND WINDOWS METHODS)

**Bash Shell**\
![Bash Shell running FileSplitter](https://github.com/lmmcntsh/FileSplitter/assets/112915632/174f10a3-192c-4405-b209-48df62cef875)

**Windows CMD**\
![CMD running FileSplitter](https://github.com/lmmcntsh/FileSplitter/assets/112915632/f4023919-7ef6-402a-b219-fad34a5eced0)

### Selecting Your File
First, when prompted, enter the full path to the file you wish to split. If FileSplitter is in the same directory as the target file you can simply enter its name.

**Full Path**\
![FULL PATH EXAMPLE](https://github.com/lmmcntsh/FileSplitter/assets/112915632/a8f0c287-aaf3-4ee4-9530-6b1414671310)

**Just the file name (testFile.txt and FileSplitter.py are in the same directory)**\
![File name example](https://github.com/lmmcntsh/FileSplitter/assets/112915632/e84c1dda-d9be-45eb-b40f-fcef3480de23)

After selecting your file, FileSplitter will automatically count the number of lines/entries in your file and give you the total.

### Configuring Your Split
After your main file is chosen you will be asked how many lines per file you would like.
![image](https://github.com/lmmcntsh/FileSplitter/assets/112915632/ca53e9d4-80f0-417f-9990-2378a6fbb6f3)
It will check your file's total size and tell you how many files it will create to reach your desired split. You can hit "y" to confirm and continue or "n" to quit the process. 

*Will be adding the ability to set an output directory but for now, files will just be created in the same directory as the main file.*

## RETRIEVING YOUR FILES
After the final confirmation, the files will be created under the same name as your target file, being stored in the same directory. You can see an example below \
![image](https://github.com/lmmcntsh/FileSplitter/assets/112915632/c05c86a7-8ff5-4e4d-9cf6-76ee0865fd50)




