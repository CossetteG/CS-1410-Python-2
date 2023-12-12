from typing import Protocol, List, Union, runtime_checkable

@runtime_checkable
class Packaging(Protocol):
  def __init__(self, packaging:str=None):
    self.packaging = packaging