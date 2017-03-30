import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import math
import numpy as np

filename = 'co2_mm_mlo.txt'
data = pd.read_table(filename, delimiter='\s+', skiprows=72,
                     names=['0','1','decimal date','average','interpolated','trend','#days'])

# time (t) goes on the x-axis anc co2 goes on the y-axis

co2 = data['interpolated']

t = data['decimal date']                            # by default, statsmodels doesn't compute y-intercept
T = sm.add_constant(t)
tsquared = t**2                                     # squaring provides the 'quadratic' aspect
Tsquared = sm.add_constant(tsquared)                # again, by default, statsmodels doesn't compute y-intercept

c1 = np.cos(2*math.pi*t)
s1 = np.sin(2*math.pi*t)

model = smf.ols(formula = 'co2 ~ T + Tsquared + c1 + s1', data = data).fit()
results = model.fittedvalues
print(model.summary())

plt.figure(1)
plt.subplot(211)
plt.plot(t, co2)
plt.plot(t, results)
plt.title('Sinusoidal Model of Atmospheric CO2 at Mauna Loa Observatory')
plt.ylabel('CO2 Concentration (ppmv)')

residuals = model.resid
'''c1 = np.cos(2*math.pi*t)
s1 = np.sin(2*math.pi*t)
residualModel = smf.ols(formula = 'residuals ~ T + Tsquared + c1 + s1', data = residuals).fit()'''

plt.subplot(212)
plt.plot(t, residuals)
# plt.plot(t, residualModel.fittedvalues)
plt.ylabel('Residuals (ppmv)')
plt.xlabel('Time (years)')
plt.title('Residuals showing possible harmonics')
plt.show()