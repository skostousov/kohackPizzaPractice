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
        cur.execute("CREATE TABLE IF NOT EXISTS orders(name,address,phone,topping,slices,tracking NOT NULL PRIMARY KEY)")
        cur.execute("INSERT INTO orders values (?,?,?,?,?,?)",self.name,self.address,self.phone,self.topping,self.slices,self.tracking)
        con.commit()
        cur.close()
        
  

  
