def foo(x):
    return x*3

def user_input():
    x = input('Enter a number: ')
    return x

res = foo( user_input() )

print(res)