from datetime import date
d1=(15, 2, 2025)
d2=(16, 2, 2025)
d3=(17, 2, 2025)
date1=date(d1[2], d1[1], d1[0])
date2=date(d2[2], d2[1], d2[0])
difference= abs((date2-date1).days)
print("The number of days between the two dates:", difference)
