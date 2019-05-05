import re
import argparse

def Main():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v','--verbose',action='store_true')
    group.add_argument('-q','--quiet',action='store_true')

    parser.add_argument('word',help = 'the word you want to search')
    parser.add_argument('fname',help = 'the file you want to read')
    parser.add_argument('-o','--output',help='writes the result \
                        to an output file',action='store_true')

    args = parser.parse_args()

    file = open(args.fname)
    lineNum = 0
    result = []

    for line in file.readlines():
        line = line.strip('\n\r')
        lineNum += 1
        searchResult = re.search(args.word,line,re.M|re.I)
        if searchResult:
            if args.verbose:
                result.append(str('\nLine no. ' + str(lineNum) + ': ' + str(line)))
                print('Line no. ' + str(lineNum) + ': ' + str(line))
            elif args.quiet:
                result.append('\n'+str(lineNum))
                print(str(lineNum))
            else:
                result.append('\n'+str(lineNum) + '  ' + str(line))
                print(str(lineNum) + '  ' + str(line))

    if args.output:
        fname2 = open('lookup.txt','a')
        for k in range(len(result)):
            fname2.write(str(result[k]))
        fname2.close


if __name__ == "__main__":
    Main()


