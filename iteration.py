from matplotlib import pyplot as plt

def rauber_beute(x, **kwargs):
    x_elem = list(x)
    assert(len(x_elem) == 2)
    a = kwargs.get('a')
    b = kwargs.get('b')
    c = kwargs.get('c')
    d = kwargs.get('d')
    H = x[0]
    L = x[1]
    H = H+a*H-b*H*L
    L = L-c*L+d*H*L
    return [H, L]
    


def iteration(f, x=[0, 0], n=10, **kwargs):
    x_elem = list(x)
    x_list = [x_elem]
    for i in range(n):
        x_elem = f(x_elem, **kwargs)
        x_list.append(x_elem)
        # if x_list[-1] < 20:
        #     print("Bedingung erfüllt für Element x" + str(i))
    return x_list


def plot_iteration(func, x0=[0, 0], n=10, **kwargs):
    x_list = iteration(func, x0, n, **kwargs)
    plt.plot(x_list)
    plt.show()
