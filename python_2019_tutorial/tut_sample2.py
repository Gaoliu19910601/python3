import tut_sample1

print("top-level in tut_sample2.py")

tut_sample1.func()

if __name__ == "__main__":
    print("Tut_sample2.py is run directly")
else:
    print("tut_sample2.py is exported to another file")