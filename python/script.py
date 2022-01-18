import glob
import os

path = "/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/"

def list_to_string(s): 
    str1 = " "  
    return (str1.join(s))

for file in glob.glob("/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/usfm/*"):
    with open(file, 'r') as f:
        book_name = ""
        chapter_number = 0
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            split_string = line.split()
            if split_string[0] == "\id":
                try:
                    os.makedirs(path + "md/" + split_string[1])
                except:
                    pass
                continue
            if split_string[0] == "\mt":
                book_name = list_to_string(split_string[1:])
                print(book_name)
                continue
            if split_string[0] == "\p":
                continue
            if split_string[0] == "\c":
                continue
            if split_string[0] == "\\v":
                continue