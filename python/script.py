import glob
import os
import subprocess
from pathlib import Path

path = "/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/md/"
subprocess.run(["rm", "-rf", "/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/md/*"])

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
    try:
        os.makedirs(path + folder_name)
    except:
        pass
    with open(file, 'r') as f:
        file_to_edit = ""
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
                chap_no = list_to_string_without_space(split_string[1:])
                if len(chap_no) == 1:
                    chap_no = "00"+chap_no
                elif len(chap_no) == 2:
                    chap_no = "0"+chap_no
                file_to_edit = path + folder_name + "/" + "chap-" + chap_no +".md"
                Path(file_to_edit).touch()
                continue
            if split_string[0] == "\\v":
                continue