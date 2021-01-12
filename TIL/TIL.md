# Today I Learned Cake!

## A piece of Cake
- pandas dataframe 통채로 plot에 넣었는데 데이터 타입이 string이었는데도 그림 그려지기 때문에 데이터 타입 확인하고 astype('')으로 숫자형으로 바꿔주기
    - ASCII로 변환되어서인가? 
- 상관계수와 결정계수는 다름
    - 선형회귀분석에서는 상관계수를 제곱해 결정계수로 사용하지만 결정계수를 다르게 계산하는 경우도 있음
    - 선형회귀에서 결정계수는 귀무가설과 대립가설의 인과관계의 유의미한 정도를 수치화시킴
    - 자세한건 다음에 다시 다루기 (참조 : https://m.blog.naver.com/istech7/50153288534)
- python에서 reshape(-1, 1)를 하라는 에러는 입력 함수가 2D array형태를 요구하는지 확인하기
    - reshape(-1, 1)의 의미는 row는 어떤지 모르겠고, column은 1이니 길이 맞춰서 정리해라! 라는 뜻
    - 결과적으로 column이 1개인 2D matrix 화 됨
- 입출력이 제한적인 솔루션의 경우 Finite State Machine(FSM)을 통해 안정성 확보가 가능함
    - 참조 : https://ozt88.tistory.com/8
- 경고 처리 : SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
    - 참조 : https://emilkwak.github.io/pandas-dataframe-settingwithcopywarning
- pandas DataFrame 복사할 때 deep copy 별도로 써줘야 됨
- pandas DataFrame 조건부 인덱싱
    - 예시 : pred.loc[pred['0SRF_Cha1'] >= thresh, '0SRF_Dis1'] = overThresh_Dis_mean
   