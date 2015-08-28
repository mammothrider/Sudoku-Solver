#sudoku
import os, sys
import copy


sudokuGlobalBoard = [ 
0, 0, 4,  0, 2, 0,  0, 0, 0,
0, 0, 0,  9, 0, 0,  6, 0, 0, 
0, 0, 0,  0, 0, 0,  5, 0, 7, 

0, 0, 0,  0, 0, 0,  0, 0, 4, 
0, 0, 0,  0, 0, 9,  0, 0, 1, 
3, 0, 0,  5, 0, 0,  0, 0, 0, 

0, 0, 0,  0, 0, 0,  0, 0, 0, 
5, 0, 0,  0, 0, 0,  3, 9, 0, 
0, 2, 0,  0, 4, 1,  0, 0, 0, 
]

class sudokuSolver:
	
	Avail = [[] for i in range(81)]
	sudokuBoard = []
	
	def __init__(self, _board):
		self.sudokuBoard = [i for i in _board]
	
	def checkAvail(self, nine):
		a = []
		for i in range(1, 10):
			if i not in nine:
				a.append(i)
		return a
		
	def findIntersection(self, a, b):
		r = [x for x in a if x in b]
		#print r, a, b
		return r
	
	def getAvail(self):
		
		self.Avail[:] = [[] for i in range(81)]
		
		for num in range(81):
			if self.sudokuBoard[num] == 0:
				line = self.checkAvail(self.sudokuBoard[num/9*9:(num/9+1)*9])
				col  = self.checkAvail([self.sudokuBoard[num % 9 + i * 9] for i in range(9)])
				x = (num / 9) / 3
				y = (num % 9) / 3
				temp = self.sudokuBoard[(x*3*9 + y*3):(x*3*9 + y*3 + 3)] \
					 + self.sudokuBoard[(x*3*9 + y*3 + 9):(x*3*9 + y*3 + 12)] \
					 + self.sudokuBoard[(x*3*9 + y*3+18):(x*3*9 + y*3 + 21)]
				nine = self.checkAvail(temp)
				#print x, y
				#print temp
				
				self.Avail[num] = self.findIntersection(self.findIntersection(line, col), nine)
				#print num , ":" , self.Avail[num], line, col, nine
		return
	
	def elim(self):
		change = 0
		for num in range(81):
			#print num, self.Avail[num]
			#print "test:", num
			if self.sudokuBoard[num] == 0:
				if len(self.Avail[num]) == 1:
					self.sudokuBoard[num] = self.Avail[num][0] #only one correct answer
					change = 1
					
			#check line
			if self.sudokuBoard[num] == 0:
				for each in self.Avail[num]:
					lock = 0
					
					for j in self.Avail[num/9*9:(num/9+1)*9]:
						if each in j:
							lock += 1
							
					if lock == 1:
						self.sudokuBoard[num] = each
						change = 1
						#print "line:", num, each
						break
						
			#check col
			if self.sudokuBoard[num] == 0:
				#print self.Avail[num]
				for each in self.Avail[num]:
					lock = 0
					
					for j in [self.Avail[num % 9 + i * 9] for i in range(9)]:
						if each in j:
							lock += 1
							
					if lock == 1:
						self.sudokuBoard[num] = each
						change = 1
						#print "col", num, each
						break
	
			#check nine
			x = (num / 9) / 3
			y = (num % 9) / 3
			if self.sudokuBoard[num] == 0:
				for each in self.Avail[num]:
					lock = 0
					
					temp = self.Avail[(x*3*9 + y*3):(x*3*9 + y*3 + 3)] \
					 + self.Avail[(x*3*9 + y*3 + 9):(x*3*9 + y*3 + 12)] \
					 + self.Avail[(x*3*9 + y*3+18):(x*3*9 + y*3 + 21)]
					#print num, each, temp
					for j in temp:
						if each in j:
							lock += 1
							
					if lock == 1:
						self.sudokuBoard[num] = each
						change = 1
						#print "nine:",num, each
						break
		return change
		
	def printBoard(self):
		for i in range(9):
			print self.sudokuBoard[i*9:i*9+9]
		
	def returnBoard(self):
		count = 0
		
		change = 1
		while change:
			print "Pace ", count
			count += 1
			self.printBoard()
			self.getAvail()
			change = self.elim()
				
			print "\n\n\n"
		return copy.copy(self.sudokuBoard)
		
	def returnMorePosibility(self):
		returnList = []
		
		self.getAvail() #refresh the Avail list 
		
		#leagal check
		for index in range(81):
			if self.sudokuBoard[index] == 0 and len(self.Avail[index]) == 0:
				print "Number Conflict!"
				return -1
		
		for index in range(81):
			if len(self.Avail[index]) == 1:
				print "System Error"
				return -1
			elif len(self.Avail[index]) >= 2:
				break
		
		for j in self.Avail[index]:
			tempBoard = copy.copy(self.sudokuBoard)
			tempBoard[index] = j
			returnList.append(tempBoard)
			
		if len(returnList) <= 0:
			print "Empty list"
			return -1
		return returnList
		
	def checkAccomplishment(self):
		if 0 in self.sudokuBoard:
			return "Unfinished"
			
			
		for num in range(81):
			line = self.checkAvail(self.sudokuBoard[num/9*9:(num/9+1)*9])
			col  = self.checkAvail([self.sudokuBoard[num % 9 + i * 9] for i in range(9)])
			x = (num / 9) / 3
			y = (num % 9) / 3
			temp = self.sudokuBoard[(x*3*9 + y*3):(x*3*9 + y*3 + 3)] \
				 + self.sudokuBoard[(x*3*9 + y*3 + 9):(x*3*9 + y*3 + 12)] \
				 + self.sudokuBoard[(x*3*9 + y*3+18):(x*3*9 + y*3 + 21)]
			nine = self.checkAvail(temp)
				
			if line + col + nine: #line or col or nine is not empty, means one of them lose some number.
				return "Conflict"
				
		return "Finished"
		
class morePosibility:
	
	boardList = []
	testNumber = 0
	
	def __init__(self, upperBoard):
		self.boardList.append(upperBoard)
	
	def tryMore(self):
		board = self.boardList.pop()
		
		print "New Test ", self.testNumber
		solver = sudokuSolver(board)
		returnBoard = solver.returnBoard()
		finished = solver.checkAccomplishment()
		print "Test ", self.testNumber, " ", finished
		self.testNumber += 1
		
		if 0 in returnBoard: #means unfinish
			returnList = solver.returnMorePosibility() #exhaustion
			if returnList == -1:
				print "Test Failed"
			else:
				for tempBoard in returnList:
					self.boardList.append(tempBoard)
		return returnBoard, finished
				
	def run(self):
		finalBoard = []
		finished = 0
		while self.boardList or finished != "Finished":
			finalBoard, finished = self.tryMore()
		return finalBoard

if __name__ == '__main__':
	tool = morePosibility(sudokuGlobalBoard)
	a = tool.run()
	
	print " \n"*3
	print "Final Result"
	for i in range(9):
			print a[i*9:i*9+9]