numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_cnt = 0
for num in numbers:
    if num > 0:
        positive_num_cnt += 1
print("Final count of positive number : ", positive_num_cnt)