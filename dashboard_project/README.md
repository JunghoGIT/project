# Dash 를 이용하여 Dashboard 만들기





## 목표 



- anaconda로 가상환경을 구축한 후, 가상환경에서 dash를 이용해 dashboard를 구현하고 flask 기반으로 서버에 배포까지 하는 것을 목표로 한다.





## 주제 



- 2020/10/29 ~ 2021/11/29 기간의 BTC, ETC 캔들차트 구현





## 과정



- **가상환경 구축**
  - anaconda 프롬포트를 이용하여 구축
  - 해당 가상환경에 필요한 패키지, 라이브러리 설치
- **데이터 수집**
  - [인베스팅닷컴](https://kr.investing.com/) 에서 과거 BTC, ETC 가격 데이터 수집
- **데이터 전처리**
  - dashboard에 interactive 를 구현하는 것을 목표로 데이터 전처리
    - BTC, ETC 두개로 나눠져 있던 데이터프레임을 하나로 결합
    - object 형식의 날짜 데이터를 datetime 형식으로 변경
    - 거래량에서 숫자 값을 제외 한 모든 문자 제거
    - 코인 종류와 날짜 순으로 정렬 
    - 중복된 인덱스를 제거하기 위해 인덱스 리셋
- **HTML 작성**
  - dash 의 dash_html_components(as HTML) 을 이용하여 기본 틀을 구성
- **데이터 시각화 및 interactive component 구성**
  - dash의 dash_core_components(as dcc) 을 이용하여 plotly 시각화 그래프 추가 
  - dcc 를 이용하여 메뉴 생성
- **Reactive Programming**
  - @app.callback 데코레이터를 이용하여 reactive programming 구현
- **꾸미기**
  - 각 요소들을 HTML 클래스로 지정하여 style.css 파일 안에서 css 코드로 수정
  - 그래프 layout 커스텀
- **배포**
  - heroku를 통한 배포







## 수정 내역



- **1차 수정**

  - HTML 구성 변경

  - 기본적인 css 설정
  - reactive programming 구현











