def solution(nums: list, target: int) -> list:
    for i in range(len(nums)):
        test_num = nums[i]
        test_list = nums[:i] + nums[i+1:]
        diff = target - test_num
        print(f'{test_num} + {diff} = {target} : {test_list}')
        if diff in test_list:
            i_2 = test_list.index(diff)
            return [i, i_2+1]
    # return test_nums


