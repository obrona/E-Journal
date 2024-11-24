def f(g):
    return lambda x: g(x + 1)



def g(x):
    return 2 * x

h = f(g)


file = open('advice.txt', 'r')
print(file)
for i in range(20):
    text = file.readline()
    print(text)
    