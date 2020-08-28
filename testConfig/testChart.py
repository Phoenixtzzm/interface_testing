# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2020/8/11 16:07'
import plotly
import plotly.graph_objs as go
import numpy as np
N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace1 = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)
random_y2= np.random.randn(N)

trace2 = go.Bar(x = random_x,y = random_y2)
data = [trace1,trace2]

plotly.offline.plot(dict(data=[trace1,trace2]))