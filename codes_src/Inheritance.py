#example for all types of inheritance(self,multiple,multilevel,heirarchical)
class Basic_info: #Parent class 1
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def printinfo(self):
        print("Car brand and model is",self.brand,self.model)
        print("price is",self.price)
class instock: #Parent class 2
    def __init__(self,avail,shipment):
        self.avail=avail
        self.shipment=shipment        
# example for multiple inheritance --> inheriting more than one parent classes          
class Cars(Basic_info,instock): #inheriting Basic_info class,instock class
    def __init__(self,brand,model,price,avail,shipment): #declaring child class its own init
        Basic_info.__init__(self,brand,model,price)  #inheriting Basic_info attributes
        instock.__init__(self,avail,shipment)  #inheriting instock attributes
    def printCinfo(self):
        print("Car brand and model is",self.brand,self.model)
        print("price is",self.price)    
        print(self.avail)
        print(self.shipment)
#example for multilevel inheritance --> inheriting child class as parent     
class infotainment(Cars): 
    def __init__(self,brand,model,price,spclfeatures,warranty,rating,avail,shipment):
        Basic_info.__init__(self,brand,model,price)
        instock.__init__(self,avail,shipment)
        self.spclfea=spclfeatures #intializing additional required attributes
        self.warrn=warranty
        self.rating=rating
    def printinfo_of_inoftainment(self):
        print("Accessory brand and model is:",self.brand,self.model)
        print("Price:",self.price)
        print("warranty period:",self.warrn)
        print("Rating:",self.rating)
        print(self.brand,self.model,"is special for",self.spclfea)
        print(self.avail,"-",self.shipment)

# example for single inheritance --> inheriting a single parent class       
# example for heirarchical inheritance --> inheriting same parent class more than once        
class paints(Basic_info): 
    def __init__(self,brand,model,price,composition,nature):
        Basic_info.__init__(self,brand,model,price)
        self.compo=composition #intializing additional required attributes
        self.nature=nature
    def printpaint(self):
        print("Paint manufacturer and model is:",self.brand,self.model)
        print("Price:",self.price)
        print("Chemical Composition:",self.compo)
        print("Evnironmental harmfulness lvl:",self.nature)

car1=Cars("Ford","GT-06","$45,0000","not available","expected to arrive soon") #obj-1
car2=Cars("Ferrari","MX-330","$67,000","Available","Ready to ship in 3 days") #obj-2
car1.printCinfo()
print("\n")
car2.printCinfo()
Zebronics=infotainment("Zebronics","Zeb-Thunder","$25","50W output with dual stereo speaker","5 years","5 star","available","ships in 3 days") #obj-3
Bose=infotainment("Bose","BV-420","$50","80W bt portable speaker","10 years","4.7 star","out of stock","no units available for shipment") #obj-4
print("\n")
Zebronics.printinfo_of_inoftainment()
print("\n")
Bose.printinfo_of_inoftainment()
paintbrand1=paints("SherinWilliams","Red_BX-550","$600/litre","Al2O3-2H2O+Na2B4O7-10H2O","medium") #obj-5
paintbrand2=paints("PPG_INDUSTRIES","BlueWhite_GTX1650","$400/litre","FeSO4-7H2O+2PbO-PbO2","low") #obj-6
print("\n")
paintbrand1.printpaint()
print("\n")
paintbrand2.printpaint()
