import numpy as np
import matplotlib.pyplot as plt

pop1 = 2
pop2 = 1
empty = 0

t = 0.3

#for i in range(100):
    
#   print(grid)

size = 5

grid = np.random.choice([pop1, pop2, empty], size=(size, size), p=[0.45, 0.45, 0.1])
print(grid)

fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='viridis')

plt.ion() # Enable interactive mode
plt.show()

for i in range(size):
    for j in range(size):
        if grid[i][j] != 0:
            neighbors = []
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < size and 0 <= nj < size:
                        neighbors.append(grid[ni][nj])
            #print(f"Cell ({i}, {j}) has neighbors: {neighbors}")

            print(f"Cell ({i}, {j}) has neighbors: {neighbors}")

            same_type = neighbors.count(grid[i][j])
            if grid[i][j] == pop1:
                other_type = pop2
            else:
                other_type = pop1

            different_type = neighbors.count(other_type)

            #total_neighbors = len(neighbors)

            percentage_same = same_type / different_type if different_type > 0 else 1.0

            if percentage_same < t:
                #print(f"Cell ({i}, {j}) is unhappy with {percentage_same:.2f} similar neighbors.")
                for a in range(size):
                    for b in range(size):
                        if grid[a][b] == 0:
                            grid[a][b] = grid[i][j]
                            grid[i][j] = 0

                            break

                    else:
                        continue
                    break

                im.set_data(grid)
                plt.draw()
                plt.pause(0.01)  # Pause to update the plot
'''
plt.imshow(grid, cmap='viridis')
plt.colorbar()
plt.title("Initial Grid")
plt.show()

'''
plt.ioff()                     # Turn off interactive mode
plt.show(block=True)    




