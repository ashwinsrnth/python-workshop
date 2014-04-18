from Tkinter import *
import numpy as np

class Matrix:

    def __init__(self, master, M, N):
     
        self.M = M   
        self.N = N

        self.array = []

        # creation and placement:
        for i in range(self.M*self.N):
            self.array.append(Entry(master, width=5))
            
        for i in range(self.M*self.N):
            x = i%N
            y = i/N
            self.array[i].grid(column = x, row = y)

    def get(self):
        '''
            Return all the values of the matrix as a list
            of strings
        '''
        return [self.array[i].get() for i in range(len(self.array))]
    

class App:
    '''
        Application to display GUI that
        does matrix-vector multiplication
    '''


    def __init__(self, master):

        # space allocation
        self.matrixFrame = Frame(master)
        self.vectorFrame = Frame(master)
        self.resultFrame = Frame(master)

        # fill space with entry boxes:
        self.matrix = Matrix(self.matrixFrame, 2, 2)
        self.vector = Matrix(self.vectorFrame, 2, 1)
        self.result = Matrix(self.resultFrame, 2, 1)

        # make button
        self.button = Button(root, text='MULTIPLY!', command=self.multiply)

        # place widgets:
        self.matrixFrame.grid(row=0,column=0,padx=5,pady=5)
        self.vectorFrame.grid(row=0,column=1,padx=5,pady=5)
        self.button.grid(row=0,column=2,padx=5,pady=5)
        self.resultFrame.grid(row=0,column=3,padx=5,pady=5)

    def multiply(self):

        A = self.matrix.get()
        A = [float(A[i]) for i in range(self.matrix.M*self.matrix.N)]
        A = np.matrix(A)
        A = A.reshape([self.matrix.M, self.matrix.N])

        x = self.vector.get()
        x = [float(x[i]) for i in range(len(x))]
        x = np.matrix(x)
        x = x.reshape([self.vector.M, self.vector.N])

        b = A*x

        for i in range(self.result.M):
            self.result.array[i].delete(0, END)
            self.result.array[i].insert(0, str(b[i,0]))

root = Tk()
app = App(root)
root.mainloop()


