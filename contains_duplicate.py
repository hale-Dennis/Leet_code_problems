
nums = [1,2,3,1]

def containsdubplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(nums)
    return False


if containsdubplicate(nums):
    print("contains duplicates")

