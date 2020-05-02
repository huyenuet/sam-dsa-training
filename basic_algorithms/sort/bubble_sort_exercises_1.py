def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this


def bubble_sort_2(ls):
    if len(ls) == 1 or 0:
        return ls
    j = 0
    n = len(ls)
    while j < n:
        i = 0
        while i < n - 1:
            if ls[i] > ls[i + 1]:
                temp = ls[i]
                ls[i] = ls[i + 1]
                ls[i + 1] = temp
            i += 1
        j = 0
        n -= 1

    return ls


wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]


def test(func):
    func(wakeup_times)
    print("Pass" if (wakeup_times == [3, 9, 12, 13, 13, 16, 19, 22, 25, 45, 46, 46, 48, 49, 49, 55, 55, 56, 56]) else "Fail")


test(bubble_sort_1)
test(bubble_sort_2)
