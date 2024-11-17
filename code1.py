import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node, to_node, weight):
        # Ensure both nodes are in the graph
        if from_node not in self.graph:
            self.graph[from_node] = []
        if to_node not in self.graph:
            self.graph[to_node] = []
       
        # Add the edge in both directions for an undirected graph
        self.graph[from_node].append((to_node, weight))
        self.graph[to_node].append((from_node, weight))

def dijkstra(graph, start, end):
    # Initialize distances with infinity and set start node distance to zero
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to select the node with the shortest tentative distance
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
   
    # Track path to reconstruct it at the end
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
       
        # Stop if we reach the destination
        if current_node == end:
            break
       
        # Skip processing if we find a longer path
        if current_distance > distances[current_node]:
            continue
       
        # Check neighboring nodes
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
           
            # Only consider this path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the shortest path
    path, current = [], end
    while previous_nodes[current] is not None:
        path.append(current)
        current = previous_nodes[current]
    path.append(start)
   
    return path[::-1], distances[end]

# Main function to take user input and execute the program
def main():
    transport_network = Graph()
   
    # Take input for the graph structure
    print("Enter the stations and travel time between them.")
    while True:
        from_station = input("From station (or 'done' to finish adding): ")
        if from_station.lower() == 'done':
            break
        to_station = input("To station: ")
        weight = int(input("Travel time between stations in minutes: "))
       
        transport_network.add_edge(from_station, to_station, weight)
   
    # Take input for start and destination stations
    start = input("Enter the starting station: ")
    end = input("Enter the destination station: ")

    # Run Dijkstra's algorithm to find the shortest path
    shortest_path, travel_time = dijkstra(transport_network.graph, start, end)
   
    # Display the result
    print(f"Shortest path from {start} to {end}: {shortest_path}")
    print(f"Total travel time: {travel_time} minutes")

# Run the main function
if __name__ == "__main__":
    main()
