"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exits, connect v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex)
        # create an emtpy Set to stoe the visited vertices
        visited = set()
        # while the queue is not empty ...
        while queue.size() > 0:
            # dequeue the first vertex
            vert = queue.dequeue()
            # if that vertex has not been visited..
            if vert not in visited:
                # mark it as visited
                visited.add(vert)
                print(vert)
                # then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[vert]: # self.get_neighbors(vert)
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # create an empty Set to store the visited vertices
        visited = set()
        # while the stack is not empty ...
        while stack.size() > 0:
            # pop the first vertex
            vert = stack.pop()
            # if that vertex has not been visited ..
            if vert not in visited:
                # mark it is visited
                visited.add(vert)
                print(vert)
                # then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[vert]: #self.get_neighbors(vert)
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighb_vert in self.vertices[starting_vertex]:
            if neighb_vert not in visited:
                self.dft_recursive(neighb_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue A-PATH-TO the starting vertex ID
        # create a Set to store the visited vertices
        # while the queue is not empty ..
            # dequeue the first PATH
            # grab the last vertex from the PATH
            # if that vertex has not been visited ..
                # check if its the target
                    #if yes, return path
                #mark it as visited
                # add A PATH TO its neighbots to the back of the queue
                    # copt the path
                    # append the neighbor to the back
        
        
        # create an empty Queue 
        queue = Queue()
        #push the starting vertex ID as list
        queue.enqueue([starting_vertex])
        # create an empty Set to store the visited vertices
        visited = set()
        # while the queue is not empty ...
        while queue.size() > 0:
            # dequeue the first vertex
            path = queue.dequeue()
            vert = path[-1]
            # if that vertex has not been visited ..
            if vert not in visited:
                #check for target
                if vert == destination_vertex:
                    return path
                # mark it is visited
                visited.add(vert)
                # then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[vert]: #self.get_neighbors(vert)
                    #copy path to avoid pass by reference
                    new_path = list(path) # make a copy
                    new_path.append(neighbor)
                    queue.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # create an empty stack 
        stack = Stack()
        #push the starting vertex ID as list
        stack.push([starting_vertex])
        # create an empty Set to store the visited vertices
        visited = set()
        # while the stack is not empty ...
        while stack.size() > 0:
            # pop the first vertex
            path = stack.pop()
            vert = path[-1]
            # if that vertex has not been visited ..
            if vert not in visited:
                #check for target
                if vert == destination_vertex:
                    return path
                # mark it is visited
                visited.add(vert)
                # then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[vert]: #self.get_neighbors(vert)
                    #copy path to avoid pass by reference
                    new_path = list(path) # make a copy
                    new_path.append(neighbor)
                    stack.push(new_path)


    def dfs_recursive(self, starting_vertex, target, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target:
            return path
        for neighb_vert in self.vertices[starting_vertex]:
            if neighb_vert not in visited:
                new_path = self.dfs_recursive(neighb_vert, target, visited, path)
                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('Graph Vertices')
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("BFT")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT")
    graph.dft(1)
    print("DFT RECURSIVE")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS")
    print(graph.dfs(1, 6))
    print("DFS RECURSIVE")
    print(graph.dfs_recursive(1, 6))
