import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

# 데이터 불러오기
data = pd.read_csv('data\Bitcoin.csv')
data['coinname'] = 'BTC'
data2 = pd.read_csv('data\Ethereum.csv')
data2['coinname'] = 'ETH'

data=data.append(data2)


data['날짜'] = data['날짜'].str.replace(pat=r'[^A-Za-z0-9]', repl=r'-', regex=True)
data['거래량'] = data['거래량'].str.replace(pat=r'[^0-9]', repl=r'', regex=True)
data['날짜'] = pd.to_datetime(data['날짜'], format="%Y--%m--%d-")

data=data.sort_values(by=['coinname','날짜'])

data=data.reset_index(drop=True)

# dash 클래스로 app 인스턴스 생성
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "JH's first dashboard"
server = app.server



fig1 = go.Figure(data=[go.Candlestick(
    x=data['날짜'],
    open=data['오픈'], high=data['고가'],
    low=data['저가'], close=data['종가'],
    increasing_line_color= 'red', decreasing_line_color= 'blue'
)])


app.layout = html.Div(

    children=[

        html.Div(children=[
            html.H1(children="Bitcoin & Ethereum",style={"fontSize": "50px", "text-align": "center","padding-top" :"50px"}, className='header_title' ),
            html.P(
                children="1일 가격과 거래량",style={"fontSize": "30px", "text-align": "center"},className='header_description'
            )
        ],className='header'
        ),
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
                    ],className="menu_date"
                ),
                html.Div(
                    children=[
                        html.Div(children="BTC or ETH", className="menu-title"),
                        dcc.Dropdown(
                            id="coin-name",
                            options=[
                                {"label": "BTC", "value": "BTC"},
                                {"label": "ETH", "value": "ETH"}
                            ],
                            value="BTC",
                            clearable=False,

                        ),
                    ],className="menu_coin",
                ),
            ],
            className="menu",
        ),
        # 그래프
        html.Div(
            children=[
                dcc.Graph(id="candlestick-chart", figure=fig1),
                dcc.Graph(id="chart",
                          figure={
                              "data": [
                                  {
                                      "x": data["날짜"],
                                      "y": data["거래량"],
                                      "type": "lines",
                                  },
                              ],
                              "layout": {"title": "거래량 선 그래프"},
                          },
                          )
            ],className="chart"
        )

    ],className="index"
)

@app.callback(
    [dash.dependencies.Output("candlestick-chart", "figure"), dash.dependencies.Output("chart", "figure")],
    [
        dash.dependencies.Input("coin-name", "value"),
        dash.dependencies.Input("date-range", "start_date"),
        dash.dependencies.Input("date-range", "end_date"),
    ],
)
def update_charts(coin_name, start_date, end_date):
    mask = (
            (data.날짜 >= start_date) & (data.날짜 <= end_date) & (data.coinname == coin_name)
    )
    filtered_data = data.loc[mask, :]

    fig1 = go.Figure(data=[go.Candlestick(
        x=filtered_data['날짜'],
        open=filtered_data['오픈'], high=filtered_data['고가'],
        low=filtered_data['저가'], close=filtered_data['종가'],
        increasing_line_color='red', decreasing_line_color='blue'
    )])

    candlestick_chart_figure = fig1
    fig1.update_layout(title={'text' : "1일 가격 차트",
                              'y':0.9,
                              'x':0.5,
                              'xanchor': 'center',
                              'yanchor': 'top'},
                       xaxis_title="날짜",
                       yaxis_title="가격",
                       height = 700,
                       paper_bgcolor = '#4D4D4D',
                       font_color= "#FFFFFF",
                       plot_bgcolor= '#525252')


    chart_figure = {
        "data": [
            {
                "x": filtered_data["날짜"],
                "y": filtered_data["거래량"],
                "type": "lines",
            },
        ],
        "layout": {"title": {"text" :"거래량 선 그래프"},
                   "xaxis":{"title":"날짜"},
                   "yaxis":{"title":"거래량"},
                   "height" : "300",
                   "paper_bgcolor": "#4D4D4D",
                   "font": {"color":"#FFFFFF"},
                   "plot_bgcolor": "#525252",
                   }
    }

    return candlestick_chart_figure, chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)


