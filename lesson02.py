#if문
#등호가 왼쩍에 붇는다.
# score = int(input("점수 입력: "))
# if score >= 90:
#     print("학정: A")
# elif 80 <= score < 90:
#     print("학점: B")
# elif 70 <= score < 80:
#     print("학점: C")
# else:
#     print("학점: F")
#인터프리터 번역 순서
#위에서부터 아래로 가면서 번

#while문
# count = 1
# while count <= 100:
#     print("Hello world")
#     count += 1

# num = 0
# while True: #무한루프 boolean타입 첫 글자 대문자로 쓴다.
#     num += 1
#     if num % 2 == 1:
#         continue
#     print(num)
#     if num == 20:
#         break

#for문
# for i in ["one", "two", "three"]:
#     print(i)

#함수 입출력

def add(a, b):
    return a + b
print(add(10, 20))
