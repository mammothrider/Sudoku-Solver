import copy

class test:
	
	a = [1, 2, 3]
	
	def testreturn(self):
		return self.a
		
b = test()
c = b.testreturn()
print c
c[1] = 100
print c
print b.a