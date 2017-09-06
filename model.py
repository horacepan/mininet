from layers import *
import pdb

class Sequential(object):
    def __init__(self, *layers):
        self._layers = []

        for l in layers:
            self.add(l)

    def add(self, layer):
        # TODO: do some checking to make sure the layer fits the right dimensions
        self._layers.append(layer)

    def forward(self, input):
        val = input
        for l in self._layers:
            val = l.forward(val)

        return val

    def backward(self, loss):
        pass

    def __call__(self, input):
        self.forward(input)

    def __repr__(self):
        layers =  map(lambda (ind, x): '  ({}): {}'.format(ind, x.__repr__()),
                      enumerate(self._layers))
        _repr = ['Model ('] + layers + [')']
        return '\n'.join(_repr)

if __name__ == '__main__':
    x = Sequential(
        Linear(in_dim=5, out_dim=10),
        ReLU(),
        Linear(in_dim=10, out_dim=1),
        ReLU()
    )
    print x
