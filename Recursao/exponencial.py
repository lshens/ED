__author__ = 'lucas.shen'
def expo(k, n):
    if n == 0:
        return 1
    if n == 1:
        return k
    else:
        return k * expo(k, n - 1)
print(expo(10, 3))