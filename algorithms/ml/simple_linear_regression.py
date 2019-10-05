from typing import List, Tuple

def predict_y(x: float, weight: float, bias: float) -> float:
    """Helper function to calculate y
    
    Arguments:
        x {float}
        weight {float}
        bias {float}
    
    Returns:
        float -- calculated y value
    """
    return x * weight + bias

def mse_loss_function(x: List[float], y: List[float], weight: float, bias: float) -> float:
    """Helper function to see progression of loss with number of iterations
    
    Arguments:
        x {List[float]}
        y {List[float]}
        weight {float}
        bias {float}
    
    Returns:
        float -- mean square loss at any given point using passed weight and bias
    """
    loss = 0.0
    number_data_points = len(x)

    for i in range(number_data_points):
        loss += (y[i] - predict_y(x[i], weight, bias))**2

    return loss / number_data_points

def update_params(x: List[float], y: List[float], weight: float, bias: float, learning_rate: float) -> Tuple[float, float]:
    """Helper function to update weight and bias terms
    
    Arguments:
        x {List[float]}
        y {List[float]}
        weight {float}
        bias {float}
        learning_rate {float}
    
    Returns:
        Tuple[float, float] -- updated weight and bias terms after current iteration
    """
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

def train(x: List[float], y: List[float], learning_rate: float, n_iter: int) -> Tuple[float, float]:
    """Generate the weight and bias using linear regression for a set of
    data points and corresponding values provided
    
    Arguments:
        x {List[float]} -- List of x values
        y {List[float]} -- Corresponding list of y values
        learning_rate {float} -- Learning rate for the weight updates
        n_iter {int} -- Number of iterations to run the algorithm for
    
    Returns:
        Tuple[float, float] -- updated weight and bias for the given data points
    """
    assert len(x) == len(y), 'The vectors must be same length. Currently, len(x)={} len(y)={}'.format(len(x), len(y))
    weight = 0.0
    bias = 1.0
    
    for _ in range(n_iter):
        weight, bias = update_params(x, y, weight, bias, learning_rate)
    
    return weight, bias
