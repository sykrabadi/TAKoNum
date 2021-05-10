class error(shared_property):
	str_func = "(2*a*4) + (4*x*2)"
	a = 1
	b = 3
	n = 4

	if isinstance(a, str):
		print("Lower bound be number")

	if isinstance(b, str):
		print("Upper bound should be number")
	try:
	    func = lambda x : eval(str_func)
	    res = integrate(func, 1, 3)
	except TypeError:
	    print("Expression should be written in x")
