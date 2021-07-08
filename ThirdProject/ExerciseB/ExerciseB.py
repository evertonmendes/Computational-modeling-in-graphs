#Name: Éverton Luís Mendes da Silva
#NºUSP: 10728171

import os

def main():

    def ReadPajek(filename=''):

        archive= open(filename, 'r')
        
        aux=archive.readline().split()
        n_nodes=aux[1]
        n_nodes=int(n_nodes)

        #Drop the string information 'Edges'
        type_of_graph=archive.readline()

        adjency_list=[0]*n_nodes
        for i in range(len(adjency_list)):
            adjency_list[i]=[]


        if type_of_graph=="*Edges":

            for edges in archive:
            
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

    
    def Find_cycle(graph, name_file):

        color = {}
        parent = {}

        for value in range(graph[0]):
            color[str(value+1)] = 'White'
            parent[str(value+1)] = None

        def dfs(vertex, color):
            color[str(vertex)] = "Red"
            for neighbor in graph[1][vertex-1]:
                if color[str(neighbor)] == 'White':
                    parent[str(neighbor)] = vertex
                    dfs(neighbor, color)

                elif color[str(neighbor)] == "Red" and parent[str(vertex)]!=neighbor:
                    return True
            
            color[str(vertex)] = "Black"
            return False

        cycle = False
        parent[str(1)]=-1
        for n_vertex in range(graph[0]):
            if color[str(n_vertex+1)] == 'White':
                cycle = dfs(n_vertex+1, color)
                if cycle == True:
                    break

            
        txt_file=open(name_file.replace("pajek", "txt"), "w")
        if cycle==True:
            txt_file.write("S")
            print("S")
        else:
            txt_file.write("N")
            print("N")

        txt_file.close()
        

    
    help_path=os.path.dirname(__file__)
    file_name=raw_input("")
    graph=ReadPajek(filename=help_path+file_name)
    Find_cycle(graph=graph, name_file=help_path+file_name)
    

main()