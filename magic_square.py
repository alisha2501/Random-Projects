def magic_sq(n):
    magicSq = [[0 for _ in range(n)] for _ in range(n)]


    i = n // 2
    j = n - 1
    num = n * n
    count = 1

    while count <= num:
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
        if magicSq[i][j] != 0:
            j = j - 2
            i = i + 1
            continue
        else:

            magicSq[i][j] = count
            count += 1

        i = i - 1
        j = j + 1


    for row in magicSq:
        for val in row:
            print(val, end=" ")
        print()

    print("The sum of each row/column/diagonal is: " + str((n * (n**2 + 1)) // 2))

magic_sq(7)