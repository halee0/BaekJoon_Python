def sol(hour,min):
    if min>=45:
        min-=45
    else:
        if hour>0:
            hour-=1
        else:
            hour=hour+24-1
        min = min + 60 - 45
    return hour,min

lines=input()
nums=lines.split(" ")
hour=int(nums[0].strip())
min=int(nums[1].strip())
calc_hour, calc_min=sol(hour,min)
print(calc_hour,calc_min)