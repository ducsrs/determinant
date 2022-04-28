def det(a: list[list[int | float]]) -> int | float:
    if len(a) == 1:
        return a[0][0]
    else:
        adding = True
        result = 0
        for i in range(len(a)):
            minor = [a[j + 1][:i] + a[j + 1][i + 1:] for j in range(len(a) - 1)]
            if adding:
                result += a[0][i] * det(minor)
            else:
                result -= a[0][i] * det(minor)
            adding = not adding
        return result
