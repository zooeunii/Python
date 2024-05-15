#함수 사용하기
#divmod() 함수를 이용해 -27의 절댓값을 5로 나눈 '몫'과 '나머지'를 변수
#x와 y에 각각 할당한 후 x와 y를 출력한다.
#pow() 함수를 사용해서 x의 제곱을 y로 나눈 나머지 값을 변수 z에 할당한 후 z를 출력
#변수 z를 7로 나눈 후 소수점 3자리로 반올림한 결괏값 출력 

x, y = divmod(abs(-27), 5)
print(x)
print(y)

z = pow(x, 2, y)
print(z)

z /= 7
print(round(z, 3))
