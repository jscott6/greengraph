
#!usr/bin/env python

from argparse import ArgumentParser
from matplotlib import pyplot as plt
from ggraph import Greengraph

# execute iff we are on command line
if __name__ == "__main__":
    parser = ArgumentParser(description = "Run Greengraph from command line")
    parser.add_argument('--begin', '-b', type = str)
    parser.add_argument('--end', '-e', type = str)
    parser.add_argument('--steps','-s', type = int)
    parser.add_argument('--out', '-o')
    arguments = parser.parse_args()

    mygraph = Greengraph(arguments.begin, arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    plt.savefig(args.out)
