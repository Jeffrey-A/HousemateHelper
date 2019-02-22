from tkinter import *
from Console_Housemate import *
import tkinter.messagebox


class GUI(HousemateHelper):
    '''This class display the majority of layouts'''
    def __init__(self,win):
        self.win = win  #TK window
        self.frame_1 = Frame(self.win)#Frames
        self.frame_2 = Frame(self.win)
        self.frame_3 = Frame(self.win)
        self.frame_1.grid(row = 0, column = 0)
        self.frame_2.grid(row = 1, column =0,sticky =W,pady=15)

        HousemateHelper.__init__(self) #Constructor of the parent class
        
    def adding_Purchase(self):
        self.status.config(text='Adding Purchases...') #Change status of the status bar
        user = tkinter.messagebox.showinfo("Adding Purshases", "After adding all the purshases click DONE") #Message to the user
        
        #GUI
        self.headtitle = Label(self.frame_2, text = "Adding Purshases")
        self.name = Label(self.frame_2, text = "Name:")
        self.inpname = Entry(self.frame_2)
        self.quantity = Label(self.frame_2, text = "Quantity:")
        self.inpquantity = Entry(self.frame_2)
        self.money = Label(self.frame_2, text = "Money Spent:")
        self.inpmoney = Entry(self.frame_2)

        self.itembought = Label(self.frame_2, text = "What item did you bought:")

        self.add = Button(self.frame_2, text = "ADD PURSHASE")
        self.done = Button(self.frame_2, text = "DONE")

        #Options
        var = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        food = Checkbutton(self.frame_2, text = "Food",variable = var, onvalue =1, offvalue =0)
        toy = Checkbutton(self.frame_2, text = "Toy",variable = var2,onvalue =1, offvalue =0)
        utility = Checkbutton(self.frame_2, text = "Utility",variable = var3,onvalue =1, offvalue =0)

        #Logic   
        self.add.bind('<Button-1>',lambda e: self.getItem_add(var,var2,var3))
        self.done.bind('<Button-1>', lambda e: self.finish())
        
        
        #Place everything in the screen
        self.name.grid(row =1, column = 0,sticky = W)
        self.inpname.grid(row =1, column = 0,padx = 50)
        self.itembought.grid(row =2, column = 0, sticky = W)
        self.headtitle.grid(row = 0, column = 0, sticky = W)   #title r1
        food.grid( row =3, column = 0,sticky = W)  #Food r2
        toy.grid( row =4, column = 0,sticky = W)#Toy r3
        utility.grid( row =5, column = 0,sticky = W)#Utility r4
        self.quantity.grid( row =6, column = 0,sticky = W)
        self.inpquantity.grid(row =6, column = 0,padx = 80)
        self.money.grid( row =7, column = 0,sticky = W)
        self.inpmoney.grid(row =7, column = 0,padx = 80)
        self.add.grid(row =8, column = 0, padx = 4, pady = 6)
        self.done.grid(row= 9,column=0)

    def finish(self):
        '''this method is used for adding_purshases when DONE is clicked'''
        user = tkinter.messagebox.askquestion("Adding Purshases", "Did you add all the desired purshases?")
        if user == 'yes':
            if len(self.people)> 1:
                self.total = self.cal_total()###############
                self.add.grid_remove()
                self.done.grid_remove()
                self.status.config(text='All purshases add...')
            else:
                user = tkinter.messagebox.showinfo("Adding Purshases", "You must add add least two purshases")
                self.adding_Purchase()
                
    def getItem_add(self,v1,v2,v3):
        '''this method is used for adding_purshases when ADD is clicked'''
        if v1.get() == 1:
            item='food'
        elif v2.get() == 1:
            item='toy'
        elif v3.get() == 1:
            item='utility'
        else:
            item='invalid item'
        name = self.inpname.get()
        quantity = self.inpquantity.get()
        cost = self.inpmoney.get()
        if name != '' and quantity.isdigit() and cost.isdigit() and (item =='food' or item == 'toy' or item == 'utility'):
            self.addPurchase(name,item,int(quantity),int(cost))
            self.status.config(text='Purchase added...')
        else:
            user = tkinter.messagebox.showinfo("Adding Purshases", "Something when wrong, plese try again!")
            self.adding_Purchase()
        
    def getting_Inventory(self):
        self.status.config(text='Getting Inventory...')
        self.headtitle = Label(self.frame_2, text = "Getting Inventory")
    
        var = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        
        food = Checkbutton(self.frame_2, text = "Food",variable = var)#Frame
        toy = Checkbutton(self.frame_2, text = "Toy",variable = var2)
        utility = Checkbutton(self.frame_2, text = "Utility",variable = var3)
        self.headtitle.grid(row = 0, column = 0, sticky = W)   #title r1
        food.grid( row =1, column = 0,sticky = W)  #Food r2
        toy.grid( row =2, column = 0,sticky = W)#Toy r3
        utility.grid( row =3, column = 0,sticky = W)#Utility r4
        
        enter = Button(self.frame_2, text = 'GET INFO')
        enter.bind("<Button-1>",lambda e: self.getItem_inv(var,var2,var3))

        
        result = Label(self.frame_2, text = "Result:")
        
        enter.grid( row =4, column = 0,sticky = W)
        result.grid( row =5, column = 0,sticky = W)

    def getItem_inv(self,v1,v2,v3):
        '''this method is used for getting_inventory when GET INFO is clicked'''
        if v1.get() == 1:
            item='food'
        elif v2.get() == 1:
            item='toy'
        elif v3.get() == 1:
            item='utility'
        else:
            item='invalid item'
        t = StringVar()
        t.set(str(self.getInventory(item)) + ' units of '+item+' left.                        ')
        result = Label(self.frame_2, textvariable = t)
        result.grid(row=6,column=0,sticky = W)

    
    def using_Item(self):
        self.status.config(text='Using Items...')
        self.headtitle = Label(self.frame_2, text = "Using Items:")
        

        var = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        
        food = Checkbutton(self.frame_2, text = "Food",variable = var)#Frame
        toy = Checkbutton(self.frame_2, text = "Toy",variable = var2)
        utility = Checkbutton(self.frame_2, text = "Utility",variable = var3)
        self.headtitle.grid(row = 0, column = 0, sticky = W)   #title r1
        food.grid( row =1, column = 0,sticky = W)  #Food r2
        toy.grid( row =2, column = 0,sticky = W)#Toy r3
        utility.grid( row =3, column = 0,sticky = W)#Utility r4
        
        self.itemsquantity = Label(self.frame_2, text = "How many? ")
        self.inputquan = Entry(self.frame_2)
        enter = Button(self.frame_2, text = 'USE IT')

        self.itemsquantity.grid(row = 4, column = 0)
        self.inputquan.grid(row = 4, column = 1)
        enter.grid( row =5, column = 1,sticky = W, pady = 10)

        enter.bind('<Button-1>',lambda e: self.getItem_use(var,var2,var3))

    def getItem_use(self,v1,v2,v3):
        '''this method is used for using_item when USE IT is clicked'''
        
        if v1.get() == 1:
            item='food'
        elif v2.get() == 1:
            item='toy'
        elif v3.get() == 1:
            item='utility'
        else:
            item='invalid item'
        num = self.inputquan.get()
        if num.isdigit() and item in self.inventory:
            self.status.config(text='Item used...')
            self.useItem(item,int(num))
        else:
            user = tkinter.messagebox.showinfo("Warning", "You must choose one option and type an integer value")
            self.using_Item()
    def personValue_checking(self):
        self.status.config(text='Checking who owes money...            total money spent = '+str(self.total_money_spent)+'$')
        head_title = Label(self.frame_2, text = "See Who Owes:")
        self.name = Entry(self.frame_2)
        check = Button(self.frame_2, text = "CHECK")

        if  len(self.people)>0:
            per = Label(self.frame_2,fg= 'red',text= "People in the House:",font=("Helvetica", 10))
            x =0
            for p in self.people:
                Label(self.frame_2,text= p,fg='green').grid(columnspan=5,row=1,column=x,sticky=W)
                x= x+1
            per.grid(columnspan=5,row= 0,column= 0, sticky = W)   
        else:
            Label(self.frame_2,text= 'There are not purshases registered yet',fg='red').grid(columnspan=5,row=1,column=0,sticky=W)
            
        #placing in the screen
        head_title.grid(columnspan=5,row= 3,column= 0, sticky = W,pady=30)
        self.name.grid(columnspan=5,row=3,column =0, padx = 85,sticky = W)
        check.grid(rowspan=5,columnspan=5,row=3,column=0, padx =125,sticky = W,pady=60)

        #binding
        check.bind('<Button-1>',lambda e: self.getValue())

    def getValue(self):
        '''this method is used for personValue_checking when CHECK is clicked'''
        result = Label(self.frame_2, text ='Not info to display.')
        name = self.name.get()
        self.value = 0
        if name !='' and name in self.people:
            self.value =self.personValue(name)
        else:
            result.config(text= 'That person did not spent a penny ')
            self.personValue_checking()
        if self.value < 0:
            result = Label(self.frame_2, text ='Owes '+str(abs(self.personValue(name)))+'                                        ') 
        elif self.value > 0:
            result.config(text= 'Need to get back: '+str(abs(self.personValue(name))) +'                                         ' )
        else:
            result.config(text= 'That person did not spent a penny.')
        result.grid(columnspan=3,row= 6,column=0,sticky=W)
        

    def equalizing(self):
        '''This method equalized all the expenses'''
        user = tkinter.messagebox.askquestion("Equalize", "This action must be perform after adding all the purshases. Did you do so?")
        if user == 'yes':
            self.status.config(text='Expenses Equalized')
            pay = self.equalize()
            place = 0
            if len(self.people) >0 and self.value !=0:
                for i in range(len(pay)):
                    summa = pay[i][0].capitalize() + ' needs to pay '+ pay[i][1].capitalize() +' '+ str(pay[i][2])+'$'
                    result = Label(self.frame_2,text= summa)
                    result.grid(row=place,column=0)
                    place = place + 1
            else:
                result = Label(self.frame_2,text= pay,fg='red')
                result.grid(row=0,column=0)
            user = tkinter.messagebox.showinfo("Reset", "The program must be reseted.")
        

    def reset(self):
        '''This method reset the entire program'''
        self.total_money_spent = 0 #Not money spent yet
        self.inventory = {'food':0,'utility':0,'toy':0}#enventory is empty, there are no items in there
        self.people = {} #Store the people that purchase somthing and how much they spent
        user = tkinter.messagebox.showinfo("Reseted", "The program have been reseted.")
        self.adding_Purchase()
        

    
        
        




class Main(GUI):
    '''This class allows the user to chose the action that they want to perform'''

    def __init__(self,win):
        GUI.__init__(self,win)

    def clear_frame(self,event):
        '''Destroy all the widgets in self.frame_2''' 
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        
    def addPurchase_frame(self):
        add = Button(self.frame_1, text = 'Add Purchase',command =self.adding_Purchase)
        add.bind('<Button-1>',self.clear_frame)
        add.grid( row = 0, column = 0, sticky = NW)
        
    def getInventory_frame(self):
        inve = Button(self.frame_1, text = 'Get Inventory',command =self.getting_Inventory)
        inve.bind('<Button-1>',self.clear_frame)
        inve.grid( row = 0, column = 1, sticky = N)

    def useItem_frame(self):
        use = Button(self.frame_1, text = 'Use Item',command =self.using_Item)
        use.bind('<Button-1>',self.clear_frame)
        use.grid( row = 0, column = 2, sticky = N)

    def who_owes_frame(self):
        owe = Button(self.frame_1, text = 'Who Owes',command =self.personValue_checking)
        owe.bind('<Button-1>',self.clear_frame)
        owe.grid( row = 0, column = 3, sticky = N)

    def equalize_frame(self):
        equa = Button(self.frame_1, text = 'Equalize Expenses',command =self.equalizing)
        equa.bind('<Button-1>',self.clear_frame)
        equa.grid( row = 0, column = 4, sticky = N)

    def reset_frame(self):
        re = Button(self.frame_1, text = 'Reset Program',command =self.reset,width = 15)
        re.bind('<Button-1>',self.clear_frame)
        re.grid( row = 0, column = 5, sticky = N)

    def intro(self):
        user = tkinter.messagebox.showinfo("Instructions", "Recomended sequense of actions: \n First: Add Purshases \n Last: Equalize Expenses")

    def status_bar(self):
        self.status = Label(self.win,text= 'Status:',bd=1, relief=SUNKEN, anchor =W,width = 490)
        self.status.place(x=0,y=330)
    def logo(self):
        logo = PhotoImage(file='logo.png')
        label = Label(self.win, image=logo)
        label.image = logo 
        label.place(x=300,y=90)
         
        
def control():
    '''Control the whole programm'''
    win = Tk()
    win.title("Housemate Helper")
    win.geometry('500x350')
    a = Main(win)
    a.logo()
    a.addPurchase_frame()
    a.getInventory_frame()
    a.useItem_frame()
    a.who_owes_frame()
    a.equalize_frame()
    a.reset_frame()
    a.intro()
    a.status_bar()
    win.mainloop()
    
control()
