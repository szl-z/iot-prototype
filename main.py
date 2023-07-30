from chart_studio.tools import set_credentials_file
from config import (
  PLOTLY_USERNAME,
  PLOTLY_API_KEY
)
from pandas import DataFrame
import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as py
import json

set_credentials_file(
  username = PLOTLY_API_KEY,
  api_key = PLOTLY_API_KEY
)

def parse_data(data) -> pd.DataFrame:
#  sound_df = pd.read_json(data)
  sound_df = pd.DataFrame(data)
  sound_df.set_index(keys=sound_df['timestamp'], inplace=True)
  return sound_df

def create_chart(sound_df: DataFrame) -> py.plot:
  fig = go.Figure(data=[
    go.Bar(
      x=sound_df.index,
      y=sound_df.soundLevel
    )
  ])
  fig.show()
  chart = py.plot(
    fig,
    filename=symbol,
    auto_open=False,
    fileopt='overwrite',
    sharing='public'
  )
  return chart

f = open('generated_sound_data.json')
data = json.load(f)
sound_df = parse_data(data)
print(create_chart(sound_df))
