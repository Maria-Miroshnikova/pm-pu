import numpy as np
import matplotlib.pyplot as plt

def time_scaling_5(T):
    a = [0, 0, 0, 10/T**3, -15/T**4, 6/T**5]
    t = np.arange(0, T, T/20)
    s = a[0] + a[1] * t + a[2] * t**2 + a[3] * t**3 + a[4] * t**4 + a[5] * t**5
    ds = a[1] + 2 * a[2] * t + 3 * a[3] * t**2 + 4 * a[4] * t**3 + 5 * a[5] * t**4
    dds = 2 * a[2] + 6 * a[3] * t + 12 * a[4] * t**2 + 20 * a[5] * t**3
    plt.plot(t, s)
    plt.title("s(t): fifth-order polynomial time scaling")
    plt.xlabel("Values of t")
    plt.ylabel("Values of s")
    plt.show()

    plt.plot(t, ds)
    plt.title("ds(t): fifth-order polynomial time scaling")
    plt.xlabel("Values of t")
    plt.ylabel("Values of ds")
    plt.show()

    plt.plot(t, dds)
    plt.title("dds(t): fifth-order polynomial time scaling")
    plt.xlabel("Values of t")
    plt.ylabel("Values of dds")
    plt.show()

time_scaling_5(10)