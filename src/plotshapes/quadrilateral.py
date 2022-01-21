import numpy as np

class rectangle:
	"""This class defines an object of type rectangle. 
	Attributes: 
		center: (0,0) by default
		radius
		fill_type"""
	
	def __init__(self, a,b, center=(0,0),pts=100):
		
		self.xc, self.yc = center
		
		self.a = a
		self.b = b
		
		pts_by_2 = int(pts/2)
		
		pts_a = int(pts_by_2*self.a/self.b)
		pts_b = pts_by_2 - pts_b
		
		self.perimeter = 2*(self.a+self.b)
		self.area = self.a * self.b
		
		self.x = np.linspace(-self.a/2,self.a/2,pts_a) + self.xc
		self.y = -self.b/2*np.ones_(pts_a) + self.yc
