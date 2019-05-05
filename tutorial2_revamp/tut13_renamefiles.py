
import os

print('')

print(os.getcwd())

path = '/home/amardeep/PycharmProjects/tutorial2_revamp/filestorename'

os.chdir(path)

print(os.getcwd())

print('')
# print(os.listdir())

for fname in os.listdir():
    realname, fext = os.path.splitext(fname)

    word1,word2,word3 = realname.split('-')
    word1 = word1.strip()
    word2 = word2.strip()
    word3 = word3.strip()[1:].zfill(2)

    newfname = '{}-{}-{}{}'.format(word3,word2,word1,fext)
    print(newfname)

    os.rename(fname,newfname)