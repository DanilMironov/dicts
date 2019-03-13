import matplotlib.pyplot as plot


class Painter:
    def __init__(self, data):
        self.data = data
        self.colors = {'LinearArrayDict': 'red',
                       'BinaryArrayDict': 'purple',
                       'TreeDict': 'green',
                       'BalancedTreeDict': 'blue',
                       'HashTableDict': 'yellow',
                       'StandardDict': 'black'}

    def draw(self):
        plot.clf()
        for operation in self.data:
            plot.clf()
            for name in self.data[operation]:
                current_dict = self.data[operation][name]
                plot.plot(current_dict.keys(),
                          [current_dict[key] for key in current_dict.keys()],
                          self.colors[name])
            plot.savefig(operation + '_' + 'result.png')
