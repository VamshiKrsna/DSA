def PascalII(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        row.append(1)
        for j in range(len(row)-2,0,-1):
            row[j] = row[j] + row[j-1]
    print(row)


if __name__ == '__main__':
    PascalII(4)