#Name: Éverton Luís Mendes da Silva
#NºUSP: 10728171

import os

def main():

    def ReadPajek(filename=''):

            archive= open(filename, 'r')       
            aux=archive.readline().split()
            n_nodes=aux[1]
            n_nodes=int(n_nodes)

            type_of_graph=archive.readline()

            AdjList_dict={}
            for vertex in range(n_nodes):
                AdjList_dict[vertex+1]={}

            if type_of_graph=="*Edges":

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


    def Dijkstra_Algorithm(graph, begin_vertex):

        minimum_distance={}
        for vertex in graph:
            minimum_distance[vertex]=float('inf')
        minimum_distance[begin_vertex]=0
        
        predecessor = {}
        Unvisited_vertexs=[value for value in graph.keys()]
        
        while Unvisited_vertexs:

            minimum=None
            for node in Unvisited_vertexs:
                if None==minimum:
                    minimum=node
                elif minimum_distance[node] < minimum_distance[minimum]:
                    minimum=node

            for neighbor, weight in graph[minimum].items():
                    
                if (minimum_distance[minimum]+weight < minimum_distance[neighbor]):
                    minimum_distance[neighbor]=minimum_distance[minimum]+weight
                    predecessor[neighbor]=minimum
                    
            Unvisited_vertexs.remove(minimum)

        
        return minimum_distance



    help_path=os.path.dirname(__file__)
    file_name=raw_input("")
    graph=ReadPajek(filename=help_path+file_name)

    txt_file=open(file_name.replace("pajek", "txt"), "w")

    for i in range(graph[0]):
        smallest_distances=Dijkstra_Algorithm(graph[1], i+1)
        for distance in smallest_distances.values():
            print(distance, end=" ")
            txt_file.write(str(distance)+" ")
        print('')
        txt_file.write('\n')

    txt_file.close()




main()