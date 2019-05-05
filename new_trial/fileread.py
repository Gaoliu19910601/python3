
with open("fileread.txt",'r') as f:
    f_contents = f.read(50)
    # f_contents2 = f.readlines()
    # print(f_contents)
    print(f_contents)

    f.seek(10)

    print(f.read(500))


with open("testfile.txt",'w') as wf:
    wf.write("1. wow wow wow yippie yo yipiie ye\n")
    wf.write("2. wow wow wow yubba yubba yubbaa\n")
    wf.write("3. snoop doggy dogg\n")
    wf.write("4. dr.drake and its all a big load of shit")

with open("testfile.txt",'r') as rf:
    with open("testwrite.txt",'w') as ww:
        for line in rf:
            ww.write(line)

with open("space1.jpg",'rb') as rf:
    with open("testpic.jpg",'wb') as ww:
        chunksize = 1350
        ww.write(rf.read(1350))