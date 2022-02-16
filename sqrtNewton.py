def sqrtNewton(n):
    e = 0.0001
    x = n
    root = 0.5 * (x + (n/x))
    check = 0
    while check != 1:
        root = 0.5 * (x + (n/x))
        if abs(root-x) < e:
            check = 1
        x = root
    return root

#next_guess: root
#last_guess: x
