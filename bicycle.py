class Bicycle(object):
  def __init__(self, frame_model, wheel_type): #frame models are 'City', 'Mountainous', 'Speedster', 'Kiddy', 'SuperBMX', 'Roadie'
    self.frame_model = frame_model
    self.wheel_type = wheel_type
    
class Frame(object):
  def __init__(self, model="m", weight="w", cost="c"): #frame models are 'City', 'Mountainous', 'Speedster', 'Kiddy', 'SuperBMX', 'Roadie'
    self.model = model
    self.weight = weight
    self.cost = cost
    
class Wheel(object):
  def __init__(self, material, weight, cost): #wheel materials are alu, carbon, steel
    self.material = material
    self.weight = weight
    self.cost = cost   
    
class Shop(object):
  def __init__(self):
    self.frames = {
      "Speedster":{"weight":25, "cost":100, "stock":11},
      "Mountainous":{"weight":25, "cost":200, "stock":12},
      "SuperBMX":{"weight":25, "cost":300, "stock":13},
      "Kiddy":{"weight":25, "cost":400, "stock":14},
      "Roadie":{"weight":25, "cost":500, "stock":15},
      "City":{"weight":25, "cost":600, "stock":16}
    }
    #frames and wheels are dictionaries that stores data for model, weight, cost, and number available bikes
    self.wheels = {
      "alu":{"weight":25, "cost":100, "stock":11},
      "carbon":{"weight":25, "cost":200, "stock":12},
      "steel":{"weight":25, "cost":300, "stock":13}
    }
    #inventory is a dictionary of dictionaries that the shop will use to list 
    #just the model or name of the item and the number of them in stock
    self.inventory = {"frames":{},"wheels":{}}
    #customer_list is a list of customer objects
    self.customer_list = []
    
    
  def stock_frames_wheels (self):
    #replaces the weight/cost info with Frame objects objects 
    #and creates inventory dict with only stock info
    for frame_name,v in self.frames.iteritems(): 
      self.frames[frame_name] = Frame(model=frame_name, weight=v["weight"], cost=v["cost"]) 
      self.inventory["frames"][frame_name] = v["stock"]
    #replaces the weight/cost info with Frame Wheel objects 
    #and creates inventory dict with only stock info
    for k,v in self.wheels.iteritems():
      self.wheels[k] = Wheel(frame_name,v["weight"],v["cost"])
      self.inventory["wheels"][k] = v["stock"]   
    
    
  def calc_cost_bike (self, frame_model, wheel_type):
    cost = self.wheels[wheel_type].cost*2 + self.frames[frame_model].cost
    return cost
  
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
  
  def purchase_bike(self, shop, frame_model, wheel_type): #pass in a shop object and strings for frame and wheel type
    self.bikes_owned.append(Bicycle(frame_model,wheel_type))
    self.money_left = self.budget - (shop.calc_cost_bike(frame_model, wheel_type) * 1.2)
    shop.inventory["frames"][frame_model] -= 1
    shop.inventory["wheels"][wheel_type] -= 1

    
