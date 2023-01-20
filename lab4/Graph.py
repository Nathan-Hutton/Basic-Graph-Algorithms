
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang and Nathan Hutton
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 

        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
        self.cycle = False
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.DFSInit()
        if method == 'recursive':
            for vertex in self.vertices:
                if vertex in self.unVisitedVertices:
                    self.DFS_recur(vertex)




            return self.path
        elif method == 'stack':
            for vertex in self.vertices:
                if vertex in self.unVisitedVertices:
                    self.DFS_stack(vertex)



            
            return self.path
            

    def DFS_recur(self,vertex):
        self.unVisitedVertices.remove(vertex)
        self.path += vertex
        for node in self.adjacencyList[vertex]:
            if node in self.unVisitedVertices:
                self.DFS_recur(node)
            
                
    def DFS_stack(self, vertex):
        stack=[]
        stack.append(vertex)
        while stack:
            node = stack.pop()
            if node in self.unVisitedVertices:
                self.unVisitedVertices.remove(node)
                self.path += node
                for adjacent_node in self.adjacencyList[node]:
                    if adjacent_node in self.unVisitedVertices:
                        stack.append(adjacent_node)
                    elif adjacent_node != self.adjacencyList[node][0]:
                        self.cycle = True


    def BFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""
        

    def BFS(self):
        self.BFSInit()
        for vertex in self.vertices:
            if vertex in self.unVisitedVertices:
                self.BFS_queue(vertex)

        return self.path


    def BFS_queue(self, vertex):
        queue = []
        self.unVisitedVertices.remove(vertex)
        self.path += vertex
        queue.append(vertex)
        while queue:
            node = queue.pop(0)
            for adjacent_node in self.adjacencyList[node]:
                if adjacent_node in self.unVisitedVertices:
                    self.unVisitedVertices.remove(adjacent_node)
                    self.path += adjacent_node
                    queue.append(adjacent_node)


    def hasCycle(self):
        self.DFS('stack')
        return self.cycle

                    
    # Work on this function for at most 10 extra points
    def shortestpath(self, p, q):
        self.BFSInit()
        queue = []
        levels = {p: 0}
        self.unVisitedVertices.remove(p)
        queue.append(p)
        while queue:
            node = queue.pop(0)
            if node == q:
                return levels[node]
            for adjacent_node in self.adjacencyList[node]:
                if adjacent_node in self.unVisitedVertices:
                    levels[adjacent_node] = levels[node] + 1
                    self.unVisitedVertices.remove(adjacent_node)
                    queue.append(adjacent_node)
