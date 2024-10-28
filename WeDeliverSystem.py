#We Deliver System

#main menu 
class Mainmenu:
    def __init__(self):
        self.menu=  int(input('Enter:\n1 To go to the drivers\' menu'
                                 + '\n2 To go to the cities\' menu'
                                 + '\n3 To exit the system\n'
                                 ))

    #exit system
    def exitSys(self):
        return
    
    #drivers' menu
    def driversMenu(self):

        self.driver_choice= int(input('Enter:\n1 To view all the drivers'
                                 + '\n2 To add a driver'
                                 + '\n3 Check similar drivers'
                                 + '\n4 To go back to the main menu\n'))

        return self.driver_choice

#run system
if __name__== "__main__":
    
    #predefined drivers with starting city
    drivers= {'1':{'Adam': 'Beirut'}}
    #mainmenu 
    m= Mainmenu()
    #drivers'menu
    if m.menu==1:
        dm=m.driversMenu()
    #exit system
    if m.menu==3:
        m.exitSys()