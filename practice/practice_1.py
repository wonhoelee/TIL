# 개
#print('|\_/|\n|q p|   /}\n( 0 )\"\"\"\ \n|\"^\"`   |\n||_/=\\__|')


# 사칙연산
#두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램

# a ,b = map(int,input().split())
# print (a+b)
# print (a-b)
# print (a*b)
# print (a/b)
# print (a%b)

# 나머지
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

#https://www.acmicpc.net/problem/2588 문제

# a = input()
# b = input()

# print(int(a)* int(b[2]))
# print(int(a)* int(b[1]))
# print(int(a)* int(b[0]))
# print(int(a)* int(b[2])+(int(a)* int(b[1])*10)+(int(a)* int(b[0]))*100)