def power(darshaka):
    def inner(base):
        return pow(base,darshaka)
    return inner

a=power(2)


print(a(5))
cube=power(3)

print(cube(1))
print(cube(2))
print(cube(3))
print(cube(4))