def ReadPajek(filename=''):

    archive= open(filename, 'r')
    
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