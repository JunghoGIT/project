import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Output, Input

# 데이터 불러오기
data = pd.read_csv('data\Bitcoin.csv')
data['coinname'] = 'BTC'
data2 = pd.read_csv('data\Ethereum.csv')
data2['coinname'] = 'ETH'

data=data.append(data2)


data['날짜'] = data['날짜'].str.replace(pat=r'[^A-Za-z0-9]', repl=r'-', regex=True)
data['날짜'] = pd.to_datetime(data['날짜'], format="%Y--%m--%d-")
data=data.sort_values(by=['coinname','날짜'])


data=data.reset_index(drop=True)

# data=data.sort_index(ascending=False)



print(data.info())


