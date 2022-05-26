from solve import Solver
from read import get_grids

if __name__ == '__main__':
    grids = get_grids()
    solver = Solver(grids[0])
    solver.test()    