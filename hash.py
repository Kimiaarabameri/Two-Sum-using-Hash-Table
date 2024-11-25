def FindTwoSum(nums, target):
    seen = set()  # مجموعه ای که اعداد در ان ذخیره میشوند
    for num in nums:
        complement = target - num
        if complement in seen:
            return num, complement
        seen.add(num)
    return None  # اگر هیچ جفتی پیدا نشد


# تست
numbers = [2, 10, 11, 15]
target = 12
result = FindTwoSum(numbers, target)

if result:
    print(f"numbers : {result[0]}  {result[1]}")
else:
    print("not found")

