# Task 6
color_dict = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}
sorted_color_dict = {k: color_dict[k] for k in sorted(color_dict)}
for key, value in sorted_color_dict.items():
    print(f"{key}: {value}")