

if __name__ == '__main__':
    lines = 20
    arr = []
    for q in range(lines):
        if q == 0:
            arr.append([1])
        elif q == 1:
            arr.append([1, 1])
        else:
            new_arr = []
            for i in range(len(arr[-1]) + 1):
                if (i == 0) | (i == len(arr[-1])):
                    new_arr.append(1)
                else:
                    new_arr.append(arr[-1][i - 1] + arr[-1][i])
            arr.append(new_arr)
    for q in arr:
        print(q)