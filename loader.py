from importlib import reload
import matplotlib.pyplot as plt

import example_plot


def main():
    plt.show(block=False)
    fig = plt.figure()
    cache = {}  # allow plotter to store data between hot-reload
    while True:
        reload(example_plot)
        fig.clf()
        example_plot.plot(fig, cache)
        fig.show()
        fig.canvas.draw()
        fig.canvas.flush_events()
        com = input("Enter r to reload, q to quit\n")
        if com == 'q':
            break


if __name__ == '__main__':
    main()
