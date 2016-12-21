import string 
from collections import defaultdict
import cPickle as pickle


#Binary search
def bsearch(A,target):
        
        n = len(A)
	last = n - 1 
	first = 0 

        if n == 0:
                return False
	
	m = (first + last) / 2 
       
        #print n,A[m]

        if A[m] == target:
                return True
        elif target < A[m]:
                return bsearch(A[:m], target)
        else:
                return bsearch(A[m+1:], target)



# getting the wordlist
fp = open('wordlist.txt', 'r')

words = []
agrams = []
for line in fp:
	word = line.rstrip()
	words.append(word)
	agrams.append(''.join(sorted(word)))


#sort agrams and remove duplicates

agrams_sor = list(sorted(set(agrams)))

#Build DAG

G = defaultdict(list)   #adj list

#each agram is a vx in DAG 
alpha_bet_list = list(string.uppercase)
count = 0 

print "len :: ", len(agrams_sor)

for ag in agrams_sor:
	count += 1
	print "count", count
	G[ag] = []
	for alpha_bet in alpha_bet_list:
		new_ag = ''.join(sorted(ag + alpha_bet))
			
		#check if new_ag exists in agrams_sor list
		if (bsearch(agrams_sor,new_ag) == True):
			#print "found true"
			
			#add a directed arc 
			G[ag].append(new_ag)


print G


with open('graph.txt', 'wb') as f:
  pickle.dump(G, f)

f.close()
