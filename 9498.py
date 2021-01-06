def sol(score):
    result=None
    if score>=90 and score<=100:
        result="A"
    elif score>=80:
        result="B"
    elif score>=70:
        result="C"
    elif score>=60:
        result="D"
    else:
        result="F"
    print(result)

score=int(input())
sol(score)