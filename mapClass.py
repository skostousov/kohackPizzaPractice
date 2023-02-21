class mapping:
    def __init__(self,address,tracker):
        self.adress = address
        self.tracker = tracker

    def mapRoute(self,tracker,address):
        route1 = []
        route2 = []
        route3 = []
        #the function will fill these lists with all of the street names in the 3 fastest routes if there are 3 routes otherwise leave some of the lists empty
        
        #insert google maps code to get the routes
        
        #put the a list of the routes into db
        con = sqlite3.connect("orders.db")
        cur = con.cursor()
        
        cur.execute("UPDATE orders SET route = ? WHERE tracking IS ?;",([route1,route2,route3],tracker))
        con.commit()
        cur.close()
