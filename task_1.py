time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_split = time.split(',') 
print(time_split)

minutes = 0

for i in time_split:
    time_replaced = i.replace('h', ' ').replace('m', ' ').replace('s', ' ').split()
    print(time_replaced)
    
    if 'h' in i and 's' in i:
        # Часы + секунды (например: '2h 60s')
        minutes += int(time_replaced[0]) * 60  # часы
        minutes += int(time_replaced[1]) // 60  # секунды
    elif 'h' in i:
        # Часы + минуты (например: '1h 45m')
        minutes += int(time_replaced[0]) * 60  # часы
        minutes += int(time_replaced[1])  # минуты
    elif 'm' in i and 's' in i:
        # Минуты + секунды (например: '30m 120s')
        minutes += int(time_replaced[0])  # минуты
        minutes += int(time_replaced[1]) // 60  # секунды
    elif 's' in i:
        # Только секунды
        minutes += int(time_replaced[0]) // 60
    else:
        # Только минуты
        minutes += int(time_replaced[0])

print("Общее количество минут:", minutes)