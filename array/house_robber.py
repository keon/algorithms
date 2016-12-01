def house_robber(houses):
    last, now = 0, 0
    for house in houses:
        tmp = now
        now = max(last + house, now)
        last = tmp
    return now

houses = [1, 2, 16, 3, 15, 3, 12, 1]

print(house_robber(houses))
