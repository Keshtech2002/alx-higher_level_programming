#!/usr/bin/python3
"""A Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """update string representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
