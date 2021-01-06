def div(lines):
    nums=lines.split(" ")
    a=int(nums[0].strip())
    b=int(nums[1].strip())
    return a/b

lines=input()
print(div(lines))