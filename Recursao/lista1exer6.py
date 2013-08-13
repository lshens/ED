__author__ = 'lucas.shen'
def ff(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return ff(n / 2)
    else:
        return ff((n-1)/2) + ff((n+1)/2)

print(ff(7))