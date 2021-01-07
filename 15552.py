import sys

def sol(n):
    for i in range(n):
        nums=sys.stdin.readline().rstrip()
        nums=nums.split(" ")
        a=int(nums[0])
        b=int(nums[1])
        print(a+b)

n=sys.stdin.readline().rstrip()
sol(int(n))