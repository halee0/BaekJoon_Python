def show(lines):
    nums=lines.split(" ")
    a=int(nums[0].strip())
    b=int(nums[1].strip())

    print(a+b)
    print(a-b)
    print(a*b)
    print(int(a/b))
    print(a%b)

lines=input()
show(lines)