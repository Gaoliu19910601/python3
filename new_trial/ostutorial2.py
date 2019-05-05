import os

fpath = os.chdir("/home/amardeep/PycharmProjects/new_trial/os_tutorial2/")

os.getcwd()

for files in os.listdir(fpath):
    print(files)
    fname, fext = os.path.splitext(files)
    print(fname)
    print(fext)
    first,second,third = fname.split("-")
    # print(first)
    first = first.strip()     # done in order to correct the spaces
    second = second.strip()   # done in order to correct the spaces
    third = third.strip()     # done in order to correct the spaces
    fext = fext.strip()
    print(fext)
    newname = "{}{}-{}{}".\
          format(third,first,second)
    os.rename(files,newname)






