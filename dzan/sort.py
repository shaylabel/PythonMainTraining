def find_max_sum(numbers, res=[0, 0]):
    for i in range(0, 2):
        for number in numbers :
            if number > res[i]:
                res[i] = number

        numbers.remove(res[i])

    return res[0] + res[1]



if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))
    print(find_max_sum([5, 9, 25, 7, 11]))
    print(find_max_sum([25, 9, 12, 7, 17]))
