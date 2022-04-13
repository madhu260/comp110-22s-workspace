from __future__ import annotations

class Point:
    # Attribute Definitions
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Constructor definition for initialization of attributes."""
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        """"Special"""
        return f"{self.x}, {self.y}"

    def __mul__(self, factor: float) -> Point:
        """Calculate."""
        return Point(self.x * factor, self.y * factor)

