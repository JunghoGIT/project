import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Output, Input

# 데이터 불러오기
data = pd.read_csv('data\Bitcoin.csv')

data['날짜'] = data['날짜'].str.replace(pat=r'[^A-Za-z0-9]', repl=r'-', regex=True)
data['거래량'] = data['거래량'].str.replace('K', '')
data['거래량'] = data['거래량'].str.replace('M', '')
data['날짜'] = pd.to_datetime(data['날짜'], format="%Y--%m--%d-")
data=data.sort_index(ascending=False)


print(data.head())

# dash 클래스로 app 인스턴스 생성
app = dash.Dash(__name__)




fig1 = go.Figure(data=[go.Candlestick(
    x=data['날짜'],
    open=data['오픈'], high=data['고가'],
    low=data['저가'], close=data['종가'],
    increasing_line_color= 'red', decreasing_line_color= 'blue'
)])


app.layout = html.Div(

    children=[
 html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.날짜.min().date(),
                            max_date_allowed=data.날짜.max().date(),
							initial_visible_month=data.날짜.min().date(),
                            start_date=data.날짜.min().date(),
                            end_date=data.날짜.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.H1(children="Bitcoin",),
        html.P(
            children="1일 가격 선 그래프",
        ),
        # 그래프
        dcc.Graph(id="candlestick-chart", figure=fig1),
        dcc.Graph(id="chart",
            figure={
                "data": [
                    {
                        "x": data["날짜"],
                        "y": data["종가"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "최근 1년간 비트코인 가격 변동 선 그래프"},
            },
        )

    ]
)

@app.callback(
    [Output("candlestick-chart", "figure"), Output("chart", "figure")],
    [
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(start_date, end_date):
    mask = (
       (data.날짜 >= start_date) & (data.날짜 <= end_date)
    )
    filtered_data = data.loc[mask, :]
    fig2 = go.Figure(data=[go.Candlestick(
        x=filtered_data['날짜'],
        open=filtered_data['오픈'], high=filtered_data['고가'],
        low=filtered_data['저가'], close=filtered_data['종가'],
        increasing_line_color='red', decreasing_line_color='blue'
    )])
    candlestick_chart_figure = fig2

    chart_figure = {
                "data": [
                    {
                        "x": filtered_data["날짜"],
                        "y": filtered_data["종가"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "최근 1년간 비트코인 가격 변동 선 그래프"},
            }

    return candlestick_chart_figure, chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)


