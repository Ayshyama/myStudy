# 09.05.23
# Task - Combine lists into a dict




color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']

colors = dict(zip(color_names, color_hex))
print(colors)
print(colors['green'])