import math


def jaccard(l1, l2):
    intersection = len(list(set(l1).intersection(l2)))
    union = (len(l1) + len(l2)) - intersection
    return float(intersection) / union


def Euclidean(l1, l2):
    tmp = 0.0
    for i, e in enumerate(l1):
        tmp += (e - l2[i]) ** 2
    return math.sqrt(tmp)


def main():
    x1 = [1, 1, 1, 1, 1]
    x2 = [1, 1, 1, 0, 0]
    y1 = [0, 0, 0, 0, 0]
    y2 = [0, 0, 0, 1, 1]
    print("jaccard(x1, x2): {}".format(jaccard(x1, x2)))
    print("jaccard(y1, y2): {}".format(jaccard(y1, y2)))
    print("Euclidean(x1, x2): {}".format(Euclidean(x1, x2)))
    print("Euclidean(y1, y2): {}".format(Euclidean(y1, y2)))


if __name__ == "__main__":
    main()
