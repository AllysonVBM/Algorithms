def gnome_sort(v):
    i = 1
    n = len(v)
    while i < n:
        if i == 0 or v[i-1] <= v[i]:
            i += 1
        else:
            v[i], v[i-1] = v[i-1], v[i]
            i -= 1
    return v

if __name__ == "__main__":
    a = [34, 2, 10, -9]
    b = [5, 4, 3, 2, 1]
    c = [1, 2, 3, 4, 5]
    d = []
    print(gnome_sort(a) == sorted(a))
    print(gnome_sort(b) == sorted(b))
    print(gnome_sort(c) == sorted(c))
    print(gnome_sort(d) == sorted(d))
