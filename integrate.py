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
        return """
        Summary for simpson method
        Lower bound (a) = {}
        Upper bound (b) = {}
        Segment (n)     = {}
        Function        = {}
        """.format(shared_property.a, shared_property.b, shared_property.n, shared_property.func)

    def calculate_trapezoid():
        a = int(shared_property.a)
        b = int(shared_property.b)
        n = int(shared_property.n)
        eval_func = str(shared_property.func)
        fn = "f0 "
        result_list = list()
        result = 0
        func = lambda x: eval(eval_func)
        
        h = (b - a) / n
        n_segment = np.arange(a, b+h, h)
        res = list(map(func, n_segment))

        for i in range(len(n_segment)):
            print("f{} = {}".format(i, res[i]))
            if((i>0) and (i<n)):
                fn = fn + "+ 2f{} ".format(i)
                result_list.append(2*res[i])

        result_list.insert(0, res[0])
        result_list.append(res[-1])
        result = (h/2)*(sum(result_list))

        fn = fn + "+ f{}".format(n)

        actual_result, error = integrate.quad(func, a, b)

        realtive_error = 100 * (abs(result - actual_result) / actual_result)

        return """
        Result  = {}
        I       = {}
        Error   = {} %
        """.format(result, fn, realtive_error)
        

class simpson(shared_property):
    def simpson_summary():
        return """
        Summary for simpson method
        Lower bound (a) = {}
        Upper bound (b) = {}
        Segment (n)     = {}
        Function        = {}
        """.format(shared_property.a, shared_property.b, shared_property.n, shared_property.func)

    def calculate_simpson():
        a = int(shared_property.a)
        b = int(shared_property.b)
        n = int(shared_property.n)
        eval_func = str(shared_property.func)
        fn = "f0 "
        result_list = list()
        result = 0
        func = lambda x: eval(eval_func)

        h = (b - a) / n
        n_segment = np.arange(a, b+h, h)
        res = list(map(func, n_segment))

        for i in range(len(n_segment)):
            print("f{} = {}".format(i, res[i]))
            if((i>=1) and (i%2!=0) and (i<n)):
                fn =  fn + "+ 4f{} ".format(i)
                result_list.append(4*res[i])
            elif((i>=2) and (i%2==0) and (i!=n)):
                fn =  fn + "+ 2f{} ".format(i)
                result_list.append(2*res[i])
        
        result_list.insert(0, res[0])
        result_list.append(res[-1])
        result = (h/3)*(sum(result_list))

        fn = fn + "+ f{}".format(n)
    
        actual_result, error = integrate.quad(func, a, b)

        realtive_error = 100 * (abs(result - actual_result) / actual_result)

        return """
        Result  = {}
        I       = {}
        Error   = {} %
        """.format(result, fn, realtive_error)
"""
values below are examples for exception handling

try:
    func = lambda x : eval(str("(2*a**4) + (4*x**2)"))
    res = func(0)
    print(res)
except NameError:
    print("Expression should be written in x")
"""
"""
shared_property.func = "(2*x**4) + (4*x**2)"
shared_property.a = 1
shared_property.b = 3
shared_property.n = 4
res = trapezoid.calculate_trapezoid()
print(res)
func = lambda x: (2*x**4) + (4*x**2)
res, err = integrate.quad(func, 1, 3)
print(res)
print(err)
trapezoid result : 136.125
simpson resilt : 131.5
"""