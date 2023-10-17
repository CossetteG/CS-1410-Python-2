#Exam will be open for one week, opens tomorrow
#25 multiple choice questions, 2 hour test 

#implement the abstract method ----------------------------------------------------------------------------------------------------------------------------------------------------------------aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

from typing import Protocol, List, Union

class Drawable(Protocol):
    def draw(self) -> None:
        pass 
    
class Draggable(Protocol):
    def drag(self) -> None:
        pass
    
class Rectangle:
    def __init__(self) -> None:
        pass 
    
    def draw(self) -> None:
        print("draw rectangle")
        
class Circle:
    def __init__(self) -> None:
        pass 
    
    def draw(self) -> None:
        print("Draw a circle")

    # def drag(self) -> None:
    #     print("Drag circle to a point")


from abc import ABC, abstractmethod

class Drawable_(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass
    
class Rectangle_(Drawable_):
    def __init__(self) -> None:
        pass 
    
    def draw(self) -> None:
        print("draw rectangle")

rectangle = Rectangle()
circle = Circle()

def draw_shapes(shapes: List[Drawable]) -> None:
    for shape in shapes:
        shape.draw()

def draw_and_drag(shapes: List[Union[Drawable, Draggable]]):
    for shape in shapes:
        shape.draw()
        shape.drag() 

draw_shapes([rectangle])
draw_and_drag([rectangle, circle])

#if using it, @property (the getter/setter decorator) the decorator must be on 
# both and functions the same 
#if every method in a class is abstract and it has no implementation,
#  we call it an interface 
#Protocol is like interface for Python, since pythono supports multiple inheritance 
#multiple interface is available in all programing languages, unlike ^