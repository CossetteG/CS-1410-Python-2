from typing import Protocol, List, Union, runtime_checkable

@runtime_checkable
class Combinable(Protocol):

  @property
  def can_combine(self, other: "Combinable"):
    pass
  
  @property
  def combine(self, other: "Combinable") -> "Combinable":
    pass

'''
#yeah so dont use. any of this. its fine. 
    if isinstance(item) == Candy():
      if (item.name, item.price_per_pound) in self.candy_cache;
        return True
      else:
        self.candy_cache.append((item.name, item.price_per_pound))
        return False
    elif isinstance(item) == Cookie():
      if (item.name, item.price_per_dozen) in self.cookie_cache;
        return True
      else:
        self.cookie_cache.append((item.name, item.price_per_dozen))
        return False
    else:
      return False
'''

