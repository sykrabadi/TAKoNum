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
   def __init__(self, a, b, n, func):
       self.func = None
       self.a = None
       self.b = None
       self.n = None

class trapezoid(shared_property):
    pass

class simpson(shared_property):
    pass

#kode di bawah untuk mencari nilai integral menggunakan metode simpson 1/3
str_func = "(2*x**4) + (4*x**2)"
func = lambda x: eval(str_func)
result_list = list()
result = 0
a = 1
b = 3
n = 4
h = (b-a) / n
fn = "f0 "

n_segment = np.arange(a, b+h, h)
res = list(map(func, n_segment))

#untuk print pola rumus
for i in range(len(n_segment)):
    print("Indeks i : {}, nilainya {}".format(i, res[i]))
    if((i>=1) and (i%2!=0) and (i!=n)):
        fn =  fn + "+ 4f{} ".format(i)
        result_list.append(4*res[i])
    elif((i>=2) and (i%2==0) and (i!=n)):
        fn =  fn + "+ 2f{} ".format(i)
        result_list.append(2*res[i])

result_list.insert(0, res[0])
result_list.append(res[4])
result = (h/3)*(sum(result_list))
print(result_list)
print("Hasil pengintegralan metode simposon : {}".format(result))

fn = fn + "+ f{}".format(n)
print("Rumus simpson untuk n = {} adalah : {}".format(n, fn))