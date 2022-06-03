def search(input_list, target):
    nums = sorted(input_list)
    print(nums)

    (left, right) = (
        0,
        len(nums) - 1,
    )  # simultaneous assignment of left and right bounds

    while left <= right:

        mid = (left + right) // 2  # rounds down if it's a decimal

        if (
            target == nums[mid]
        ):  # if it finds the target, return the current index
            return mid

        elif target < nums[mid]:  # Target is smaller, discard the right
            right = mid - 1

        else:  # Target is larger, discard the left
            left = mid + 1

    return None
