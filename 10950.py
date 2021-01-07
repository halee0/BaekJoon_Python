def sol(n):
    for i in range(n):
        lines=input()
        nums=lines.split()
        a=int(nums[0].strip())
        b=int(nums[1].strip())
        print(a+b)

n=int(input())
sol(n)