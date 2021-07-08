#Name: Éverton Luís Mendes da Silva
#NºUSP: 10728171

import os

def main():


    def ReadPajek(filename):

        
        archive=open(filename, "r")
            
        aux=archive.readline().split()
        n_nodes=aux[1]
        n_nodes=int(n_nodes)

        #Drop the string information 'Edges'
        archive.readline()

        adjency_list=[0]*n_nodes
        for i in range(len(adjency_list)):
            adjency_list[i]=[]

        for edges in archive:
                
            edges=edges.split()
            adjency_list[int(edges[0])-1].append(int(edges[1]))
            adjency_list[int(edges[1])-1].append(int(edges[0]))

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


    help_path=os.path.dirname(__file__)

    archive_out=open(help_path+"/resposta.out", "w")

    case_in=input()
    graph= ReadPajek(help_path+case_in)

    n_vertex=graph[0]

    for i in range(n_vertex):
        for j in range(n_vertex):

            bfs_value=str(bfs(graph, i+1, j+1))
            archive_out.write(bfs_value+" ")
            print(bfs_value, end=" ")
            
        print()
        archive_out.write("\n")



    archive_out.close()
    




#initialize the main function
main()