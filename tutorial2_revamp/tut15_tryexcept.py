
# try:
#     f = open('test2.txt')
#     var = badvar
# except FileNotFoundError:
#     print('File not found !')
# except Exception:
#     print('Sorry shit happens!')
# else:
#     print(f.read())
#     f.close()


try:
    f2 = open('test3.txt')
    print(f2.name)
    if f2.name == 'test3.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f2.read())
    f2.close()
finally:
    print('Executing Finally...')
