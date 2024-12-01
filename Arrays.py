def arr(rows, cols):
    arr = [[0 for i in range(cols)] for j in range(rows)]
    return arr

hallo=arr(10, 10)
for i in range(len(hallo)):
    print(i,":")
    for j in range(len(hallo[i])):
        print(hallo[i][j])
else:
    print("Fertig!")
