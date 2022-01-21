import glob
import os
from pathlib import Path

path = "/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/md/"

def list_to_string(s): 
    str1 = " "  
    return (str1.join(s))

def list_to_string_without_space(s): 
    str1 = ""  
    for ele in s: 
        str1 += ele
    return str1 

for file in glob.glob("/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/usfm/*"):
    folder_name = (Path(file).stem)
    with open(file, 'r') as f:
        book_name = ""
        chapter_number = 0
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            split_string = line.split()
            if split_string[0] == "\id":
                continue
            if split_string[0] == "\mt":
                book_name = list_to_string(split_string[1:])
                # print(book_name)
                continue
            if split_string[0] == "\p":
                continue
            if split_string[0] == "\c":
                continue
            if split_string[0] == "\\v":
                continue