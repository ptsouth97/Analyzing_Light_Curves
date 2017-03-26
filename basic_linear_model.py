import pandas as pd
import matplotlib.pyplot as plt

filename = 'co2_mm_mlo.txt'
data = pd.read_table(filename, delimiter='\s+', skiprows=72, names=['0','1','decimal date','average','interpolated','trend','#days'])

x = data['decimal date']
y = data['interpolated']

plt.plot(x, y)
plt.title('Atmospheric CO2 at Mauna Loa Observatory')
plt.xlabel('Year')
plt.ylabel('Parts Per Million')
plt.show()

