import scipy
import numpy as np
from scipy import integrate
"""
kode di bawah untuk mencari nilai integral menggunakan pengintegralan biasa
func = (2*x**4) + (4*x**2)
res = integrate.quad(func, 1, 3)
print(res)
"""

class shared_property:
    func = None
    a = None
    b = None
    n = None

class trapezoid(shared_property):
    def trapezoid_summary():
        print("""
        Summar for trapezoid method
        Lower bound (a) = {}
        Upper bound (b) = {}
        Segment (n) = {}
        Funcion = {}
        """.format(shared_property.a, shared_property.b, shared_property.n, shared_property.func)) 

    def calculate_trapezoid():
        func = lambda x: eval(shared_property.func)

        result_list = list()
        result = 0
        h = (shared_property.b - shared_property.a) / shared_property.n

        fn = "f0 "

        n_segment = np.arange(shared_property.a, shared_property.b+h, h)
        res = list(map(func, n_segment))

        for i in range(len(n_segment)):
            print("f{} = {}".format(i, res[i]))

class simpson(shared_property):
    def simpson_summary():
        print("""
        Summar for simpson method
        Lower bound (a) = {}
        Upper bound (b) = {}
        Segment (n) = {}
        Funcion = {}
        """.format(shared_property.a, shared_property.b, shared_property.n, shared_property.func)) 

    def calculate_simpson():
        func = lambda x: eval(shared_property.func)

        result_list = list()
        result = 0
        h = (shared_property.b - shared_property.a) / shared_property.n

        fn = "f0 "

        n_segment = np.arange(shared_property.a, shared_property.b+h, h)
        res = list(map(func, n_segment))

        for i in range(len(n_segment)):
            print("f{} = {}".format(i, res[i]))
            if((i>=1) and (i%2!=0) and (i!=shared_property.n)):
                fn =  fn + "+ 4f{} ".format(i)
                result_list.append(4*res[i])
            elif((i>=2) and (i%2==0) and (i!=shared_property.n)):
                fn =  fn + "+ 2f{} ".format(i)
                result_list.append(2*res[i])
        
        result_list.insert(0, res[0])
        result_list.append(res[-1])
        result = (h/3)*(sum(result_list))

        fn = fn + "+ f{}".format(shared_property.n)
        print("I = {}".format(fn))
        print("Hasil : {}".format(result))
        print(result_list)

shared_property.func = "x**2"
shared_property.a = 2
shared_property.b = 5
shared_property.n = 3

trapezoid.trapezoid_summary()