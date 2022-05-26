from rich import print

class Solver:
    
    def __init__(self, grid):
        self.grid = grid
        self.length = len(self.grid)
        self.n = int((self.length)**0.5)
        self.rows = [set(row).difference({0}) for row in self.grid]
        self.columns = [{self.grid[i][j] for i in range(self.length)}.difference({0}) for j in range(self.length)]
        self.blocks = [[set(self.grid[i][j:j+3]).union(self.grid[i+1][j:j+3]).union(self.grid[i+2][j:j+3]).difference({0}) for j in [0,3,6]] for i in [0,3,6]]
        self.numbers = {i for i in range(1,10)}
        self.possibilities = {}
        self.done_sure = False
        self.update_possibilities()
                  
    def update_possibilities(self):
        for i,row in enumerate(self.grid):
            for j,num in enumerate(row):
                if num==0:
                    self.possibilities[(i,j)]=self.numbers.difference(self.rows[i]).difference(self.columns[j]).difference(self.blocks[i//self.n][j//self.n])

    def fill_sure(self):
        self.done_sure = True
        for i,j in self.possibilities:
            values = self.possibilities[(i, j)]
            if values is not None and len(values)==1:
                self.done_sure = False
                (value, ) = values
                self.grid[i][j] = value
                self.possibilities[(i, j)] = None
                self.rows[i].add(value)
                self.columns[j].add(value)
                self.blocks[i//self.n][j//self.n].add(value)
                self.update_possibilities()

    def test(self):
        print(self.grid)
        while not self.done_sure:
            self.fill_sure()
        print(self.grid)