# This will not work even though list gets concatenated
some_tuple = (1, 2, [30, 40])
some_tuple[2] += [50, 60]