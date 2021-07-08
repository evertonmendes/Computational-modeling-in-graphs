adj_list = {
    "A" : ["C", "B", "D"],
    "B" : ["A", "D"],
    "C" : ["A"],
    "D" : ["A","B" "E"],
    "E" : ["D"]
}

color = {}
parent = {}

for u in adj_list.keys():
    color[u] = 'W'
    parent[u] = None

def dfs(u, color, parent):
    color[u] = 'G'
    for v in adj_list[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs(v, color, parent)
        elif color[v] == "G" and parent[u]!=v:
            print ("Cycle found", u, v)
            return True
    color[u] = "B"
    return False

is_cyclic = False
for u in adj_list.keys():
    if color[u] == 'W':
        is_cyclic = dfs(u, color, parent)
        if is_cyclic == True:
            break
print ("Is_cyclic ", is_cyclic)