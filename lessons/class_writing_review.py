"""A."""

from typing import ItemsView

import platformdirs


food: bool = True 

# class Pond:
#     bread: int
#     ducks: list[str]

#     def __init__(self, bread: int, ducks: list[str]):
#         self.bread = bread
#         self.ducks = ducks
    
#     def unfed(self):
#         if len(self.ducks) > (self.bread / 2):
#             print(f"{self.ducks[len(self.ducks) - 1]} didn't get fed!")
#             global food
#             return food == False

#     def feed(self):
#         if food == False:
#             add_food = int(input(print("Give them some more bread:")))
#             self.bread += add_food


# class StrArray:
#     items: list[str]

#     def __init__(self, items) -> None:
#         self.items = items

#     def __repr__(self) -> str:
#         return f"StrArray({self.items})"
    
#     def __add__(self, rhs:str):
#         result: list[str] = []
#         for x in self.items:
#             result.append(x + rhs)
#         return StrArray(result)

# first: StrArray = StrArray([""])

class ChristmasTreeFarm:
    plots: list[int]
    def __init__(self, plots: int, initial_planting: int):
        """Sets up farm."""
        self.plots = []
        i = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1
    
    def plant(self, plot_index: int) -> :
        self.plots[plot_index] = 1 
    
    def growth(self):
        result = []
        for x in self.plots:
            x += 1
            result.append(x)
        return result
    
    def harvest(self, replant: bool):
        i = 0
        count = 0
        for x in self.plots:
            count +=1
            if x >= 5:
                i += 1
                if replant == True:
                    self.plots[count] = 1
                if replant == False:
                    self.plots[count] = 0
        return i
    def __add__(self, other: ChristmasTreeFarm) -> ChristmasTreeFarm:
        for x in other.plot:
            self.plots.append(x)
            


            






