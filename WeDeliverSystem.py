import random

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

#drivers'menu options
class Driver:

    def __init__(self, drivers):
        
        self.drivers= drivers

    #view all drivers
    def viewDriver(self):
        for id in self.drivers:
            for name in self.drivers[id]:
                print('ID'+id, name,self.drivers[id][name]) 
    
    #add new driver
    def addDriver(self):

        self.name= input("Enter the driver's name: ").capitalize()
        self.start_city= input("Enter the driver's start city: ").capitalize()
        print(self.start_city)
        #if driver name is empty or starting city is empty enter them again
        while not self.name or not self.start_city:
            self.name= input("Enter the driver's name: ").capitalize()
            self.start_city= input("Enter the driver's start city: ").capitalize()
        
        #generate a random unique id
        def genId(self):
            self.start= 1
            self.end=100
            # increase range of random numbers when needed
            while self.end<= len(self.drivers):
                self.start +=100
                self.end +=100

            id_num= random.randint(self.start, self.end)
            
            #ensure a unique id is generated
            while id_num in self.drivers:

                id_num= random.randint(self.start, self.end)
            return id_num        
        
        #add the starting city of the driver
        def addCity(self):
            #create a list of all available cities 
            self.cities=[] 
            for id in self.drivers:
                for name in self.drivers[id]:
                    if self.drivers[id][name].capitalize() not in self.cities:
                        self.cities.append(self.drivers[id][name].capitalize()) 
            
            #if the starting city is not available, ask user
            if self.start_city not in self.cities:
                self.valid_city= input("This city is invalid. Do you still want to add it? y/n ")

                #add driver and starting city to dictionary of drivers        
                if self.valid_city== 'y':
                    id_num= genId(self)
                    self.drivers[id_num]= {self.name: self.start_city}
                    print(f'{self.name}: {self.start_city} is added.')
                #do not add driver and starting city to dictionary of drivers
                else:
                    print('The driver and its starting city is not added.' )
            #starting city is available        
            else:
                id_num= genId(self)
                #add driver and starting city to dictionary of drivers
                self.drivers[id_num]= {self.name: self.start_city}
                print(f'{self.name}: {self.start_city} is added.')

        addCity(self)

    #similar drivers
    def similarDrivers(self):
        self.cities=[] 
        for id in self.drivers:
            for name in self.drivers[id]:
                if self.drivers[id][name].capitalize() not in self.cities:
                    self.cities.append(self.drivers[id][name].capitalize())         

        for city in self.cities:
            self.sim_drivers=[]
            for id in self.drivers:
                for name in self.drivers[id]:
                    if self.drivers[id][name].capitalize()== city:
                        self.sim_drivers.append(name)
            print(city + ':',', '.join(self.sim_drivers)) 

#run system
if __name__== "__main__":
    
    #predefined drivers with starting city
    drivers= {'1':{'Adam': 'Beirut'}, '2':{'Peter': 'Beirut'}, '3':{'Roy': 'Zahle'}}
    #mainmenu 
    m= Mainmenu()
    #drivers'menu
    if m.menu==1:
        dm=m.driversMenu()
        drive= Driver(drivers)
        #view all drivers
        if dm==1:
            drive.viewDriver()
        #add a driver
        elif dm==2:
            drive.addDriver()
        #similar drivers
        elif dm==3:
            drive.similarDrivers()                    
    #exit system
    if m.menu==3:
        m.exitSys()