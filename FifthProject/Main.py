import os
from collections import defaultdict
import heapq




def Main():

    def ReadPajek(filename=''):

                archive= open(filename, 'r')       
                aux=archive.readline().split()
                n_nodes=aux[1]
                n_nodes=int(n_nodes)

                type_of_graph=archive.readline()

                AdjList_dict={}
                for vertex in range(n_nodes):
                    AdjList_dict[vertex+1]={}

                if type_of_graph[:6]=="*Edges":

                    for edges in archive:
                        edges=edges.split()
                        try:
                            AdjList_dict[int(edges[0])][int(edges[1])]=int(edges[2])
                            AdjList_dict[int(edges[1])][int(edges[0])]=int(edges[2])
                        except(IndexError):
                            print(len(AdjList_dict), edges)

                else:

                    for edges in archive:           
                        edges=edges.split()
                        try:
                            AdjList_dict[int(edges[0])][int(edges[1])]=int(edges[2])
                        except(IndexError):
                            print(len(AdjList_dict), edges)

                archive.close()
                return n_nodes, AdjList_dict



    def Prim_algorithm(graph, initial_vertex):
        mst = defaultdict(set)
        visited = set([initial_vertex])
        edges = [(weight, initial_vertex, toward) for toward, weight in graph[initial_vertex].items()]
        heapq.heapify(edges)

        while edges:
            weight, frm, toward = heapq.heappop(edges)
            if toward not in visited:
                visited.add(toward)
                mst[frm].add(toward)
                for next_neighbor, weight in graph[toward].items():
                    if next_neighbor not in visited:
                        heapq.heappush(edges, (weight, toward, next_neighbor))

        return mst


    help_path=os.path.dirname(__file__)
    file_name=input()
    graph=ReadPajek(filename=help_path+"/"+file_name)
    prim_mst=Prim_algorithm(graph[1], 1)

    count=0
    for x in prim_mst.keys():
        for y in prim_mst[x]:
            count+=graph[1][x][y]
    
    txt_file=open(file_name.replace("pajek", "txt"), "w")
    txt_file.write(str(count))
    txt_file.close()

    print(count)

    
    

Main()