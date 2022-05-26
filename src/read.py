def get_grids():
    with open("data/sudokus.txt") as f:
        a = [ele.strip() for ele in f.readlines()]
        
    str_list = [a[i+1:i+10] for i,ele in enumerate(a) if 'Grid' in ele]
    grids=[]
    for grid in str_list:
        g = []
        for row in grid:
            g.append(list(map(int, list(row))))
        grids.append(g)
    return grids