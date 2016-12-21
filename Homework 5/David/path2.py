
import sys
import string

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
        
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
        
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    verts = [item for item in graph.getVertex(start).getConnections() if item not in visited]
    for vert in verts:
        dfs(graph, vert.getId(), visited)
    return visited

def alphagram(word):
    return "".join(sorted(word))

def isEdge(word1, word2):
    if (len(word1) == len(word2) + 1):
        return set(word1).intersection(set(word2)) == word2
    else:
        return False

def main():
    fo = open('wordlist.txt', "r")
    lines = fo.readlines()
    lines.sort()
    g = Graph()
    # create a dictionary with alphagram as key, word as value
    wordlist = dict()
    # for every name in file create a vertex
    for line in lines:
        line = line.strip()
        g.addVertex(line)
        wordlist[alphagram(line)] = line
    for word in g.getVertices():
        for c in string.ascii_uppercase: # iterate from A to Z
            new_word = alphagram(word + c) # add a letter to the alphagram
            if alphagram(new_word) in wordlist:
                # word exists, add edge
                g.addEdge(word, wordlist[alphagram(new_word)])
    fo.close()
    # once graph is created then perform dfs on every node
    max_depth = 0 # we'll keep track of the max depth we encounter
    for word in g.getVertices():
        search = dfs(g, word)
        depth = len(search)
        if depth > max_depth: # if we encounter a deeper search, print results and update old counter
            max_depth = depth
            print search
    
if __name__ == "__main__":
    main()
