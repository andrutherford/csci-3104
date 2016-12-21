import sys

class CutPrices():
	def __init__(self):
		#stores where a cut can be and the value of that cut
		self.matrix = []


	def initMatrix(self, x,y):
		countx = 0
		while countx < x:
			templist = []
			county = 0
			while county < y:
				templist.append(-1)
				county += 1
			self.matrix.append(templist)
			countx += 1

	def getCosts(self, specs):
		for row in specs:
			self.matrix[row[0] -1][row[1] - 1] = row[2]

class Cloth():
	def __init__(self):
		#stores where cuts should happen and the financial return
		self.matrix = []


	def initMatrix(self, x, y):
		countx = 0
		while countx < x:
			templist = []
			county = 0
			while county < y:
				templist.append(-1)
				county += 1
			self.matrix.append(templist)
			countx += 1
		#upper left corner equals 0
		if self.matrix:
			self.matrix[0][0] = 0


	def maxReturn(self, pricing):
		x = 1
		while x < len(self.matrix):
			y = 1
			while y < len(self.matrix[0]):
				self.computeVal(x, y, pricing)
				y += 1
			x += 1

	def computeVal(self, x, y, pricing):
		if self.matrix[x][y] is not -1:
			pass
		else:
			max1 = -1
			max2 = -1
			max3 = pricing[x][y]
			count1 = 1
			count2 = 1
			while count1 < x:
				tempval = self.matrix[count1][y] + self.matrix[x - count1][y]
				if tempval > max1:
					max1 = tempval
				count1 += 1
			while count2 < y:
				tempval = self.matrix[x][y - count2] + self.matrix[x][count2]
				if tempval > max2:
					max2 = tempval
				count2 += 1
			maxval = max(max1, max2, max3)

			self.matrix[x][y] = maxval


if __name__ == '__main__':

	#initialize one of each
	m_p = CutPrices()
	m_r = Cloth()

	#get the product dimensions information from the disk
	f = open(sys.argv[1],"r")
	x = f.readline().strip().split()
        f.readline()
	#with open(f) as f:
	cols = f.readlines()

	specs = []
	for col in cols:
		row = col.split('\n')[0]
		row = row.strip().split()
		templist = []
		for i in row:
			templist.append(int(i))
		specs.append(templist)

	#get the spec pricing and make sure the cloth is bigger than the spec
	minx = specs[0][0]
	miny = specs[0][1]
	for i in specs:
		if i[0] > minx:
			minx = i[0]
		if i[1] > miny:
			miny = i[1]

	#get the dimension of the cloth from the user
	xin = x[0]
	yin = x[1]


	#if the values are valid run the computation
	if int(xin) > minx and int(yin) > miny:
		m_p.initMatrix(int(xin), int(yin))
		m_r.initMatrix(int(xin), int(yin))
		m_p.getCosts(specs)
		m_r.maxReturn(m_p.matrix)
        print "Dimensions of the cloth:\nX = " + str(xin) + "\nY = "+ str(yin)
        print "X x Y cut specs"
        print specs
	print "maximum value of the cloth:", m_r.matrix[-1][-1]

else:
	print "values too small, closing"
