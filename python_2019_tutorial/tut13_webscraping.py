from bokeh.plotting import output_file,show,figure
import pandas as pd

dataset = pd.read_excel('verlegenhuken.xlsx',sheet_name=0)

dataset['Temperature'] = dataset['Temperature']/10
dataset['Pressure'] = dataset['Pressure']/10

p = figure(plot_width=500,plot_height=400)

p.title.text = 'Temperature and Air pressure'
p.title.text_color = 'Red'
p.title.text_font = 'arial'
p.title.text_font_style = 'bold'
p.xaxis.axis_label = 'Temperature (C)'
p.yaxis.axis_label = 'Pressure (hPa)'


p.circle(dataset['Temperature'],dataset['Pressure'],size=0.1)
output_file('Weather.html')
show(p)


# data = pd.DataFrame(columns=['X','Y'])
#
# data['X'] = [1,2,3,4,5]
# data['Y'] = [1,4,9,16,25]
#
# p = figure(plot_width=500,plot_height=400)
# p.circle(data['X'],data['Y'],size=15)
# output_file('scatter.html')
# show(p)