#!/usr/bin/env python

#get start and end


def aStarAlgo(start_node, stop_node):


    # print(start_node)
    open_set = { start_node }
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        # print(n)
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        # print(n)
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m,weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            # print('Path does not exist!')
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()
            # print('Path found:',path)
            return path

        open_set.remove(n)
        closed_set.add(n)
    # print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(a):
    h = abs(a[0] - end[0]) + abs(a[1] - end[1])
    return h


inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

theMap = {}
for y in range(len(data_list)):
    for x in range(len(data_list[y])):
        theMap[(x,y)] = data_list[y][x]

theMapLength = len(data_list[0])
theMapHeight = len(data_list)


start = next(k for k,v in theMap.items() if v == "S")
theMap[start] = "a"

end = next(k for k,v in theMap.items() if v == "E")
theMap[end] = "z"


Graph_nodes = {}
for y in range(theMapHeight):
    for x in range(theMapLength):
        
        candidates = []
        # print(x,y)
        # print(ord(theMap[(x,y)]))
        if x - 1 > -1 and ord(theMap[(x-1,y)]) <= ord(theMap[(x,y)])+1:
                candidates.append((x-1,y))
        if x + 1 < theMapLength and ord(theMap[(x+1,y)]) <= ord(theMap[(x,y)])+1:
                candidates.append((x+1,y))
        if y - 1 > -1 and ord(theMap[(x,y-1)]) <= ord(theMap[(x,y)])+1:
                candidates.append((x,y-1))
        if y + 1 < theMapHeight and ord(theMap[(x,y+1)]) <= ord(theMap[(x,y)])+1:
                candidates.append((x,y+1))
        # print(candidates)

        Graph_nodes[(x,y)] = []
        for entry in candidates:
            Graph_nodes[(x,y)].append((entry,1))


# print(Graph_nodes)

print("part1:", len(aStarAlgo(start, end))-1)

theAs = []
for y in range(theMapHeight):
    for x in range(theMapLength):
        if theMap[x,y] == "a":
            theAs.append((x,y))

distances = []
for point in theAs:
    result = aStarAlgo(point,end)
    if result != None:
        distances.append(len(result)-1)
# print(distances)
distances.sort()
print("part2:",distances[0])