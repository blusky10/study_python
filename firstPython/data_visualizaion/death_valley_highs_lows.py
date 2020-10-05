import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename='d:\\STUDY\\study_python\\firstPython\\data_visualizaion\\data\\death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    print(header_row)

    dates, highs, lows=[], [],[]
    for row in reader:
        current_date=datetime.strptime(row[2], '%Y-%m-%d')
        
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)        
            lows.append(low)
            dates.append(current_date)
    
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates,highs, c='red')    
ax.plot(dates,lows, c='blue')    

ax.set_title('Daily high temperatures, July 2018 \n', fontsize=24)
ax.set_xlabel('', fontsize=10)

fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()
