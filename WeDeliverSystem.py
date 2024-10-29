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
    
    #go to drivers' menu
    def driversMenu(self):

        driver_choice= int(input('Enter:\n1 To view all the drivers'
                                 + '\n2 To add a driver'
                                 + '\n3 Check similar drivers'
                                 + '\n4 To go back to the main menu\n'))

        return driver_choice

    # go to cities' menu
    def CitiesMenu(self):

        city_choice= int(input('Enter:\n1 Show cities'
                                 + '\n2 Search city'
                                 + '\n3 Print neighboring cities'
                                 + '\n4 Print Drivers delivering to city\n'))

        return city_choice


    

#drivers'menu options
class Driver:

    def __init__(self, drivers):
        
        self.drivers= drivers

    #view all drivers
    def viewDriver(self):
        for id in self.drivers:
            for name in self.drivers[id]:
                print(f'ID{id}, {name}, {self.drivers[id][name]}') 
    
    #generate a random unique id
    def genId(self):
        start= 1
        end=100
        # increase range of random numbers when needed
        while end<= len(self.drivers):
            start +=100
            end +=100

        id_num= random.randint(start, end)
        
        #ensure a unique id is generated
        while id_num in self.drivers:

            id_num= random.randint(start, end)
        return id_num 

    #add the starting city of the driver
    def addCity(self, start_city, name):
        #create a list of all available cities 
        cities=[] 
        for id in self.drivers:
            for n in self.drivers[id]:
                if self.drivers[id][n].capitalize() not in cities:
                    cities.append(self.drivers[id][n].capitalize()) 
        
        #if the starting city is not available, ask user
        if start_city not in cities:
            valid_city= input("This city is invalid. Do you still want to add it? y/n ")

            #add driver and starting city to dictionary of drivers        
            if valid_city== 'y':
                id_num= self.genId()
                self.drivers[id_num]= {name: start_city}
                print(f'{name}: {start_city} is added.')
            #do not add driver and starting city to dictionary of drivers
            else:
                print('The driver and its starting city is not added.' )
        #starting city is available        
        else:
            id_num= self.genId()
            #add driver and starting city to dictionary of drivers
            self.drivers[id_num]= {name: start_city}
            print(f'{name}: {start_city} is added.')


    #add new driver
    def addDriver(self):

        name= input("Enter the driver's name: ").capitalize()
        start_city= input("Enter the driver's start city: ").capitalize()
       
        #if driver name is empty or starting city is empty enter them again
        while not name or not start_city:
            name= input("Enter the driver's name: ").capitalize()
            start_city= input("Enter the driver's start city: ").capitalize()
        #add driver and starting city
        self.addCity(start_city, name)

    #similar drivers
    def similarDrivers(self):
        cities=[] 
        for id in self.drivers:
            for name in self.drivers[id]:
                if self.drivers[id][name].capitalize() not in cities:
                    cities.append(self.drivers[id][name].capitalize())         

        for city in cities:
            sim_drivers=[]
            for id in self.drivers:
                for name in self.drivers[id]:
                    if self.drivers[id][name].capitalize()== city:
                        sim_drivers.append(name)
            print(city + ':',', '.join(sim_drivers)) 

#cities' menu options
class Cities:
    def __init__(self, drivers):
        self.drivers= drivers

    #merge sort
    def merge(self, list1, start,end):
        mid= (start + end)//2

        i= start
        j= mid +1
        temp =[]

        while i<=mid and j <= end:
            if list1[i]> list1[j]:
                temp.append(list1[i])
                i +=1
            else:
                temp.append(list1[j])
                j +=1
        
        while i<=mid:
            temp.append(list1[i])
            i +=1
        while j<=end:
            temp.append(list1[j])
            j +=1                
        
        list1[start:end+1]= temp


    def mergeSort(self,list1, start, end):
        if start==end:
            return list1
        mid = (start + end)//2
        self.mergeSort(list1, start, mid)
        self.mergeSort(list1, mid +1, end)
        self.merge(list1, start,end)
        return list1
    
    #show cities in descending order
    def showCities(self):
        cities=[] 
        for id in self.drivers:
            for name in self.drivers[id]:
                if self.drivers[id][name].capitalize() not in cities:
                    cities.append(self.drivers[id][name].capitalize())        
        start=0
        end= len(cities) -1
        cities= self.mergeSort(cities, start, end)
        print('Cities:', ', '.join(cities))

    #search cities
    def searchCities(self):
        city_key= input('Enter a key and the' 
                        + 'system will output all cities containing this key: ').lower()
        match_cities=[]
        cities=[] 
        for id in self.drivers:
            for name in self.drivers[id]:
                if self.drivers[id][name].lower() not in cities:
                    cities.append(self.drivers[id][name].lower())

        for city in cities:
            if city_key in city:
                match_cities.append(city.capitalize())
        if match_cities:
            print('The matching cities:', ' ,'.join(match_cities))
        else:
            print(f'No cities contain \'{city_key}\'.')
#run system
if __name__== "__main__":
    
    #predefined drivers with starting city
    drivers= {'1':{'Adam': 'Beirut'}, '2':{'Peter': 'Beirut'}, '3':{'Roy': 'Zahle'}}
    #mainmenu 
    m= Mainmenu()
    # go to drivers'menu
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
    
    #go to cities' menu
    if m.menu==2:    
        cm=m.CitiesMenu()
        #show all cities in descending order
        if cm==1:
            Cities(drivers).showCities()
        #search for cities with a given key
        if cm==2:
            Cities(drivers).searchCities()    
    #exit system
    if m.menu==3:
        m.exitSys()