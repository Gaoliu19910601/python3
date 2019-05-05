

class Player:
    def __init__(self,ID,name,price,items):
        self.ID = ID
        self.name = name
        self.price = price
        self.items = items

    def __str__(self):
        return "My ID:" +str(self.ID)+"\nMy name:"+\
               str(self.name)+"\nMy price: "+str(self.price)+\
               "\nMy Items: "+str(self.items)


class Player2:
    def __init__(self,ID2,name2,price2,items2):
        self.ID2 = ID2
        self.name2 = name2
        self.price2 = price2
        self.items2 = items2

    def __str__(self):
        return "My ID:" +str(self.ID2)+"\nMy name:"+\
               str(self.name2)+"\nMy price: "+str(self.price2)+\
               "\nMy Items: "+str(self.items2)