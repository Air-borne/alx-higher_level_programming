#!/usr/bin/python3

"""
...
"""
from models.base import Base

class Rectangle(Base):
	"""
	...
	"""
	
	def __init__(self, width, height, x=0, y=0, id=None):
		"""
		...
		"""
		
		super().__init__(id)
		
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y
	
	@property
	def width(self):
		"""
		...
		"""
		return self.__width
	
	@width.setter
	def width(self, param):
		"""
		...
		"""
		self.__width = param
	
	@property
	def height(self):
		"""
		...
		"""
		return self.__height
	
	@height.setter
	def height(self, param):
		"""
		...
		"""
		self.__height = param
		
	@property
	def x(self):
		"""
		...
		"""
		return self.__x
	
	@width.setter
	def x(self, param):
		"""
		...
		"""
		self.__x = param
	
	@property
	def y(self):
		"""
		...
		"""
		return self.__y
	
	@width.setter
	def y(self, param):
		"""
		...
		"""
		self.__y = param
