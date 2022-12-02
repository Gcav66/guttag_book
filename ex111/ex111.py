import sys

def square_root_exhaustive(x, epsilon):
    """Assumes x and epsilon are positive floats & epsilon < 1
       Returns a y such that y*y is witin epsilon of x"""
    step = epsilon**2
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        ans += step
    if ans*ans > x:
        raise ValueError
    return ans

if __name__ == "__main__":
    x = float(sys.argv[1]) if len(sys.argv) > 1 else 25
    epsilon = float(sys.argv[2] if len(sys.argv) > 2 else 0.1)
    ans = square_root_exhaustive(x, epsilon)
    print(ans)