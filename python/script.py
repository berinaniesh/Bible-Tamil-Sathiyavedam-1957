import glob
import os
import subprocess
from pathlib import Path

# base_path = "/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/"
# pdf_path = "/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/pdf/"
# pptx_path = "/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/pptx/"
md_path = "/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/md/"

subprocess.run(["rm", "-rf", md_path])
# subprocess.run(["rm", "-rf", pptx_path])
# subprocess.run(["rm", "-rf", pdf_path])

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
        os.makedirs(md_path + folder_name)
    except:
        pass
    with open(file, 'r') as f:
        file_to_edit = ""
        book_name = ""
        chapter_number = 0
        verse_number = 0
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            split_string = line.split()
            if split_string[0] == "\id":
                continue
            if split_string[0] == "\mt":
                book_name = list_to_string(split_string[1:])
                continue
            if split_string[0] == "\p":
                continue
            if split_string[0] == "\c":
                chapter_number = split_string[1]
                chap_no = list_to_string_without_space(split_string[1:])
                if len(chap_no) == 1:
                    chap_no = "00"+chap_no
                elif len(chap_no) == 2:
                    chap_no = "0"+chap_no
                file_to_edit = md_path + folder_name + "/" + "chap-" + chap_no +".md"
                Path(file_to_edit).touch()
                file1 = open(file_to_edit, "a")
                file1.write("---\n")
                file1.write("title: " + book_name + " " + chapter_number + "\n")
                file1.write("lang: ta\n")
                file1.write("mainfont: Noto Sans Tamil Regular\n")
                file1.write("---\n\n")
                file1.close()
                continue
            if split_string[0] == "\\v":
                verse_number = split_string[1]
                verse = list_to_string(split_string[2:])
                file1 = open(file_to_edit, "a")
                file1.write("# " + book_name + " " + chapter_number + ":" + verse_number + "\n\n")
                file1.write(verse + "\n\n")
                file1.close()
                continue