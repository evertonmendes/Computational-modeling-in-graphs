#Name: Éverton Luís Mendes da Silva
#N USP: 10728171

import matplotlib.pyplot as plt
import numpy as np
import random
import itertools



class Erdos_Renyi_model():

    def __init__(self , nodes=0, probability=0, matrix=[], AdjList=[]):

        self.nodes=nodes
        self.probability=probability
        self.matrix=matrix
        self.AdjList=AdjList
        self.Initialize()

    #create G(n, p) matrix using nodes and probability
    def CreateMatrix(self):


        all_combinations=list(itertools.combinations(range(self.nodes), 2))
        self.matrix=np.zeros(shape=(self.nodes,self.nodes))
        
        for edgeA, edgeB in all_combinations:

            probability_experiment=random.random()

            if (probability_experiment<self.probability):

                self.matrix[edgeA][edgeB]=1
                self.matrix[edgeB][edgeA]=1
    
    #create a Adjency List by matrix
    def CreateAdjList(self):

        self.AdjList=[]

        for i in range(self.nodes):

            neighborsList=[]
            neighbors=self.matrix[i]
            for index, value in enumerate(neighbors):

                if (value==1):
                    neighborsList.append(index)

            self.AdjList.append(neighborsList)

    #get the degree of a node    
    def VertexDegree(self, vertex):

        try:
            degree_number=len(self.AdjList[vertex])
        
        except IndexError:
            print("Error: The number have to respect 0<=vertex<=number_vertex")
            return

        return degree_number


    #Initialize the matrix and the AdjList using nodes and probability
    def Initialize(self):

        self.CreateMatrix()
        self.CreateAdjList()





