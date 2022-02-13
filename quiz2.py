import statistics

# equal frequency
def equifreq(arr1, m):
    a = len(arr1)
    n = int(a / m)
    for i in range(0, m):
        arr = []
        for j in range(i * n, (i + 1) * n):
            if j >= a:
                break
            arr = arr + [arr1[j]]
        print(arr)

# equal width
def equiwidth(arr1, m):
    a = len(arr1)
    w = int((max(arr1) - min(arr1)) / m)
    min1 = min(arr1)
    arr = []
    for i in range(0, m + 1):
        arr = arr + [min1 + w * i]
    arri=[]

    for i in range(0, m):
        temp = []
        for j in arr1:
            if j >= arr[i] and j <= arr[i+1]:
                temp += [j]
        arri += [temp]
    print(arri)


def main():
    original_data_set = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
    original_data_set = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]
    d_mean = statistics.mean(original_data_set)
    d_stdev = statistics.stdev(original_data_set)

    print("equal frequency binning")
    m = 3
    equifreq(original_data_set, m)

    print("\n\nequal width binning")
    equiwidth(original_data_set, m)

    a_data_set = [x - d_mean for x in original_data_set]
    print("\n\n", a_data_set)
    print("equal frequency binning")
    m = 3
    equifreq(a_data_set, m)

    print("\n\nequal width binning")
    equiwidth(a_data_set, m)

    b_data_set = [(x - d_mean)/2 for x in original_data_set]
    print("\n\n", b_data_set)

    print("equal frequency binning")
    m = 3
    equifreq(b_data_set, m)

    print("\n\nequal width binning")
    equiwidth(b_data_set, m)


if __name__ == "__main__":
    main()
