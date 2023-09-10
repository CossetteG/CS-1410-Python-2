class Subway():
  fare = 2.4
  def __init__(self):
    self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
    self.current_stop= "Alewife"
    self.direction = "south"
    self.passengers = 0
    self.total_fares = 0

  def board(self, pasng):
    self.passengers += pasng

  def disembark(self, pasng):
    if pasng > self.passengers:
      pass
      # print("There aren't enough passengers to disembark that many")
    else:
      self.passengers -= pasng

  def advance(self):
    """ advances the subway and switches its direction"""
    curr_index = self.stops.index(self.current_stop)

    if curr_index == len(self.stops)-1:
      self.stops.reverse()
      if self.direction == "south":
        self.direction = "north"
      else:
        self.direction ="south"
    else:
      pass

    curr_index = self.stops.index(self.current_stop)
    new_index = curr_index + 1
    self.current_stop = self.stops[new_index]
    

  def distance(self, des_stop):
    """ calculates how many stops from the current stop to the desired stop"""
    if des_stop in self.stops:

      hypth_stops = self.stops.copy()
      if self.direction == "north":
        hypth_stops.reverse()
      curr_stop = self.current_stop

      if hypth_stops.index(des_stop) == hypth_stops.index(curr_stop):
        #you are at your desired stop
        return 0 
      elif hypth_stops.index(des_stop) > hypth_stops.index(curr_stop):
        #your desired stop is ahead of you
        return hypth_stops.index(des_stop) - hypth_stops.index(curr_stop)
      elif hypth_stops.index(des_stop) < hypth_stops.index(curr_stop):
        #your desired stop is behind you 
        return (len(hypth_stops)-1-hypth_stops.index(curr_stop))*2 + (hypth_stops.index(curr_stop) - hypth_stops.index(des_stop))
    else:
      pass
      # print("That is not a stop on this subway")
  @classmethod
  def change_fare(cls, new_fare):
    """updates the subway fare"""
    cls.fare = new_fare

  def calculate_fares(self):
    """calculates the fares for all passengers currently on board and adds it to the total fares"""
    self.total_fares += self.passengers*self.fare 
    

sooubway = Subway()

sooubway.passengers = 220
sooubway.board(45)
print(sooubway.passengers)

sooubway.passengers = 100
sooubway.calculate_fares()
print(sooubway.total_fares)

sooubway.passengers = 80
sooubway.disembark(90) 
print(sooubway.passengers)

print(sooubway.current_stop, sooubway.direction)
sooubway.advance()
print(sooubway.current_stop, sooubway.direction)

sooubway.current_stop = "Davis"
sooubway.direction = "north"
print(sooubway.current_stop, sooubway.direction)
print(sooubway.distance("Porter"))

sooubway.change_fare(2.75)
print(sooubway.fare)

'''
class Subway():
  fare = 2.4
  def __init__(self):
    self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
    self.current_stop= "Alewife"
    self.direction = "south"
    self.passengers = 0
    self.total_fares = 0

  def board(self, pasng):
    self.passengers += pasng
    self.calculate_fares(pasng, mode="per_board")

  def disembark(self, pasng):
    if pasng > self.passengers:
      self.passengers = 0
      # print("There aren't enough passengers to disembark that many")
    else:
      self.passengers -= pasng

  '''
'''
  #my code is better than yours becuase I didn't hard code in the stop names but codio f#ckin hates me so 
  def advance(self):
    """ advances the subway and switches its direction"""
    curr_index = self.stops.index(self.current_stop)

    if curr_index == len(self.stops)-1:
      self.stops.reverse()
      if self.direction == "south":
        self.direction = "north"
      else:
        self.direction ="south"
    else:
      pass

    curr_index = self.stops.index(self.current_stop)
    new_index = curr_index + 1
    self.current_stop = self.stops[new_index]
    
  #again I like my code better becuase it accounts for the direction that the subway is travelling in 
  def distance(self, des_stop):
    """ calculates how many stops from the current stop to the desired stop"""
    if des_stop in self.stops:
      hypth_stops = self.stops.copy()
      if self.direction == "north":
        hypth_stops.reverse()
      curr_stop = self.current_stop

      if hypth_stops.index(des_stop) == hypth_stops.index(curr_stop):
        #you are at your desired stop
        return 0 
      elif hypth_stops.index(des_stop) > hypth_stops.index(curr_stop):
        #your desired stop is ahead of you
        return hypth_stops.index(des_stop) - hypth_stops.index(curr_stop)
      elif hypth_stops.index(des_stop) < hypth_stops.index(curr_stop):
        #your desired stop is behind you 
        return (len(hypth_stops)-1-hypth_stops.index(curr_stop))*2 + (hypth_stops.index(curr_stop) - hypth_stops.index(des_stop))
    else:
      pass
      # print("That is not a stop on this subway")
'''
'''
  def advance(self):
    """Advances the subway to the next stop"""
    current_index = self.stops.index(self.current_stop)
    if self.direction == "south":
      if self.current_stop == "Kendall":
        self.current_stop = "Central"
        self.direction = "north"
      else:
        self.current_stop = self.stops[current_index + 1]
    else:
      if self.current_stop == "Alewife":
        self.current_stop = "Davis"
        self.direction = "south"
      else:
        self.current_stop = self.stops[current_index - 1]

  def distance(self, desired_stop):
    """Returns the number of stops between the
    current location and the desired stop"""
    current_index = self.stops.index(self.current_stop)
    desired_index = self.stops.index(desired_stop)
    return abs(current_index - desired_index)

  @classmethod
  def change_fare(cls, new_fare):
    """updates the subway fare"""
    Subway.fare = new_fare

  def calculate_fares(self, pasng=0, mode="toll"):
    """calculates the fares for all passengers currently on board and adds it to the total fares"""
    if mode == "toll":
      self.total_fares += self.passengers*self.fare 
    else: 
      self.total_fares += self.fare*pasng
    

sooubway = Subway()

sooubway.passengers = 220
sooubway.board(45)
# print(sooubway.passengers)

sooubway.passengers = 100
sooubway.calculate_fares()
# print(sooubway.total_fares)

sooubway.passengers = 80
# sooubway.disembark(90) 
# print(sooubway.passengers)

# print(sooubway.current_stop, sooubway.direction)
# sooubway.advance()
# print(sooubway.current_stop, sooubway.direction)

sooubway.current_stop = "Davis"
sooubway.direction = "north"
# print(sooubway.current_stop, sooubway.direction)
# print(sooubway.distance("Porter"))

sooubway.change_fare(2.75)
# print(sooubway.fare)
'''