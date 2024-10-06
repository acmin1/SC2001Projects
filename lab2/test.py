
import math

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item, priority):
        """Add an item to the priority queue with the given priority."""
        self.queue.append((priority, item))
        self.queue.sort()  # Sort the queue by priority (ascending)

    def dequeue(self):
        """Remove and return the item with the highest priority (lowest value)."""
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")
        return self.queue.pop(0)[1]  # Remove and return the item

    def peek(self):
        """Return the item with the highest priority without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self.queue[0][1]  # Return the item

    def remove_item(self, item):
        """Remove the specified item from the priority queue."""
        for index, (priority, queue_item) in enumerate(self.queue):
            if queue_item == item:
                del self.queue[index]  # Remove the item by index
                return  # Exit after removing the item
        raise ValueError(f"Item '{item}' not found in the priority queue.")

    def __str__(self):
        return str(self.queue)

def dijkstra(adjacency_matrix, source):
    n = len(adjacency_matrix)
    
    # Initialize distances, visited array, and predecessor array
    distances = [math.inf] * n
    visited = [False] * n
    predecessors = [None] * n  # Predecessor array

    distances[source] = 0    
    # Initialize the priority queue
    q = PriorityQueue()
    q.enqueue(source, 0)  #enqueue(self, item, priority):

    while q.is_empty()==False:
        # Extract the vertex with the smallest distance
        u = q.dequeue()

        # Mark the vertex as visited
        visited[u] = True

        # Explore neighbors
        for v in range(n):
            weight = adjacency_matrix[u][v] # extracts the w[u,v]
            if weight == 0:  # There is no edge
                continue

            if(visited[v]==False and distances[v] > weight+ distances[u]):
                q.remove_item(v)
                distances[v] = weight+ distances[u]
                predecessors[v] = u
                q.enqueue(v, distances[v])
                
    
    return distances, predecessors

def reconstruct_path(predecessors, target):
    """Reconstruct the path from source to target using the predecessor array."""
    path = []
    while target is not None:
        path.append(target)
        target = predecessors[target]
    path.reverse()  # Reverse to get the path from source to target
    return path


graph = [
        [0, 7, 0, 0, 0, 2],
        [7, 0, 6, 0, 0, 1],
        [0, 6, 0, 5, 0, 0],
        [0, 0, 5, 0, 2, 0],
        [0, 0, 0, 2, 0, 3],
        [2, 1, 0, 0, 3, 0]
    ]

source_vertex = 0
distances,predecessors  = dijkstra(graph, source_vertex)
print(f"Distances from vertex {source_vertex}: {distances}")

target_vertex = 4  # Example target
path = reconstruct_path(predecessors, target_vertex)
print(f"Shortest path from {source_vertex} to {target_vertex}: {path}")