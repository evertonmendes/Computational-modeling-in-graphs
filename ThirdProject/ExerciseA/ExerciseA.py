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
        archive.readline()

        adjency_list=[0]*n_nodes
        for i in range(len(adjency_list)):
            adjency_list[i]=[]

        for edges in archive:
            
            edges=edges.split()
            adjency_list[int(edges[0])-1].append(int(edges[1]))
            adjency_list[int(edges[1])-1].append(int(edges[0]))

        return n_nodes, adjency_list


    def dfs_all(graph, name_file):

        def dfs(graph, vertex):
            visited.add(vertex)
            for neighbor in graph[1][vertex-1]:
                if neighbor not in visited:
                    dfs(graph, neighbor)

        visited = set()
        previous_lenght=1
        components=[]

        for vertex in range(graph[0]):
        
            if not vertex in visited:
                dfs(graph, vertex)
                components.append(len(visited)-previous_lenght)
                previous_lenght=len(visited)

        components.sort()
        text_file=open(name_file.replace('pajek', 'txt'), 'w')
        text_file.write(str(len(components)))
        print(len(components))
        for value in components[::-1]:
            text_file.write(str(value))
            print(value)

        text_file.close()
         

    
    help_path=os.path.dirname(__file__)
    file_name=raw_input("")
    graph=ReadPajek(filename=help_path+file_name)
    dfs_all(graph=graph, name_file=help_path+file_name)




main()
