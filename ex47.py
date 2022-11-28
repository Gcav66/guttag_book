def find_root(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
       epsilon > 0 & power >= 1
       Retrns float y such that y**power is withing epsilon of x.
       If such a float does not exist, it returns None"""
    # Find interval containing answer
    if x < 0 and power%2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    # use bisection search
    ans = (high + low)/2
    while abs(ans**power -x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans
