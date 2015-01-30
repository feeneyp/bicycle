from bicycle import Bicycle, Shop, Customer

def main():
  bikesRUS = Shop()
  #print bikesRUS.bikes
  bikesRUS.stock_bikes()
  #print bikesRUS.bikes
  print "this is the inventory {}\n".format(bikesRUS.inventory)
  customers = [Customer(200), Customer(500), Customer(1000)] #create three customers ad-hoc
  i = 1  #start of code to loop over customers
  for customer in customers:
    bikesRUS.customer_list.append(customer)
    customer.name = "customer"+str(i)
    i = i+1  
  #print bikesRUS.customer_list 
  for customer in bikesRUS.customer_list:
    print "{} can afford: ".format(customer.name)
    print "{}\n".format(bikesRUS.bikes_in_budget(customer.budget).keys())
    bike_chosen = bikesRUS.bikes_in_budget(customer.budget).items()[0][1] #items() returns a list of items i.e. unordered list of k,v tuples and call to value() is necessary because you want the object part - k is the model name and v is a Bicycle object
    customer.purchase_bike(bikesRUS,bike_chosen) #needs comment
  for customer in bikesRUS.customer_list:
    print "Bikes owned by {}: {}".format(customer.name,customer.bikes_owned)
    print "Budget left over for {}: {}\n".format(customer.name,customer.money_left)
  print "this is the inventory after three customers purchased: {}\n".format(bikesRUS.inventory) 

if __name__ == "__main__":
  import random  #is this where I would put this??
  main()