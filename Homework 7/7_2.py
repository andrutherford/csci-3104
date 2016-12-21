import sys
import itertools

#function to print out the cloth, helps visualize where cuts have been made
def show(cloth, x, y):
    for i in range (0,y):
        for j in range(0,x):
            string = cloth[i][j]
            string2 = string.rstrip('\n')
            print(string2)
        print('\n') 

#helper function to guarantee that a solid rectangular cut can be made for a particular x1 * x2 size cut
def rect(cloth, piece, x, y, x2, y2):
    area = int(piece)
    d = 0
    for k in range (0,y):
        for j in range (0,x):
            for i in range (k, y2):
                if(cloth[i][j] == '1'):
                    d = d + 1
                    if(d == area):
                        str1 = str(x2)
                        str2 = str(y2)
                        for a in range (i-y2+1, i+1):
                            for b in range (j-x2+1, j+1):
                                cloth[a][b] = '0'
                        return True
                        break
                else:
                    d = 0
    return False

#function that checks all possible cuts and selects the most profitable option
def cut(cloth, options, x, y, prices):
    length = len(options)
    cuts = []
    comb = []
    area = x*y

    for i in range(0,length):
        x1 = int(options[i][0])
        y1 = int(options[i][1])
        price = prices[i]
        xy = x1 * y1
        cuts.append(xy)

    areaprice = []
    for p in range(0,length):
        areaprice = cuts[p], prices[p]

    for l in range(0,length):
        possibs = list(itertools.combinations(cuts,l))
        l2 = len(possibs)
        for q in range(0,l2):
            l3 = len(possibs[q])
            total = 0
            for v in range(0,l3):
                total = total + int(possibs[q][v])
            if(total < area):
                c = 0
                for w in range(0,l3):
                    if(possibs[q][w] == cuts[w]):
                        x3 = int(options[w][0])
                        y3 = int(options[w][1])
                    if(rect(cloth,possibs[q][w],x,y,x3,y3) == True):
                        c = c + 1
                if(c == l3):
                    comb.append(possibs[q])

    len5 = len(comb)
    max_profit = 0

    for y in range(0,len5):
        len6 = len(comb[y])
        tmpmoney = 0
        for z in range(0,len6):
            tmp = int(comb[y][z])
            #for s in range(0,length):
            #   if(tmp == int(areaprice[s])):
            #       tmp2 = int(price[s])
            tmpmoney = tmpmoney + tmp
        if(tmpmoney > max_profit):
            max_profit = tmpmoney

    str1 = str(max_profit)
    print("Max profit is " + "$" + str1)

#initializes all arguments from text file
def main():
    filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines() 
    num_lines = len(lines)
    dimensions = []
    for p in range (0,num_lines):
        tmp = lines[p].split()
        dimensions.append(tmp)
    x = int(dimensions[0][0])
    y = int(dimensions[0][1])
    area = x * y
    n = int(dimensions[1][0])
    options = []
    for i in range (2,n):
        options.append(dimensions[i])
    rows = []
    cloth = []
    for j in range (0,x):
        rows.append('1')
    for k in range (0,y):
        cloth.append(rows)
    prices = []
    length = len(options)
    for m in range (0, length):
        a = int(options[m][2])
        prices.append(a)
    cut(cloth, options, x, y, prices)

main()