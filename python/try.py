import glob
for file in glob.glob("/home/berinaniesh/Development/Bible-Tamil-Sathiyavedam-1957/usfm/*"):
    with open(file, 'r') as f:
        f_contents = f.read()
        print(f_contents)
        