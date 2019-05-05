import re

def Main():

   line = "I think I got it"
   line2 = "think I am not"

   matchResult = re.match('think', line2, re.M|re.I)

   if matchResult:
         print('Match found ' + matchResult.group())
   else:
         print("Match not found")

   searchResult = re.search('think', line, re.M|re.I)

   if searchResult:
         print('search found ' + searchResult.group())
   else:
         print('nothing found')


if __name__ == "__main__":
    Main()



