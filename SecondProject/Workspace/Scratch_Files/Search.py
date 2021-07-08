

def bfs(graph, initial_vertex):
    
    visited=[0]*(int(graph[0]))
    queue=[initial_vertex]

    while queue:
        vertex = queue.pop(0)
        if visited[vertex]==0:

            visited[vertex]=1
            visited.append(vertex)
            for i in graph[1][vertex]:

                if  visited[vertex]==0:
                    queue.append(i)

    return visited



def dfs_r1(grafo, vertice):
    visitados = set()

    def dfs_recursiva(grafo, vertice):
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursiva(grafo, vizinho)

    dfs_recursiva(grafo, vertice)


def dfs_r2(grafo):
    def dfs_recursiva(grafo, vertice):
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursiva(grafo, vizinho)

    visitados = set()
    for vertice in grafo:
        print(visitados)
        if not vertice in visitados:
            dfs_recursiva(grafo, vertice)


def dfs_iterativa(grafo, vertice_fonte, visitados):
    visitados.add(vertice_fonte)
    falta_visitar = [vertice_fonte]
    while falta_visitar:
        vertice = falta_visitar.pop()
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                falta_visitar.append(vizinho)


def dfs(grafo, vertice):
    visitados = set()

    def dfs_iterativa(grafo, vertice_fonte):
        visitados.add(vertice_fonte)
        falta_visitar = [vertice_fonte]
        while falta_visitar:
            vertice = falta_visitar.pop()
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    falta_visitar.append(vizinho)

    dfs_iterativa(grafo, vertice)

