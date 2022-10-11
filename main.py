import matplotlib.pyplot as plt
import numpy as np

class input():
    def __init__(self,mini:float,maxi:float):
        self.minimum = mini
        self.maximum = maxi
        self.sections = {}

    def add_section(self,nodes:list,name:str):
        if len(nodes) == 3:
            self.sections[name] = nodes

        elif len(nodes) == 4:
            self.sections[name] = nodes

        else :
            raise TypeError("too many or too few elements in list")


    def draw_input(self):
        plt.figure()

        for k,v in enumerate(self.sections):
            print(v)
            if len(self.sections[v]) == 3:
                y1 = [0, 1, 0]
                plt.plot(self.sections[v], y1,label = v)
            if len(self.sections[v]) == 4:
                y2 = [0, 1, 1, 0]
                plt.plot(self.sections[v],y2,label = v)

        plt.xlim([self.minimum,self.maximum])
        plt.legend()
        plt.show()

    def __and__(self,other):
        print(np.interp(6,self.sections['poor1'],y2))
        return # dwie

    def __or__(self, other):



input1 = input(0,10)
input1.add_section([0,1,2,3],'poor')
input1.add_section([2,3,4,5],'avg')
input1.add_section([4,6,8,10],'good')
#print(input1.sections)
input1.draw_input()











