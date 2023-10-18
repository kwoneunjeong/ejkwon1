'''표준 체중을 구하는 프로그램을 작성하세요.

• 표준 체중: 키에 따른 평균 체중

• 성별에 따른 표준 체중 공식

남자: 키(m) × 키(m) × 22

여자: 키(m) × 키(m) × 21
'''


def std_weight(height, gender): #표준 체중 계산 함수 정의 
    if gender =="남자":
        return height *height *22
    else:
        return height*height *21
height = 175
gender= "남자"
weight =round(std_weight(height /100,gender), 2)
    
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight)) 
