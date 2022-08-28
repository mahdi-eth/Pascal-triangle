def pascaler(n):
    arr = [1]
    temp = []
    print(f"Pascal's triangle of {n} rows:")
    for i in range(n):
        print(end= f"row {i+1} : ")
        for j in range(len(arr)):
            print(arr[j], end=" ")
        print()
        temp.append(1)
        for j in range(len(arr)-1):
            temp.append(arr[j] + arr[j+1])
        temp.append(1)
        arr = temp
        temp = []

n = abs(int(input("Enter the number of rows you want to see of Pascal's triangle: ")))
pascaler(n)


