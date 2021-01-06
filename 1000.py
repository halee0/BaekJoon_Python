def add(lines):
    nums=lines.split(" ")
    a=nums[0].strip()
    b=nums[1].strip()
    return int(a)+int(b)

lines=input()
result=add(lines)
print(result)