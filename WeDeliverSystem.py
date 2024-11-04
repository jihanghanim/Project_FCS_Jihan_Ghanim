import random
import pandas as pd

#We Deliver System

#main menu 
class Mainmenu:
    def __init__(self):
        self.menu=  int(input('Hello! Please enter:\n' 
                                 + '\n1 To go to the drivers\' menu'
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
        last_key = list(self.drivers.keys())[-1]
        ids= set(self.drivers.keys())
        id_num= int(last_key) +1
        while id_num in ids:
            id_num= +1

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
                return True
            #do not add driver and starting city to dictionary of drivers
            else:
                print('The driver and its starting city is not added.' )
                return False
        #starting city is available        
        else:
            id_num= self.genId()
            #add driver and starting city to dictionary of drivers
            self.drivers[id_num]= {name: start_city}

            print(f'{name}: {start_city} is added.')

            return True
    #add new driver
    def addDriver(self):

        name= input("Enter the driver's name: ").capitalize()
        start_city= input("Enter the driver's start city: ").capitalize()
       
        #if driver name is empty or starting city is empty enter them again
        while not name or not start_city:
            name= input("Enter the driver's name: ").capitalize()
            start_city= input("Enter the driver's start city: ").capitalize()
        #add driver and starting city
        added_driver=self.addCity(start_city, name)

        if added_driver:
            #save added driver to excel file
            # Convert the new drivers dictionary into a list of dictionaries
            new_data = []
            for driver_id, info in self.drivers.items():
                new_data.append({
                    "ID": driver_id,
                    "Name": list(info.keys())[0],  # Extract the name
                    "Location": list(info.values())[0]  # Extract the location
                })

            # Create a new DataFrame from the new data
            new_drivers_df = pd.DataFrame(new_data)
            new_drivers_df.to_csv('drivers_data.csv', index=False)        

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

#build a graph 
class Node:
    def __init__(self,info,n):
        self.info=info
        self.next=n
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def addToHead(self,val): 
        if self.size==0: 
            n=Node(val,None)
            self.head=n
            self.tail=n
            self.size+=1
        else:
            n=Node(val,self.head)
            self.head=n
            self.size+=1

      

class CitiesGraph():
    def __init__(self,V):
        self.V= V
        self.list=[]
        for i in range(V):
            self.list.append(LinkedList())
    #create a graph pf the cities        
    def add_edge(self,n1,n2):
        self.list[n1].addToHead(n2)    
        self.list[n2].addToHead(n1)

    # Function to print a BFS of graph
    def BFS(self, s, dic_graph):

        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create a queue for BFS
        queue = []


        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        neighbors=[]
        while queue:
            # Dequeue a vertex from the queue and print it
            
            s = queue.pop()
            if s in dic_graph:
                #print(dic_graph[s], end=" ")
                neighbors.append(dic_graph[s])

            # Get all adjacent vertices of the dequeued vertex s
            # Manually traverse the linked list
            current = self.list[s].head
            while current is not None:
                if not visited[current.info]:
                    queue.append(current.info)
                    visited[current.info] = True
                current = current.next  # Move to the next node
        return neighbors
            
    #print neighbor cities
    def print_graph(self,dic_graph):
        user_city= input('Enter the city that you want to find its neighboring cities: ')
        city_found=False
        for key in dic_graph:
            if user_city.capitalize()== dic_graph[key]:
                city_found=True
                neighbors=self.BFS(key, dic_graph)
                if len(neighbors[1:])==0:
                    print('No neighboring cities')
                else:
                    print(f'The neighboring cities of {dic_graph[key]}: ', ', '.join(neighbors[1:]))
        if city_found==False:
            print('This city is not included in delivery locations.')

    
    #print drivers delivering to this city
    def deliveringDrivers(self, dic_graph,drivers):
        self.drivers= drivers
        user_city= input('Enter the city to find the drivers delivering to this city: ')
        sim_drivers=[]
        for key in dic_graph:
            if user_city.capitalize()== dic_graph[key]:
                neighbors=self.BFS(key, dic_graph)
                       
                for i in neighbors:
                    for id in self.drivers:
                        for name in self.drivers[id]:
                            if self.drivers[id][name].capitalize()== i.capitalize():
                                sim_drivers.append(name)
                print(', '.join(set(list(sim_drivers))))

        if len(sim_drivers)== 0:
            print('No Drivers delivering to this city.')


#we deliver system
def weDeliver(dic_graph):
    
    #read drivers data and write it in a dictionary

    #drivers= {'1':{'Adam': 'Beirut'}, '2':{'Peter': 'Beirut'}, '3':{'Roy': 'Zahle'}, '4': {'Oliver': 'Jbeil'}}
    drivers= {}
    drivers_data= pd.read_csv('drivers_data.csv')
    for index, row in drivers_data.iterrows():
        drivers[(row['ID'])]={row['Name']: row['Location']}    
    
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
        #go back to main menu                    
        elif dm==4:
            return weDeliver(dic_graph) 
        #error handling
        else:
            print('Please enter a valid choice!')
            return    
    #go to cities' menu
    elif m.menu==2:    
        cm=m.CitiesMenu()
        #show all cities in descending order
        if cm==1:
            Cities(drivers).showCities()
        #search for cities with a given key
        elif cm==2:
            Cities(drivers).searchCities()
        
        #neighboring cities
        elif cm==3:
            #dic_graph= {0:'Akkar', 1: 'Jbeil', 2: 'Beirut', 3: 'Saida', 4: 'Zahle'}
            G=CitiesGraph(len(dic_graph))
            G.add_edge(1,2)
            G.add_edge(1,0)
            G.add_edge(4,3)
            G.print_graph(dic_graph)  
        
        #print drivers delivering to this city
        elif cm==4:
            #dic_graph= {0:'Akkar', 1: 'Jbeil', 2: 'Beirut', 3: 'Saida', 4: 'Zahle'}
            G=CitiesGraph(len(dic_graph))
            G.add_edge(1,2)
            G.add_edge(1,0)
            G.add_edge(4,3)
            G.deliveringDrivers( dic_graph,drivers) 
        #error handling
        else:
            print('Please enter a valid choice!')
        return 
    #exit system
    elif m.menu==3:
        m.exitSys()
    
    #error handling
    else:
        print('Please enter a valid choice!')
        return


#run system
if __name__== "__main__":
    
    #cities map
    dic_graph= {0:'Akkar', 1: 'Jbeil', 2: 'Beirut', 3: 'Saida', 4: 'Zahle'}

    #We dilver system
    weDeliver(dic_graph)

    