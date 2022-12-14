from matplotlib import pyplot as plt
from randomGenerators import colors, xPoints, yPoints
import constants


def config_plt():
    plt.rcParams["figure.figsize"] = [10, 7]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    plt.axis([constants.xAxisMin, constants.xAxisMax, constants.yAxisMin, constants.yAxisMax])


def put_data_on_plot(x_axis_points=xPoints, y_axis_points=yPoints, point_colors=colors):
    for i in range(0, len(x_axis_points)):
        plt.scatter(x_axis_points[i], y_axis_points[i], c=point_colors[i], s=20, linewidth=0)


def display_plot_with_data(x_axis_points=xPoints, y_axis_points=yPoints, point_colors=colors):
    for i in range(0, len(x_axis_points)):
        plt.scatter(x_axis_points[i], y_axis_points[i], c=point_colors[i], s=20, linewidth=0)
    plt.show()
