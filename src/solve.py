from rich import print

class Solver:
    
    def __init__(self, grid):
        self.grid = grid
        self.length = len(self.grid)
        self.n = int((self.length)**0.5)
        self.rows = self.grid
        self.columns = [[self.grid[i][j] for i in range(self.length)] for j in range(self.length)]
        self.blocks = [[self.grid[i][j:j+3]+self.grid[i+1][j:j+3]+self.grid[i+2][j:j+3] for j in [0,3,6]] for i in [0,3,6]]
        self.possibilities = {}
        self.numbers = {i for i in range(1,10)}
                  
    def get_possible_values(self):
        for i,row in enumerate(self.grid):
            for j,num in enumerate(row):
                if num==0:
                    self.possibilities[(i,j)]=self.numbers.difference(self.rows[i]).difference(self.columns[j]).difference(self.blocks[i//self.n][j//self.n])
    
    def test(self):
        print(self.grid)
        self.get_possible_values()
        print(self.possibilities)