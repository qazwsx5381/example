a = 100
result = 0
for i in range(1,3):
   result = a >> i
   # a >> n은 a를 2^n으로 나눈 정수 몫과 같습니다.
   result = result + 1
print(result)