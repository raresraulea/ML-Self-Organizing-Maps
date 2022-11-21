from matplotlib import pyplot as plt

import constants
from Point import Point

from pltUtils import config_plt, display_plot_with_data, put_data_on_plot
from randomGenerators import generate_random_number_of_centroids, colors, yPoints, xPoints

points = []

with open('../GenerareDate/data.txt') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split()
        points.append(Point(float(words[0]), float(words[1])))
    if len(colors) == 0:
        colors = list(map(lambda l: constants.zones[int(l.split()[2])][2], lines))

if len(xPoints) == 0:
    xPoints = list(map(lambda p: p.x, points))
    yPoints = list(map(lambda p: p.y, points))


def get_neighbours(row, col, grid):
    result = []
    # if row == 0 or row == (len(grid) - 1) or col == 0 or col == (len(grid[0]) - 1):
    if row != 0:
        result.append([row - 1, col])
    if col != 0:
        result.append([row, col - 1])
    if row != (len(grid) - 1):
        result.append([row + 1, col])
    if col != (len(grid) - 1):
        result.append([row, col + 1])
    return result


neurons_x_points = []
neurons_y_points = []
neurons_colors = []
neuron_grid = []
diff = 0.6666666
print(diff)
for i in range(-300, 301, int(600/9)):
    neuron_row = []
    for j in range(-300, 301, int(600/9)):
        neuron_row.append([i + diff, j + diff])
        neurons_x_points.append(i + diff)
        neurons_y_points.append(j + diff)
        neurons_colors.append('blue')
    neuron_grid.append(neuron_row)

config_plt()
print(neuron_grid)

for i in range(0, len(neuron_grid)):
    for j in range(0, len(neuron_grid[0])):
        neighbours = get_neighbours(i, j, neuron_grid)
        current_point = [neuron_grid[i][j][0], neuron_grid[i][j][1]]
        for n in neighbours:
            neighbour_x = n[0]
            neighbour_y = n[1]
            x_values = [current_point[0], neuron_grid[neighbour_x][neighbour_y][0]]
            y_values = [current_point[1], neuron_grid[neighbour_x][neighbour_y][1]]
            plt.plot(x_values, y_values, 'bo', linestyle="--")


put_data_on_plot(neurons_x_points, neurons_y_points, neurons_colors)
put_data_on_plot(xPoints, yPoints, colors)

plt.show()

