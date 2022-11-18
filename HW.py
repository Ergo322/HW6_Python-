# Первая задача
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for i in list:
    if '+' in i or '-' in i:
        if '+' in i:
            new_list.append('"')
            znak = i.replace('+', '')
            if int(znak) < 10:
                znak = '0' + znak
                i = '+' + znak
            new_list.append(i)
            new_list.append('"')
        if '-' in i:
            new_list.append('"')
            znak = i.replace('-', '')
            if int(znak) < 10:
                znak = '0' + znak
                i = '-' + znak
            new_list.append(i)
            new_list.append('"')
    else:
        if i.isdigit():
            new_list.append('"')
            if int(i) < 10:
                i = '0' + i
            new_list.append(i)
            new_list.append('"')
        else:
            new_list.append(i)
result = ' '.join(new_list)
print(result)

# Вторая задача
list = [57.2, 100.13, 12.6, 545.3, 35.32, 31.3, 56.9, 34.0, 67.45, 98.1, 45.67, 87.4, 34.6, 54.64, 37.4]
list.sort()
# list.sort(reverse= True)
new_list = []
for i in list:
    c = str(i)
    c = c.split(".")[0]
    c = c + ' r'
    new_list.append(c)
    d = round(i % 1, 2)
    d = str(d)
    d = d.split(".")[1]
    if int(d) < 10:
        d = '0' + d
    d = d + ' kk,'
    new_list.append(d)
result = ' '.join(new_list)
print(result)