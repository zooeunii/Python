#좋아하는 계절과 태어난 날짜 출력하기
season = input('좋아하는 계절은 무엇인가요')        #input() 함수로 변수 season에 값을 할당한다.
print(season)       #변수 season을 출력한다.

data = input('며칠에 태어났나요?')      #input() 함수를 사용해 변수 data에 값을 할당한다. 
data = int(data)        #data의 값을 정수로 변환한 후 data에 재할당한다.
print(data)     #변수 data의 자료형을 출력한다.

#하나의 문자로 결합해서 결과를 출력한다.
print('좋아하는 계절은' + season + '이고, ' + str(data) + '일에 태어났습니다.')

