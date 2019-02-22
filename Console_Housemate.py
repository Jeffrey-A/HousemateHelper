

class HousemateHelper:
    '''This is the top level class that control the entire program.
        it uses the classes Person, Item and UserInterface.'''
    def __init__(self):
        self.total_money_spent = 0 #Not money spent yet
        self.inventory = {'food':0,'utility':0,'toy':0}#enventory is empty, there are no items in there
        self.people = {} #Store the people that purchase somthing and how much they spent
        
    def addPurchase(self,person,item_string,quantity,cost): 
        '''It saves data: name of the person, the item he bought,
            the quantity of that item and the total money he spent.'''
        self.person = Person(person,cost) #Using the Person class
        self.people[self.person.getName()] = self.person.getMoneyspent()#add this info to self.people   
        self.item = Item(item_string,quantity) #Using the Item class
        if item_string in self.inventory:
            self.inventory[item_string] = self.inventory[item_string] + self.item.getQuantity()#add this info to self.inventory
        
        
    def getInventory(self,item_string):
        '''it takes an item-string: food,utility or toy as input and return the current amount of that item.'''
        if item_string in self.inventory: 
            for key in self.inventory:
                if item_string == key:
                    if self.inventory[key] >= 0:
                        return self.inventory[key]
                    return 0
            
    
    def useItem(self,item_string,num): 
        '''it takes an item-string: food, utility or toy and integer num as input,
            then it removes num of that item from the inventory.'''
        if item_string in self.inventory:
            for key in self.inventory:
                if item_string == key:
                    self.inventory[key] = self.inventory[key] - num #remove num of a item from the inventory
        else:
            return 'Item no available'  
    
    def personValue(self,name):
        '''it takes an string as input indicating the name of a person that has purchased something,
            and it returns how much that person needs to pay'''
        ################################################
        #Please run this method after running 'cal_total'
        #################################################
        if len(self.people)>0:
            self.each = self.total_money_spent/ len(self.people) #each person should pay this  
        if name in self.people:
            for key in self.people:
                if name == key:
                    if self.people[key] < self.each: #If that person paid less than what he should pay
                        self.need_to_pay =  self.people[key] - self.each 
                        return self.need_to_pay #Then he need to pay this
                    else:
                        return  self.people[key] - self.each  #Needs to receive this money back
        else:
            return 'That person does not live in the house or did not spent anything.'
                  
    def equalize(self): #working perfect with nice number. only gives an approximation when decimal numbers
        '''It makes sure that all the housemates spent the same amount of money.
            It also identify who need to pay to who and how much.
            It returns a list of tuples, where each tuple is of the form (A, B, x),
            where A and B are person names, and x is an
            amount of money that A should pay to B.'''
        ################################################
        #Please run this method after running 'cal_total'. The equalize must be run only once.
        #################################################
        scheme = []
        for person in self.people:
            for name in self.people:
                if person != name:
                    need_to_pay = 0
                    if self.personValue(person) < 0 and self.personValue(name) > 0:
                        for i in range(abs(round(self.personValue(person)))):
                            need_to_pay = need_to_pay + 1
                            if need_to_pay == round(self.personValue(name)) or need_to_pay == abs(round(self.personValue(person))) :
                                break
                        scheme.append((person,name,round(need_to_pay,2)))
                    self.people[person] = self.people[person] + need_to_pay
                    self.people[name] = self.people[name] - need_to_pay
        if len(scheme) == 0:
            return 'There are not expenses to equalize'
        else:
            return scheme

           
    def cal_total(self):#working well
        '''This method calculates the total money spent'''
        ################################################
        #This method must be run once only. After adding the 'purchase' with the addPurchase method.
        #After that, the equaize and personValue methods will work fine.
        #################################################
        for key in self.people:
            self.total_money_spent = self.total_money_spent + self.people[key]
        return self.total_money_spent
    
    def eachPay(self):
        '''It returns the amoung of money that each person should pay'''
        return self.total_money_spent/ len(self.people)
        
class Person:
    '''This class saves the person's name and the money they spent'''
    def __init__(self, name, money_spent):
        self.name = name
        self.money_spent = money_spent
        
    def getName(self):
        '''It returns the name of the person'''
        return self.name
    
    def getMoneyspent(self):
        '''It returns the money spent'''
        return self.money_spent


class Item:
    '''This class keeps track of the inventory'''

    def __init__(self, item, num ):
        self.item = item
        self.quantity = num

    def getItem(self):
        '''it returns the item'''
        return self.item
    
    def getQuantity(self):
        '''it return the quantity of a specified item'''
        return self.quantity
    






