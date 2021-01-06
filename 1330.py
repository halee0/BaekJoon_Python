def sol(lines):
    nums=lines.split(" ")
    a=int(nums[0].strip())
    b=int(nums[1].strip())
    if a>b:
        print(">")
    elif a<b:
        print("<")
    else:
        print("==")

lines=input()
sol(lines)