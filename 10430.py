def show(lines):
    nums=lines.split(" ")
    a=int(nums[0].strip())
    b=int(nums[1].strip())
    c=int(nums[2].strip())

    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print((a%c)*(b%c)%c)

lines=input()
show(lines)