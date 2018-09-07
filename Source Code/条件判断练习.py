a=input("请输入身高\n")
b=input("请输入体重\n")
h=float(a)
w=float(b)
bmi= w/(h*h)
if bmi<18.5:
     print("您的bmi系数为%.2f"%bmi,"身体状况为过轻")
elif bmi>18.5 and bmi<25:
     print("您的bmi系数为%.2f"%bmi,"身体状况为正常")
elif bmi>25 and bmi<28:
     print("您的bmi系数为%.2f"%bmi,"身体状况为过重")
elif bmi>28 and bmi<32:
     print("您的bmi系数为%.2f"%bmi,"身体状况为肥胖")
else:
     print("您的bmi系数为%.2f"%bmi,"身体状况为重度肥胖")