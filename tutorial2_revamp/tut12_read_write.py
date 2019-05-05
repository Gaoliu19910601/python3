
# Open and Read only operation
with open('pip_guideline.txt', 'r') as f:
    # for line in f:
    #     print(line, end='')
    f_contents = f.read()
    print(f.tell()) # prints the last length of that read
    # f_contents = f.readlines()
    print(f_contents)

# Open and Write only operation
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

# Reading a file and writing its contents in another file
with open('pip_guideline.txt', 'r') as rf:
    with open('test3.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Reading an image and writing it to another picture as a copy
with open('tut12.png',  'rb') as rg:
    with open('test12_copy.png',  'wb') as wg:
        for line in rg:
            wg.write(line)

# Reading an image and writing it to another picture in chunks
with open('tut12.png',  'rb') as rg2:
    with open('test12_copy2.png',  'wb') as wg2:
        chunk_size = 80000
        contents = rg2.read(chunk_size)
        wg2.write(contents)

# Reading an image and writing it to another picture in chunks
with open('tut12.png',  'rb') as rg2:
    with open('test12_copy3.png',  'wb') as wg2:
        chunk_size = 80000
        contents = rg2.read(chunk_size)
        while len(contents) > 0:
            wg2.write(contents)
            contents = rg2.read(chunk_size)
