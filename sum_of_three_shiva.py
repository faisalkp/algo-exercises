arr = [10, 1, 3, 4, 5]

required_sum = 13

arr.sort()

arr_len = len(arr)

for i in range(0, arr_len - 2):
    first = i + 1
    last = arr_len - 1

    while first < last:
        intermediate_sum = arr[i] + arr[first] + arr[last]
        if intermediate_sum == required_sum:
            print "{0} {1} {2}".format(arr[i], arr[first], arr[last])
            exit()
        elif intermediate_sum < required_sum:
            first += 1
        else:
            last -= 1

print "Not possible with the given input..."
