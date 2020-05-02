def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this_hour, this_min = l[index]
            prev_hour, prev_min = l[index - 1]

            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue

            l[index] = (prev_hour, prev_min)
            l[index - 1] = (this_hour, this_min)


def bubble_sort_2(l):
    i = 0
    n = len(l)
    while i < n:
        j = 0
        while j < n-1:
            this_hour, this_min = l[j]
            next_hour, next_min = l[j + 1]
            if this_hour < next_hour or (this_hour == next_hour and this_min < next_min):
                l[j] = (next_hour, next_min)
                l[j + 1] = (this_hour, this_min)
            j += 1
        i = 0
        n -= 1


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def test(func):
    func(sleep_times)
    print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")


test(bubble_sort_1)
test(bubble_sort_2)
