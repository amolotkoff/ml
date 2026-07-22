import math

def linear(xs, ys):
    a = 0
    b = 0
    n = 0.01

    def loss():
        nonlocal a, b, n
        da = 0
        db = 0
        error = 0
        for i in range(len(xs)):
            x = xs[i]
            y = ys[i]
            yp = a * x + b
            err = y - yp
            da += x * err
            db += err
            error += math.pow(err, 2)
        da *= (-2/len(xs))
        db *= (-2/len(xs))
        a -= n * da
        b -= n * db
        error /= len(xs)
        return error, a, b

    return loss

def quadratic(xs, ys):
    a = 0
    b = 0
    c = 0
    n = 0.0001

    def loss():
        nonlocal a, b, c, n
        da = 0
        db = 0
        dc = 0
        error = 0
        for i in range(len(xs)):
            x = xs[i]
            y = ys[i]
            yp = a * x**2 + b * x + c
            err = y - yp
            da += -2 * err * x**2
            db += -2 * err * x
            dc += -2 * err
            error += math.pow(err, 2)
        da /= len(xs)
        db /= len(xs)
        dc /= len(xs)
        a -= n * da
        b -= n * db
        c -= n * dc
        error /= len(xs)
        return error, a, b, c

    return loss

def polynomial(xs, ys, power):
    a = [0] * (power + 1)
    n = 0.0001

    def loss():
        nonlocal a, n
        da = [0] * (power + 1)
        error = 0
        for i in range(len(xs)):
            x = xs[i]
            y = ys[i]
            yp = 0
            for j in range(power):
                yp += a[j]*(x**j)
            err = y - yp
            for j in range(power):
                da[j] += -2 * err * (x**j)
            error += math.pow(err, 2)
        for i in range(power):
            da[i] /= len(xs)
            a[i] -= n * da[i]
        error /= len(xs)
        return error, a

    return loss
