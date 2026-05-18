def is_isomorphic(s, t):

    if len(s) != len(t):
        return False

    d1 = {}
    d2 = {}

    for a, b in zip(s, t):

        if a in d1:
            if d1[a] != b:
                return False
        else:
            d1[a] = b

        if b in d2:
            if d2[b] != a:
                return False
        else:
            d2[b] = a

    return True


s = "paper"
t = "title"

print(is_isomorphic(s, t))
