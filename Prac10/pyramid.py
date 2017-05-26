def build_pyramid(n):
    total = n
    i = 1
    for block in range(n):
        total += n-i
        i += 1
    return total

print(build_pyramid(6))


def build_pyramid_recursive(n):
    if n == 1:
        return 1
    else:
        return n + build_pyramid_recursive(n-1)


print((build_pyramid_recursive(6)))