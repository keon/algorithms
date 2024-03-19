import tqdm
import numpy as np
np.random.seed(0)

from network import Network
from layer import Linear, Sigmoid, ReLU, PReLU
from loss import SSE
from optimizer import GradientDescent

hidden_layer = Linear(2, 2, "hidden", True)
output_layer = Linear(2, 1, "output", True)
loss = SSE()
optimizer = GradientDescent(0.1)

def main():
    debug = False
    xs = [[1., 1], [1., 2], [2., 1], [2., 2]]
    ys = [[1.], [2.], [2.], [1.]]

    net = Network([hidden_layer, Sigmoid(), output_layer])

    # for layer in net.get_layers():
    #     print(layer.get_params())

    with tqdm.trange(2000) as t:
        for epoch in t:
            epoch_loss = 0.0
            for x, y in zip(xs, ys):
                x = np.array(x).reshape(-1, 1)
                pred = net.forward(x, debug)
                epoch_loss += loss.loss(pred, y, debug)
                grad = loss.gradient(pred, y, debug)
                grad = np.array(grad).reshape(-1, 1)
                net.backward(grad, debug)
                optimizer.step(net, debug)
            t.set_description(f"xor loss {epoch_loss:.3f}")

    for layer in net.get_layers():
        print(layer.get_params())

main()