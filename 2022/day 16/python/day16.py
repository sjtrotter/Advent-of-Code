#!/usr/bin/env python

inputfile = open("input2.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

rates = {}
Graph_nodes = {}
for line in data_list:
    rates[line.split(" ")[1]] = \
        int(line.split(";")[0].split(" ")[-1].split("=")[-1])
    Graph_nodes[line.split(" ")[1]] = []
    if "valves" in line:
        for neighbor in line.split(";")[1].split("valves ")[-1].split(", "):
            Graph_nodes[line.split(" ")[1]].append((neighbor,1))
            
    else:
        for neighbor in line.split(";")[1].split("valve ")[-1].split(", "):
            Graph_nodes[line.split(" ")[1]].append((neighbor,1))

# print("rates:",rates)
print("graph",Graph_nodes)

def aStarAlgo(start_node, stop_node):
    # print(start_node)
    steps = 0
    open_set = set()
    open_set.add(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        # print(n)
        for v in open_set:
            if n == None or g[v] + heuristic(v,steps) < g[n] + heuristic(n,steps):
                n = v
        # print(n)
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m,weight) in get_neighbors(n):
                # print(m)
                # print(get_neighbors(n))
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

        steps += 1
        open_set.remove(n)
        closed_set.add(n)
    # print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(a,steps):
    h = steps
    return h

theFlows = []
for flow in rates.values():
    if flow != 0:
        theFlows.append(flow)

theFlows.sort(reverse=True)
print(theFlows)
path = []
path.append("AA")
actualCost = {}
for flow in theFlows:
    for key in rates.keys():
        if rates[key] == flow:
            actualCost[key] = [rates[key] - (len(aStarAlgo("AA",key))-1),len(aStarAlgo("AA",key))-1]

print(actualCost)




# set of Graph_nodes
# find highest rate with lowest cost
