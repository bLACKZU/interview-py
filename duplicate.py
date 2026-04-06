# Apple - Return true if any value appears at least twice in the array, and return false if every element is distinct.
def contains_duplicate(nums: list[int]) -> bool:
    # write code here
    count = 0
    dup_list = []
    if len(nums) != 0:
        for i in nums:
            if i in dup_list:
                dup_list.append(i)
                count = dup_list.count(i)
                if count == 2:
                    return True
            else:
                dup_list.append(i)
                if len(nums) == len(dup_list):
                    return False
    else:
        return False
            