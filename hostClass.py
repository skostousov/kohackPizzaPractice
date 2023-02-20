import sqlite3
class host:
    def __init__(self,orderlist):
        order = list(orderlist.values())
        self.order = order
        #order is a list containing [name,address,phone number, toppings, slices, tracking number] 
        self.name = self.order[0]
        self.address = self.order[1]
        self.phone = self.order[2]
        self.topping = self.order[3]
        self.slices = self.order[4]
        self.tracking = self.order[5]
    #takes in list values and puts them into db    
    def commitToDB(self):
        con = sqlite3.connect("orders.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS orders(name,address,phone,topping,slices,tracking NOT NULL PRIMARY KEY,route)")
        cur.execute("INSERT INTO orders (name,address,phone,topping,slices,tracking) values (?,?,?,?,?,?);",self.name,self.address,self.phone,self.topping,self.slices,self.tracking)
        con.commit()
        cur.close()
    
    def mapRoute(self):
        route1 = []
        route2 = []
        route3 = []
        #the function will fill these lists with all of the street names in the 3 fastest routes if there are 3 routes otherwise leave some of the lists empty
        
        #insert google maps code to get the routes
        
        #put the a list of the routes into db
        con = sqlite3.connect("orders.db")
        cur = con.cursor()
        
        cur.execute("INSERT INTO orders (route) VALUES (?);",[route1,route2,route3])
        con.commit()
        cur.close()
    def chooseOrders(self):
        #this will take the route
        con = sqlite3.connect("orders.db")
        cur = con.cursor()
        cur.execute("SELECT FROM orders (tracking,slices,route) VALUES WHERE topping IS 'cheese'")
        
        routes=cur.fetchall()
        #check for common roads
        common_routes = {}
        for route in routes:
            #keep track of how many adsresses go through a certain road
            for i in route:
                if i in common_routes.keys():
                    common_routes[i].append([route[0],route[1]]) 
                else:
                    common_routes[i] = [[route[0],route[1]]]
        
        common_streets = {}
        #check dictionary for most used roads and make groups each group will be a list in common routes
        for info in common_routes:
            total_slices = 0
            ids = []
            for i in info:
                total_slices += i[1]
                ids.append(i[0])
            common_streets[info] = [total_slices,ids]
            
            
            
                    
            
            
  
