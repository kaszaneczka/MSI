import matplotlib.pyplot as plt
import numpy as np

class input():
    def __init__(self,mini:float,maxi:float):
        self.minimum = mini
        self.maximum = maxi
        self.sections = {}

    def __getitem__(self, index:str):
        return self.sections[index]

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

            if len(self.sections[v]) == 3:
                y1 = [0, 1, 0]
                plt.plot(self.sections[v], y1,label = v)
            if len(self.sections[v]) == 4:
                y2 = [0, 1, 1, 0]
                plt.plot(self.sections[v],y2,label = v)

        plt.xlim([self.minimum,self.maximum])
        plt.legend()


class ctrl():
    def __init__(self):
        self.inputy = []
        self.warunki = []
        self.outy = []
        self.y = [[0,1,0],[0,1,1,0]]
        self.pomoc2 = []
        self.wyjscie = []
    def rule(self,inputy: list,warunki:list,wartosc : float):
        self.inputy.append(inputy)
        self.warunki.append(warunki)
        self.outy.append(wartosc)
    def compute(self,input:list = [2,3.2]):
        self.up = 0
        self.down = 0
        for a in self.inputy:
            self.pomoc = []
            for b,c in enumerate(a):
                if len(c) == 3:
                    y = [0,1,0]
                    self.pomoc.append(np.interp(input[b],c,y))
                if len(c) == 4:
                    y = [0,1,1,0]
                    self.pomoc.append(np.interp(input[b],c,y))
            self.pomoc2.append(self.pomoc)

        for a in range(len(self.warunki)):
            for b in range(len(self.warunki[a])):
                    if self.warunki[a][0] == 'and':
                        self.pomoc2[a].insert(0,sorted(self.pomoc2[a][b:b+2])[0])
                        self.pomoc2[a].pop(b+1)
                        if b < 1:
                            self.pomoc2[a].pop(b+1)
                    if self.warunki[a][0] == 'or':
                        self.pomoc2[a].insert(0, sorted(self.pomoc2[a][b:b + 2])[-1])
                        self.pomoc2[a].pop(b + 1)
                        if b<1:
                            self.pomoc2[a].pop(b+1)
            self.wyjscie.append(self.pomoc2[a][0])



        for a in range(len(self.wyjscie)):
            self.up += self.wyjscie[a]*self.outy[a]
            self.down += self.wyjscie[a]
            print(self.wyjscie[a],self.outy[a], self.wyjscie[a])
        return self.up/self.down





ctrl=ctrl()
input1 = input(0,10)
input2 = input(0,10)
input3 = input(0,5)

input1.add_section([0,0,3,4],'poor')
input1.add_section([3,4,5,6],'avg')
input1.add_section([5,6,10,10.1],'good')

input2.add_section([0,0,3,4],'poor')
input2.add_section([3,4,5,6],'avg')
input2.add_section([5,6,10,10.1],'good')

# input3.add_section([0,0,1,3],'poor')
# input3.add_section([1,3,3.5,4],'avg')
# input3.add_section([3,4.5,5,5],'good')

ctrl.rule([input1['poor'],input2['poor']],['and'],0)
ctrl.rule([input1['poor'],input2['avg']],['and'],1)
ctrl.rule([input1['poor'],input2['good']],['and'],4)

ctrl.rule([input1['avg'],input2['poor']],['and'],1)
ctrl.rule([input1['avg'],input2['avg']],['and'],3)
ctrl.rule([input1['avg'],input2['good']],['and'],4)

ctrl.rule([input1['good'],input2['poor']],['and'],5)
ctrl.rule([input1['good'],input2['avg']],['and'],7)
ctrl.rule([input1['good'],input2['good']],['and'],10)


input1.draw_input()

input2.draw_input()
plt.show()
print(ctrl.compute([10,10]))



#print(np.interp(6,self.sections['poor1'],y2))














