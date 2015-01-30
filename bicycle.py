class Bicycle(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost
    
class Shop(object):
  def __init__(self):
    self.bikes = {"Speedster":[25,100,11],"Mountainous":[25,200,12],"SuperBMX":[25,300,13],"Kiddy":[25,400,14],"Roadie":[25,500,15],"City":[25,600,16]}
    self.inventory = {}
    #bikes is a dict that stores data for model, weight, cost, and number available bikes
    #inventory is a dict that the shop will use to list just the model of the bike and the number of them in stock
    self.customer_list = [] #customer_list is a list of customer objects
    
  def stock_bikes (self):  #replaces the values of the items in the inventory with Bicycle objects
    for k,v in self.bikes.iteritems():
      self.bikes[k] = Bicycle(k,v[0],v[1]) #bikes dict items are now Bicycle objects with model, weight, cost
      self.inventory[k] = v[2] #this populates the inventory dict which was an empty dict created in _init_
  
  def bikes_in_budget (self,budget): #the shop object has a fct that returns a dict list of bike objects
    bikes_in_budget = {}
    for bike in self.bikes.itervalues():
        if bike.cost * 1.2 <= budget:
          bikes_in_budget[bike.model] = bike
    return bikes_in_budget
      
    
class Customer(object):
  def __init__(self, budget):
    self.name = ""
    self.budget = budget
    self.bikes_owned = []
    self.money_left = budget
  
  def purchase_bike(self, bicycle): #pass in a bicycle object
    self.bikes_owned.append(bicycle.model)
    self.money_left = self.budget - (bicycle.cost * 1.2)
 
def main():
  bikesRUS = Shop()
  #print bikesRUS.bikes
  bikesRUS.stock_bikes()
  #print bikesRUS.bikes
  print "this is the inventory {}\n".format(bikesRUS.inventory)
  customers = [Customer(200), Customer(500), Customer(1000)]
  i = 1
  for customer in customers:
    bikesRUS.customer_list.append(customer)
    customer.name = "customer"+str(i)
    i = i+1  
  #print bikesRUS.customer_list 
  for customer in bikesRUS.customer_list:
    print "{} can afford: ".format(customer.name)
    print "{}\n".format(bikesRUS.bikes_in_budget(customer.budget).keys())
    bike_chosen = bikesRUS.bikes_in_budget(customer.budget).items()[0][1] #items() returns a list of items i.e. unordered list of k,v tuples and call to value() is necessary because you want the object part - k is the model name and v is a Bicycle object
    customer.purchase_bike(bike_chosen) #needs comment
  for customer in bikesRUS.customer_list:
    print "Bikes owned by {}: {}".format(customer.name,customer.bikes_owned)
    print "Budget left over for {}: {}\n".format(customer.name,customer.money_left)
    

if __name__ == "__main__":
  import random  #is this where I would put this??
  main()