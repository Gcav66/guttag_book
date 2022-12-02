import os


from exhaust_enum import square_root_exhaustive

def get_input():
    x = float(os.environ['X'])
    epsilon = float(os.environ['EPSILON'])
    return x, epsilon

def run():
    x, epsilon = get_input()
    ans = square_root_exhaustive(x, epsilon)
    print(f'x: {x}')
    print(f'epsilon: {epsilon}')
    print(f'answer: {ans}')
    return ans

if __name__ == '__main__':
    run()
