"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730475197"


class Simpy:
    values: list[float]

    def __init__(self, a_list: list[float]) -> None:
        """Initializes a list of values."""
        self.values = a_list
    
    def __str__(self) -> str:
        """Converts to str representation."""
        return f"Simpy({self.values})"

    def fill(self, subj: float, multip: int) -> None:
        """Repeat given value n number of times."""
        result: list[float] = []
        for x in range(multip):
            result.append(subj)
        self.values = result
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Multiple of given number from start to stop."""
        i: int = 0
        x: float = 0.0
        if start >= 0.0 and stop >= 0.0:
            while x < (stop - step):
                x = start + (step * i)
                i += 1
                self.values.append(x)
        else:
            while x > (stop - step):
                x = start + (step * i)
                i += 1
                self.values.append(x)

    def sum(self) -> float:
        """Adds given list."""
        a_num: float = 0.0
        a_num = sum(self.values)
        return a_num

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Defines '+' in context of this class."""
        result = Simpy([])
        for x in self.values:
            result.values.append(x)
        if isinstance(rhs, float):
            i: int = 0
            for x in self.values:
                result.values[i] += rhs
                i += 1
        else:
            i: int = 0
            for x in rhs.values:
                result.values[i] += x
                i += 1
        return result
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Defines '**' in context of this class."""
        result = Simpy([])
        for x in self.values:
            result.values.append(x)

        if isinstance(rhs, float):
            i: int = 0
            for x in self.values:
                result.values[i] **= rhs
                i += 1
        else:
            i: int = 0
            for x in rhs.values:
                result.values[i] **= x
                i += 1
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Returns list of boolian comparing if items in 2 lists match or not."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for x in self.values:
                if x == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            i: int = 0
            for x in self.values:
                if x == rhs.values[i]:
                    result.append(True)
                    i += 1
                else:
                    result.append(False)
                    i += 1

        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Returns list of boolian comparing if items in a list is greater than that of another."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for x in self.values:
                if x > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            i: int = 0
            for x in self.values:
                if x > rhs.values[i]:
                    result.append(True)
                    i += 1
                else:
                    result.append(False)
                    i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]: 
        """Returns items that fullfill a requirement."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result = Simpy([])
            i: int = 0
            for x in rhs:
                if x is True:
                    result.values.append(self.values[i])
                    i += 1
                else:
                    i += 1
            return result