from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 10)

df = data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)
date_increase = df.index[df.Close > df.Open]
date_decrease = df.index[df.Close < df.Open]

p = figure(x_axis_type="datetime", width=1000, height=300)
p.title.text = "Candlestick Chart"

hours_12 = 12*60*60*1000

p.rect(df.index[df.Close > df.Open], (df.Open + df.Close)/2, hours_12, abs(df.Open - df.Close),
       fill_color='green', line_color='black')
p.rect(df.index[df.Close < df.Open], (df.Open + df.Close)/2, hours_12, abs(df.Open - df.Close),
       fill_color='red', line_color='black')

output_file("CS.html")
show(p)


