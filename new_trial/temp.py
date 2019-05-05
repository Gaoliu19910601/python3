import datetime
from string import Template
import argparse
import time
import os
import glob
import pickle
import re
import logging

start_time = time.clock()

# logging.basicConfig(filename="temp.log",level=logging.INFO,\
#                     format="%(asctime)s:%(lineno)d:%(name)s:%(message)s")

class Account:
    usage_nr = 0

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        Account.usage_nr += 1

    @property
    def email(self):
        return self.name + "@gmail.com"

    @email.setter
    def email(self,newemail):
        newname,rest = newemail.split("@")
        self.name = newname

    @email.deleter
    def email(self):
        print("Name deleted")
        self.name = None

    def type(self):
        return "normal"

    def debit(self,withdrawal):
        self.balance = self.balance - withdrawal

    def credit(self,deposit):
        self.balance = self.balance + deposit

    @classmethod
    def inputmod(cls,input):
        name,balance = input.split("-")
        balance = int(balance)
        return cls(name,balance)

    @staticmethod
    def days_remaining(validity_time):
        return validity_time - datetime.date.today()

    def __add__(self, other):
        return self.balance + other.balance

    def __str__(self):
        print("{} holds an amount of {}$ in his normal account".format(self.name,self.balance))

    def __repr__(self):
        pass


class Privelege(Account):
    def __init__(self,name,balance,interest,withdraw_limit_perday):
        super().__init__(name,balance)
        self.interest = interest
        self.withdraw_limit_perday = withdraw_limit_perday

    def type(self):
        self.type = "Privileged"
        return self.type

    def change_type(self,newtype):
        # newname,rest = newemail.split("@")
        self.type = newtype
        if self.type == "normal":
            self.interest = None
            self.withdraw_limit_perday = None

    def __str__(self):
        print("{} holds an amount of {}$ in his Privileged account".format(self.name,self.balance))

    def __repr__(self):
        pass

    def __dir__(self):
        return []


def Main():

    final_path = 'Complete/hey/now_you_are_annoyed/ok_ok_here_it_is/'

    # os.removedirs(final_path)
    # os.makedirs(final_path)

    pythonpath = '/home/amardeep/PycharmProjects/new_trial/'

    os.chdir(os.path.join(pythonpath,final_path))

    print(os.getcwd())

    # print(os.listdir())

    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--output",help="creates an output file",action="store_true")
    parser.add_argument("-r","--remove",help="remove existing files",action='store_true')
    parser.add_argument("word",help="word search in txt output file")
    parser.add_argument("-rl","--refreshlog",help="refreshes the log",action="store_true")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbose",help="Detailed printing option",action='store_true')
    group.add_argument("-q","--quiet",help="Normal printing",action="store_true")

    args = parser.parse_args()

    if args.refreshlog:
        try:
            os.remove(os.path.join(pythonpath,"temp.log"))
        except FileNotFoundError:
            print("Log does not exist for now!")

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("temp.log")
    # streamHandler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s:%(lineno)d:%(name)s:%(message)s")

    fileHandler.setFormatter(formatter)
    # fileHandler.setLevel(logging.ERROR)

    # streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    # logger.addHandler(streamHandler)

    logger.setLevel(logging.INFO)

    for dirpath, dirfile, fname in os.walk(os.getcwd()):
        logger.info("Current directory: " + str(dirpath))
        logger.info("Current file: " + str(dirfile))
        logger.info("Filename: " + str(fname))

    if args.remove:
        for f in fname:
            os.remove(f)

    input_list = []

    input_list.append(dict(name="Amardeep",balance=100000000,interest=5,withdraw_limit_perday=20000))
    input_list.append(dict(name="Steve", balance=5000000, interest=3, withdraw_limit_perday=100000))
    input_list.append(dict(name="Elon", balance=10000000, interest=1, withdraw_limit_perday=500000))
    input_list.append(dict(name="Vladimir", balance=100000, interest=5, withdraw_limit_perday=50000))
    input_list.append(dict(name="Pope", balance=5000, interest=6, withdraw_limit_perday=10000))

    output_pickle = open("list.pkl","wb")
    pickle.dump(input_list,output_pickle,pickle.HIGHEST_PROTOCOL)
    output_pickle.close()


    t = Template("$name has balance of $balance with an interest rate of $interest % and withdrawal cap per day of $withdraw_limit_perday")

    total = 0

    objectlist = []

    for data in input_list:

        total += data["balance"]
        objectlist.append(Privelege(data["name"],data["balance"],data["interest"],data["withdraw_limit_perday"]))

        if args.quiet:
            logger.info(data)
        elif args.verbose:
            logger.info(t.substitute(data) + "\n")
        else:
            pass
    if args.verbose:
        logger.info("Total balance of all account holders: " + str(total) + "\n")


    # print(objectlist[1].name)

    output_pickle2 = open("allobj.pkl","wb")
    pickle.dump(objectlist,output_pickle2,pickle.HIGHEST_PROTOCOL)
    output_pickle2.close()

    with open("allobj.pkl", 'rb') as inputFile:
        objlistall = pickle.load(inputFile)


    if args.output:

        filename = os.path.join(os.getcwd(), "out.txt")

        if os.path.exists(filename):
            logger.info("File last modified: " + str(datetime.datetime.fromtimestamp(os.stat('out.txt').st_mtime))) # to check the modified time
        else:
            pass


        with open(filename,"w") as f:
            for obj in objectlist:
                f.write("{} holds {} $ in his account with interest {} % and withdraw cap per day of {}\n".format(obj.name,obj.balance,obj.interest,obj.withdraw_limit_perday))

        f.close()

    try:
        filename = os.path.join(os.getcwd(), "out.txt")
        lineNum = 0
        result_trial = []

        with open(filename) as f:
            for line in f.readlines():
                    line = line.strip("\n\r")
                    lineNum += 1

                    searching = re.search(args.word,line,re.M|re.I)

                    if searching:
                        result_trial.append("Line nr. {}: {}\n".format(lineNum,line))
                        logger.info("Line nr. {}:\ {}\n".format(lineNum,line))

        f.close()

    except FileNotFoundError:
        logger.info("File does not exist!")

    logger.info("Total execution time: "+str(time.clock()-start_time)+" secs")
    logger.info("Execution record: "+ str(datetime.datetime.now()))


if __name__ == "__main__":
    Main()



