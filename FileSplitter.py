#FileSplitter
# Small program to split one large file into multiple smaller ones
# File must have one entry per line

import math


def file_select():
    global main_file
    print("Welcome to FileSplitter!")
    main_file = input("Enter the path full path to the file you'd like to split (Just the filename works if file is in the same directory): ")
    count_lines(main_file)
#Counts the lines in the file
def count_lines(file):
    global total_linecount
    total_linecount = 0
    with open(file, "r") as file:
        for line in file:
            total_linecount += 1

    print("Total lines in main file: ",  total_linecount)

# Set the configuration for the split
def config_split():
    global num_of_files, lines_per_file
    
    lines_per_file = int(input("How many lines would you like per file? (Leave blank for an even split per file): "))

    # num_of_files = int(input("How many files would you like to split this into?(2 or more): "))
    num_of_files = math.ceil(total_linecount / lines_per_file)

    outfile_create()

def outfile_create():
    global num_of_files, file_list
    file_list = []
    print(f"We will need {num_of_files} files to have {lines_per_file} lines in each. (Last file may have less)")
    usr_input = input("Is this ok? (y/n): ")
    if usr_input == "y":

        files_created = 0 
        
        while files_created < num_of_files:
            new_file = f"{main_file}-SPLIT0{files_created}"
            open(f"{new_file}", "w")
            file_list.append(new_file)
            print(f"[!] Created {new_file}")
            files_created += 1
            print(file_list)
    else:
        print("'n' detected or invalid input. . quitting!")

def file_split():
    global lines_per_file, file_list
    lines_written = 0
    # for out_file in file_list:
    #     with open(f"{main_file}", "r") as in_file:
    #         with open(f"{out_file}", "a") as out_file:
    #             for line in in_file:
    #                 if lines_read < lines_per_file:
    #                     out_file.write(line)
    #                     lines_read += 1
    #                 else:
    #                     lines_read = 0
    #                     break
    line_to_write = None
    with open(f"{main_file}", "r") as in_file:
        for line in in_file:
            if lines_written < lines_per_file:
                if line_to_write is None:
                    with open(f"{file_list[0]}", "a") as out_file:
                        out_file.write(line)
                        lines_written += 1
                else:
                    with open(f"{file_list[0]}", "a") as out_file:
                        out_file.write(line_to_write)
                        out_file.write(line)
                        lines_written += 2
                        line_to_write = None
            else:
                lines_written = 0
                line_to_write = line
                file_list.pop(0)



    # line_to_write = None
    # with open(f"{main_file}", "r") as in_file:
    #     for line in in_file:
    #         if lines_written < lines_per_file:
    #             if line_to_write is not None:
    #                 with open(f"{file_list[0]}", "a") as out_file:
    #                     out_file.write(line_to_write)
    #                     lines_written += 1
    #             line_to_write = line
    #         else:
    #             lines_written = 0
    #             file_list.pop(0)
    #             line_to_write = None

        



file_select()
config_split()
file_split()

