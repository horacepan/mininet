import numpy as np

class Layer(object):
    def forward(self, input):
        pass

    def back(self, grad_output):
        pass

    def __repr__(self):
        raise NotImplementedError

class Linear(Layer):
    def __init__(self, in_dim, out_dim):
        self._in_dim = in_dim
        self._out_dim = in_dim
        self._w = np.random.random()
        self._bias = np.random.random(out_dim)

    def forward(self, input):
        return self._w.dot(input) + self._bias

    def backward(self, grad_output):
        pass

    def __repr__(self):
        return 'Linear ({} -> {})'.format(self._in_dim, self._out_dim)

class ReLU(Layer):
    def __init__(self):
        pass

    def forward(self, input):
        pass
    def __repr__(self):
        return 'ReLU'

class Tanh(Layer):
    def __init__(self):
        pass

    def forward(self, input):
        pass
    def __repr__(self):
        return 'tanh'

class Sigmoid(Layer):
    def __init__(self):
        pass

    def forward(self, input):
        pass

    def __repr__(self):
        return 'Sigmoid'
