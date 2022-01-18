import glob
for file in glob.glob("/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/usfm/*"):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            split_string = line.split()
            if split_string[0] == "\p":
                print("True")
                continue
            if split_string[0] == "\id":
                print("hoo haa")
