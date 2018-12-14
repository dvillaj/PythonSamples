import statistics as stats

data = [1, 2, 2, 5, 10, 12, 1000]
funcs = [("Mean", stats.mean),
    ("Mode", stats.mode),
    ("Median", stats.median),
    ("Median Low", stats.median_low),
    ("Median High", stats.median_high),
    ("Length", len),
    ("Min", min),
    ("Max", max),
    ("Standard Deviation", stats.stdev),
    ("Popultation Standard Deviation", stats.pstdev),
    ("Population Variance", stats.pvariance),
    ("Variance", stats.variance)]

max_n = max(map(lambda x: len(x[0]), funcs)) 
clean_funcs = map(lambda f: (f[0], f[1], {})  if len(f) == 2 else f, funcs)

print("Data: ", data)

for f_str, f, params in clean_funcs:
    print('{text:{n}s} : {calc:0.2f}'.format(
        n = max_n, 
        text = f_str, 
        calc = f(data, **params)))