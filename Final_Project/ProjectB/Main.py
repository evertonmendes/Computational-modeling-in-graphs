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



    help_path=os.path.dirname(__file__)
    file_name=input()
    graph=ReadPajek(filename=help_path+"/"+file_name)

    count_sink=0
    for neighbors in graph[1]:
        if len(neighbors)==0:
            count_sink+=1

    print(count_sink)



Main()