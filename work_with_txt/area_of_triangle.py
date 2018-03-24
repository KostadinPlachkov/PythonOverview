import math

def main():
    try:
        user_input()
    except:
        print("INVALID INPUT")


def user_input():

        a = float(input())
        b = float(input())
        c = float(input())
        calc_triangle_area(a, b, c)



def calc_triangle_area(a, b, c):
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    if S == 0.0:
        print("INVALID INPUT")
    else:
        print("{:.2f}".format(S))

if __name__ == '__main__':
    main()