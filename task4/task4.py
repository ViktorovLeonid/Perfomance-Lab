import sys
from pathlib import Path


nums = list(map(int, Path(sys.argv[1]).read_text().split()))

nums.sort()
median = nums[len(nums) // 2]

moves = sum(abs(num - median) for num in nums)

if moves <= 20:
    print(moves)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")