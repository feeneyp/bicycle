from bicycle import Bicycle, Frame, Wheel, Shop, Customer

def main():
  bikesRUS = Shop()
  #print bikesRUS.bikes
  bikesRUS.stock_frames_wheels()
  #print bikesRUS.bikes
  print "this is the inventory {}\n".format(bikesRUS.inventory)
  customers = [Customer(200), Customer(500), Customer(1000)] #create three customers ad-hoc
  i = 1  #start of code to loop over customers
  for customer in customers:
    bikesRUS.customer_list.append(customer)
    customer.name = "customer"+str(i)
    i = i+1  
  print bikesRUS.customer_list 
  customers[0].purchase_bike(bikesRUS,"Kiddy","carbon") #needs comment
  customers[1].purchase_bike(bikesRUS,"Roadie","alu") #needs comment
  customers[2].purchase_bike(bikesRUS,"Speedster","alu") #needs comment
  for customer in bikesRUS.customer_list:
    print "Bikes owned by {}: {}".format(customer.name,customer.bikes_owned)
    print "Budget left over for {}: {}\n".format(customer.name,customer.money_left)
  print "this is the inventory after three customers purchased: {}\n".format(bikesRUS.inventory)


if __name__ == "__main__":
  import random  #is this where I would put this??
  main()