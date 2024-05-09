#이름과 내년 나이 출력하기
name = input('이름을 입력하세요...: ')      #input() 함수를 사용해 변수 name에 값을 할당한다.
print('안녕', name)                        #인사말을 출력한다.

age = input('몇 살이세요? ')               #input() 함수를 사용해 변수 age에 값을 할당한다.
print('내년에' + str(int(age) + 1) + '살이 되시는군요.')      #문자열을 결합해서 출력한다.
print('Bye~~~!')
