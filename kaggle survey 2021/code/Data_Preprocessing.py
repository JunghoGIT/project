import pandas as pd
import numpy as np 
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/kaggle_survey_2021_responses.csv')


# 연봉에 대한 문항 결측치 제거
df2 =df.dropna(subset=['Q25'])


# 한중일미 국가에 대한 데이터만 수집
country = ['South Korea','Japan','China','United States of America']
df2 = df2[df2.Q3.isin(country)]


# 분석이 필요한 칼럼만 수집
df2 = df2[['Q1','Q2','Q3','Q4','Q5','Q6','Q25']]

# 인덱스 재설정
df2=df2.reset_index(drop=True)

# 효율적인 분석을 위해 객관식 질의로 표현된 구간에 해당 범위의 난수로 변환
# index를 재설정함으로서 for문을 통한 탐색이 가능하게 함
# 하나의 for문에 elif 문을 사용하여 최대한 연산을 줄이려 노력함.

for i in df2.index :
  if df2.iloc[i]['Q1']=='18-21':
    df2.iloc[i]['Q1']= np.random.randint(18,22)
  
  elif df2.iloc[i]['Q1']=='22-24':
    df2.iloc[i]['Q1']= np.random.randint(22,25)
  
  elif df2.iloc[i]['Q1']=='25-29':
    df2.iloc[i]['Q1']= np.random.randint(25,30)

  elif df2.iloc[i]['Q1']=='30-34':
    df2.iloc[i]['Q1']= np.random.randint(30,35)

  elif df2.iloc[i]['Q1']=='35-39':
    df2.iloc[i]['Q1']= np.random.randint(35,40)

  elif df2.iloc[i]['Q1']=='40-44':
    df2.iloc[i]['Q1']= np.random.randint(40,45)

  elif df2.iloc[i]['Q1']=='45-49':
    df2.iloc[i]['Q1']= np.random.randint(45,50)

  elif df2.iloc[i]['Q1']=='50-54':
    df2.iloc[i]['Q1']= np.random.randint(50,55)

  elif df2.iloc[i]['Q1']=='55-59':
    df2.iloc[i]['Q1']= np.random.randint(55,60)

  elif df2.iloc[i]['Q1']=='60-69':
    df2.iloc[i]['Q1']= np.random.randint(60,70)

  elif df2.iloc[i]['Q1']=='70+':
    df2.iloc[i]['Q1']= 70
  
   

  if df2.iloc[i]['Q6']=='< 1 years':
    df2.iloc[i]['Q6']= 0.5  
  elif df2.iloc[i]['Q6']=='1-3 years':
    df2.iloc[i]['Q6']= np.random.randint(1,4)  
  elif df2.iloc[i]['Q6']=='3-5 years':
    df2.iloc[i]['Q6']= np.random.randint(3,6)  
  elif df2.iloc[i]['Q6']=='5-10 years':
    df2.iloc[i]['Q6']= np.random.randint(5,11)  
  elif df2.iloc[i]['Q6']=='10-20 years':
    df2.iloc[i]['Q6']= np.random.randint(10,21)  
  elif df2.iloc[i]['Q6']=='20+ years':
    df2.iloc[i]['Q6']= np.random.randint(20,30)  
  elif df2.iloc[i]['Q6']=='I have never written code':
    df2.iloc[i]['Q6']= 0 



  if df2.iloc[i]['Q25']=='$0-999':
    df2.iloc[i]['Q25']= np.random.randint(0,1000) 
  elif df2.iloc[i]['Q25']=='1,000-1,999':
    df2.iloc[i]['Q25']= np.random.randint(1000,2000)   
  elif df2.iloc[i]['Q25']=='2,000-2,999':
    df2.iloc[i]['Q25']= np.random.randint(2000,3000)   
  elif df2.iloc[i]['Q25']=='3,000-3,999':
    df2.iloc[i]['Q25']= np.random.randint(3000,4000)   
  elif df2.iloc[i]['Q25']=='4,000-4,999':
    df2.iloc[i]['Q25']= np.random.randint(4000,5000)   
  elif df2.iloc[i]['Q25']=='5,000-7,499':
    df2.iloc[i]['Q25']= np.random.randint(5000,7500)   
  elif df2.iloc[i]['Q25']=='7,500-9,999':
    df2.iloc[i]['Q25']= np.random.randint(7500,10000)   
  elif df2.iloc[i]['Q25']=='10,000-14,999':
    df2.iloc[i]['Q25']= np.random.randint(10000,15000)   
  elif df2.iloc[i]['Q25']=='15,000-19,999':
    df2.iloc[i]['Q25']= np.random.randint(15000,20000)   

  elif df2.iloc[i]['Q25']=='20,000-24,999':
    df2.iloc[i]['Q25']= np.random.randint(20000,25000) 
  elif df2.iloc[i]['Q25']=='25,000-29,999':
    df2.iloc[i]['Q25']= np.random.randint(25000,30000) 
  elif df2.iloc[i]['Q25']=='30,000-39,999':
    df2.iloc[i]['Q25']= np.random.randint(30000,40000) 
  elif df2.iloc[i]['Q25']=='40,000-49,999':
    df2.iloc[i]['Q25']= np.random.randint(40000,50000) 
  elif df2.iloc[i]['Q25']=='50,000-59,999':
    df2.iloc[i]['Q25']= np.random.randint(50000,60000) 
  elif df2.iloc[i]['Q25']=='60,000-69,999':
    df2.iloc[i]['Q25']= np.random.randint(60000,70000) 
  elif df2.iloc[i]['Q25']=='70,000-79,999':
    df2.iloc[i]['Q25']= np.random.randint(70000,80000) 
  elif df2.iloc[i]['Q25']=='80,000-89,999':
    df2.iloc[i]['Q25']= np.random.randint(80000,90000)
  elif df2.iloc[i]['Q25']=='90,000-99,999':
    df2.iloc[i]['Q25']= np.random.randint(90000,100000) 
  elif df2.iloc[i]['Q25']=='100,000-124,999':
    df2.iloc[i]['Q25']= np.random.randint(100000,125000) 
  elif df2.iloc[i]['Q25']=='125,000-149,999':
    df2.iloc[i]['Q25']= np.random.randint(125000,150000) 
  elif df2.iloc[i]['Q25']=='150,000-199,999':
    df2.iloc[i]['Q25']= np.random.randint(150000,200000) 
  elif df2.iloc[i]['Q25']=='200,000-249,999':
    df2.iloc[i]['Q25']= np.random.randint(200000,250000) 
  elif df2.iloc[i]['Q25']=='250,000-299,999':
    df2.iloc[i]['Q25']= np.random.randint(250000,300000)  
  elif df2.iloc[i]['Q25']=='300,000-499,999':
    df2.iloc[i]['Q25']= np.random.randint(300000,500000)  
  elif df2.iloc[i]['Q25']=='$500,000-999,999':
    df2.iloc[i]['Q25']= np.random.randint(500000,1000000)  
  elif df2.iloc[i]['Q25']=='>$1,000,000':
    df2.iloc[i]['Q25']= np.random.randint(1000000,1100000) 


# 학위에 대한 답변을 학력순으로 숫자 부여

df2.loc[df2['Q4']=='Doctoral degree','Q4'] = 5
df2.loc[df2['Q4']=='Professional doctorate','Q4'] = 5
df2.loc[df2['Q4']=='Master’s degree','Q4'] = 4
df2.loc[df2['Q4']=='Bachelor’s degree','Q4'] = 3
df2.loc[df2['Q4']=='Some college/university study without earning a bachelor’s degree','Q4'] = 2
df2.loc[df2['Q4']=='No formal education past high school','Q4'] = 1
df2.loc[df2['Q4']=='I prefer not to answer','Q4'] = 0

# 너무 길게 표현된 미국의 국가명을 약어로 변경

df2.loc[df2['Q3']=='United States of America','Q3'] = 'USA'

# 데이터 저장

df2.to_csv('ppt_df_5.csv')