from typing import List

def predict_y(x: float, weight: float, bias: float):
    return x * weight + bias

def mse_loss_function(x: List[float], y: List[float], weight: float, bias: float):
    loss = 0.0
    number_data_points = len(x)

    for i in range(number_data_points):
        loss += (y[i] - predict_y(x[i], weight, bias))**2

    return loss / number_data_points

def update_params(x: List[float], y: List[float], weight: float, bias: float, learning_rate: float):
    weight_derivative = 0.0
    bias_derivate = 0.0
    number_data_points = len(x)

    for i in range(number_data_points):
        y_hat = predict_y(x[i], weight, bias)
        weight_derivative += -2 * x[i] * (y[i] - y_hat)
        bias_derivate += -2 * (y[i] - y_hat)
    
    weight -= learning_rate * weight_derivative
    bias -= learning_rate * bias_derivate
    return weight, bias

def train(x: List[float], y: List[float], learning_rate: float, n_iter: int):
    assert len(x) == len(y), 'The vectors must be same length. Currently, len(x)={} len(y)={}'.format(len(x), len(y))
    weight = 0.0
    bias = 1.0
    
    for _ in range(n_iter):
        print(weight, bias)
        weight, bias = update_params(x, y, weight, bias, learning_rate)
    
    return weight, bias
