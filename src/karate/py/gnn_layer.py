import numpy as np


def glorot_init(n_inputs, n_outputs):
    sd = np.sqrt(6.0 / (n_inputs + n_outputs))
    return np.random.uniform(-sd, sd, (n_inputs, n_outputs))


class GNNLayer():
    def __init__(self, n_inputs, n_outputs, activation = None, name = ''):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.W = glorot_init(self.n_outputs, self.n_inputs)
        self.activation = activation
        self.name = name

    def __repr__(self):
        return f"GCN: W{'_'+self.name if self.name else ''} ({self.n_inputs}, {self.n_outputs})"
        
    def forward(self, A, X, W=None):
        print("Forward")

        self._A = A
        self._X = (A @ X).T # (n_inputs, n_nodes) @ (n_nodes, n_nodes) -> (n_inputs, n_nodes) Message Passing

        if W is None:
            W = self.W

        H = W @ self._X # (n_outputs, n_inputs) @ (n_inputs, n_nodes) -> (n_outputs, n_nodes) Linear Transformation

        if self.activation is not None:
            H = self.activation(H)
        self._H

    def backward(self, optim, update=True):
        print("Backward")