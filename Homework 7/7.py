import sys

class Cut:
    def __init__(self, x = 0, y = 0, profit= 0):
        self.x = x
        self.y = y
        self.profit = profit
    
    def getProfitDensity(self):
        assert self.profit != 0
        return (self.x * self.y) / self.profit;
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.profit) + "]"

class ClothInfo:
    def __init__(self, x = 0, y = 0, n = 0):
        self.x = x
        self.y = y
        self.n = n
        self.cuts = [] # store the cuts in x list
    
    def setDimensions(self, x, y):
        self.x = x
        self.y = y
    
    def setN(self, n):
        self.n = n
    
    def addCut(self, a, b, c):
        self.cuts.append(Cut(a, b, c))
    
    def toString(self):
        return "Dimensions: " + str(self.x) + " x " + str(self.y) + "\n" + "N: " + str(self.n) + "\n" + "Cuts: " + str(self.cuts)

def parseClothFile(fileName):
    # first line is X and Y values
    # second line is n value
    # each other line is x, y, c
    cloth = ClothInfo()
    fo = open(fileName, "r")
    lines = fo.readlines()
    for i in range(0, len(lines)):
        if (i == 0): # first line, parse X and Y
            params = lines[i].strip().split()
            x = int(params[0])
            y = int(params[1])
            cloth.setDimensions(x, y)
        elif (i == 1): # second line, parse n
            n = int(lines[i].strip())
            cloth.setN(n)
        else: # parse x, y, c
            params = lines[i].strip().split()
            a = int(params[0])
            b = int(params[1])
            c = int(params[2])
            cloth.addCut(a, b, c)
        #print lines[i].strip()
    return cloth

def main():
    cloth = parseClothFile(sys.argv[1])
    print cloth.toString()
    findBestCuts(cloth)

def findCut(cloth, x, y):
    localcut = Cut()
    for cut in cloth.cuts:
        if (cut.x <= x and cut.y < y and cut.profit > localcut.profit):
            localcut = cut
    print localcut
    if (localcut.profit == 0):
        return None
    return localcut

def findBestCuts(cloth):
    # find the best cut that will fit in this cloth
    mostprofitpercut = Cut()
    for cut in cloth.cuts:
        # Step 1: Check if the cut will fit.
        # Step 2: Check if profit is optimal
        if (cut.x <= cloth.x and cut.y <= cloth.y and cut.profit > mostprofitpercut.profit): 
            mostprofitpercut = cut
    print "most profit per cut = " + str(mostprofitpercut)
    mostprofitareacut = Cut()
    density = 0
    for cut in cloth.cuts:
        if (cut.getProfitDensity() > density):
            density = cut.getProfitDensity()
            mostprofitareacut = cut
    print "most profit area cut = " + str(mostprofitareacut)
    cloth1 = [cloth.x, cloth.y]
    cloth1profit = 0
    cloth2 = [cloth.x, cloth.y]
    cloth2profit = 0
    while True:
        # Start making cuts
        if (cloth1[0] >= mostprofitpercut.x and cloth1[1] >= mostprofitpercut.y):
            cloth1[0] = cloth1[0] - mostprofitpercut.x
            cloth1[1] = cloth1[1] - mostprofitpercut.y
            cloth1profit = cloth1profit + mostprofitpercut.profit
        else:
            # find more cuts
            anotherCut = findCut(cloth, cloth1[0], cloth1[1])
            if (anotherCut == None):
                break
            else:
                cloth1[0] = cloth1[0] - anotherCut.x
                cloth1[1] = cloth1[1] - anotherCut.y
                cloth1profit = cloth1profit + anotherCut.profit
    print "cloth 1: " + str(cloth1)
    print "cloth 1 profit: " + str(cloth1profit)
    while True:
        # Start making cuts
        if (cloth2[0] >= mostprofitareacut.x and cloth2[1] >= mostprofitareacut.y):
            cloth2[0] = cloth2[0] - mostprofitareacut.x
            cloth2[1] = cloth2[1] - mostprofitareacut.y
            cloth2profit = cloth2profit + mostprofitareacut.profit
        else:
            # find more cuts
            anotherCut = findCut(cloth, cloth2[0], cloth2[1])
            if (anotherCut == None):
                break
            else:
                cloth2[0] = cloth2[0] - anotherCut.x
                cloth2[1] = cloth2[1] - anotherCut.y
                cloth2profit = cloth2profit + anotherCut.profit
    print "cloth 2: " + str(cloth2)
    print "cloth 2 profit: " + str(cloth2profit)

if (__name__ == "__main__"):
    main()
