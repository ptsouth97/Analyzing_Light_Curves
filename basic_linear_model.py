import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

filename = 'co2_mm_mlo.txt'
data = pd.read_table(filename, delimiter='\s+', skiprows=72,
                     names=['0','1','decimal date','average','interpolated','trend','#days'])

t = data['decimal date']
x = data['interpolated']
T = sm.add_constant(t)                              # by default, statsmodels doesn't compute y-intercept

model = sm.OLS(x, T)
results = model.fit()
print(results.summary())

plt.figure(1)
plt.subplot(211)
plt.plot(t, x)
plt.plot(t, results.fittedvalues)
plt.title('Atmospheric CO2 at Mauna Loa Observatory')
plt.ylabel('CO2 Concentration (ppmv)')

plt.subplot(212)
plt.plot(t, results.resid)
plt.ylabel('Residuals (ppmv)')
plt.xlabel('Time (years)')
plt.show()