from sympy import symbols, diff, Abs, Interval

def two_conditions(g, interval):
    x = symbols("x")

    g1 = diff(g, x)
    print(g1)

    g_discontinuous_points = [point for point in interval.boundary if g.subs(x, point).is_real is False]
    g1_discontinuous_points = [point for point in interval.boundary if g1.subs(x, point).is_real is False]

    if len(g_discontinuous_points and g1_discontinuous_points) == 0:
        print("The function is continuous in the interval", interval)
        g1_condition_met = all(Abs(g1.subs(x, point)) < 1 for point in interval.boundary)
        if g1_condition_met:
            print("The condition |g'(x)| < 1 is satisfied for every x in the interval", interval)
            return True
        else:
            print("The condition |g'(x)| < 1 is not satisfied for every x in the interval", interval)
            return False
    else:
        print("The function or its equivalent is not continuous in the interval", interval)
        return False
    
    
