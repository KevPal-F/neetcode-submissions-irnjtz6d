class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = 0
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        queue = []

        def getAdjacent(i, j):
            specDir = []
            print(f"Added {i, j} ")


            for i2, j2 in directions:
                x = i2 + i
                y = j2 + j
                if x < 0 or x >= len(grid): continue 
                if y < 0 or y >= len(grid[0]): continue
                if (x, y) in queue: continue

                if grid[x][y] == 1:
                    grid[x][y] = 2
                    specDir.append((x,y))
                print(f"Found adjacent {x, y}")


            return specDir

        # search the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))

        while queue:
            temp = []
            for (i, j) in queue:
                temp.extend(getAdjacent(i, j))
            if temp: t += 1

            queue = temp

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return t

