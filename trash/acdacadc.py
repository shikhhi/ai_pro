from matplotlib import pyplot as plt    
    
# Pie chart, where the slices will be ordered and plotted counter-clockwise:    
Aus_Players = 'Smith', 'Finch', 'Warner', 'Lumberchane'    
Runs = [42, 32, 18, 24]    
explode = (0.1, 0, 0, 0)  # it "explode" the 1st slice     
    
fig1, ax1 = plt.subplots()    
ax1.pie(Runs, explode=explode, labels=Aus_Players, autopct='%1.1f%%',    
        shadow=True, startangle=90)    
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
    
plt.show()  