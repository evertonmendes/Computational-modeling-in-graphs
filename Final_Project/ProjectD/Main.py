import os

def Main():

    def ReadPajek(filename=''):

        archive= open(filename, 'r')
            
        aux=archive.readline().split()
        n_nodes=aux[1]
        n_nodes=int(n_nodes)

        #Drop the string information 'Edges or Arcs'
        type_of_graph=archive.readline()

        adjency_list=[0]*n_nodes
        for i in range(len(adjency_list)):
            adjency_list[i]=[]


        if type_of_graph[:6]=="*Edges":

            for edges in archive:
                print(edges)
                
                edges=edges.split()
                try:
                    adjency_list[int(edges[0])-1].append(int(edges[1]))
                    adjency_list[int(edges[1])-1].append(int(edges[0]))
                except(IndexError):
                    print(len(adjency_list), edges)

        else:

            for edges in archive:
                
                edges=edges.split()
                try:
                    adjency_list[int(edges[0])-1].append(int(edges[1]))
                except(IndexError):
                    print(len(adjency_list), edges)


        archive.close()

        return n_nodes, adjency_list

    
    def bfs(graph, initial_vertex, final_vertex):
        
        queue=[initial_vertex]
        visited={}
            
        visited[initial_vertex]=0

        while queue:

            if final_vertex in visited:
                return visited[final_vertex]

            vertex = queue.pop(0)

            for neighbor in graph[1][vertex-1]:

                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = visited[vertex] + 1


        return 0

    def Found_sink(graph):

        sink_vertexs=[]
        for index, neighbors in enumerate(graph[1]):
            if len(neighbors)==0:
                sink_vertexs.append(index+1)
        
        return sink_vertexs

    def dfs_all(graph):

        def dfs(graph, vertex):
            visited.add(vertex)
            for neighbor in graph[1][vertex-1]:
                parent[neighbor].append(vertex)
                if neighbor not in visited:
                    dfs(graph, neighbor)
                    

        visited = set()
        previous_lenght=1
        components=[]
        parent={}
        for vertex in range(graph[0]):
            parent[vertex+1]=[]


        for vertex in range(graph[0]):
        
            if not vertex in visited:
                dfs(graph, vertex)
                components.append(len(visited)-previous_lenght)
                previous_lenght=len(visited)
        
        return parent

    def dfs_one(graph, vertex=1, visited=[]):
    
        visited.append(vertex)
        for neighbor in graph[1][vertex-1]:
            if neighbor not in visited:
                dfs_one(graph, neighbor)
    
        return visited

    def ProjectC(parent_sink, descendant, sinks):
        
        vertexs_projectC=[]
        for sink in sinks:
            if (parent_sink[sink][0] and parent_sink[sink][1] in descendant):
                vertexs_projectC.append(sink)

        return vertexs_projectC

    def Distances(graph, vertex):

        distance_vector=[]
        for value in range(graph[0]):
            distance_vector.append(bfs(graph, vertex, value))

        return distance_vector


    def Minimum_sum(parent_sink, vertexs_c, distances_list):

        count=float('inf')
        last_count=float('inf')
        vertexs_d=[]
    
        for vertex in vertexs_c:
            if (int(distances_list[parent_sink[vertex][0]])+int(distances_list[parent_sink[vertex][1]]) <= count):
                count=distances_list[parent_sink[vertex][0]]+distances_list[parent_sink[vertex][1]]
                if last_count!=count:
                    vertexs_d=[]
                    vertexs_d.append(vertex)
                    last_count=count
                else:
                    vertexs_d.append(vertex)
                    

        return vertexs_d

    
    help_path=os.path.dirname(__file__)
    file_name=input()
    graph=ReadPajek(filename=help_path+"/"+file_name)
    parent_v=dfs_all(graph)
    descendant_v=dfs_one(graph)
    sinks_v=Found_sink(graph)
    c_vertexs=ProjectC(parent_v, descendant_v, sinks_v)
    v_distances=Distances(graph, 1)
    d_vertexs=Minimum_sum(parent_v, c_vertexs, v_distances)

    for value in d_vertexs:
        print(value)



Main()


                




