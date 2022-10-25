
from collections import defaultdict

graph = defaultdict(list)
for x in range(8):
	for y in range(8):
		n1 = (x + 1, y + 2)
		n2 = (x + 1, y - 2)
		n3 = (x - 1, y + 2)
		n4 = (x - 1, y - 2)
		n5 = (x + 2, y + 1)
		n6 = (x + 2, y - 1)
		n7 = (x - 2, y + 1)
		n8 = (x - 2, y - 1)
		n = [n1, n2, n3, n4, n5, n6, n7, n8]
		for i in range(len(n)):
			if n[i][0] > -1 and n[i][1] > -1 and n[i][0] < 8 and n[i][1] < 8:
				graph[8*x+y].append(n[i][0]*8+n[i][1])
print(graph)

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a
        # new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print (bfs(graph, 0, 63))
