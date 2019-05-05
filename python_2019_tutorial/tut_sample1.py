def func():
    print("func() is in tut_sample1.py")

print("top-level in tut_sample1.py")

if __name__ == "__main__" :
    print('tut_sample1.py is run directly')
else:
    print('tut_sample1.py is exported to another file')