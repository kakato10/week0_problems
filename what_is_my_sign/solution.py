def what_is_my_sign(day, month):
    months = {1: 21 , 2: 20,
    3: 21 , 4: 21 , 5: 22 , 6: 22 ,
    7: 23 , 8: 23 , 9: 24 , 10: 24 , 11: 23 , 12: 22}
    if day < months[month]:
        if month == 1:
            month = 12
        else: 
            month = month-1
    sign = {3: 'Aries', 4: 'Taurus',5: 'Gemini',
    6: 'Cancer',7: 'Leo',8: 'Virgo', 9: 'Libra', 10: 'Scorpio',
    11: 'Sagittarius', 12: 'Capricorn', 1: 'Aquarius', 2: 'Pisces'}
    return sign[month]
