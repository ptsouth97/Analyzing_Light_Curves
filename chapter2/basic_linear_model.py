import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

filename = 'co2_mm_mlo.txt'
data = pd.read_table(filename, delimiter='\s+', skiprows=72,
                     names=['0','1','decimal date','average','interpolated','trend','#days'])

t = data['decimal date']
co2 = data['interpolated']
T = sm.add_constant(t)                              # by default, statsmodels doesn't compute y-intercept

model = sm.OLS(co2, T)
results = model.fit()
print(results.summary())

plt.figure(1)
plt.subplot(211)
plt.plot(t, co2)
plt.plot(t, results.fittedvalues)
plt.title('Linear Model of Atmospheric CO2 at Mauna Loa Observatory')
plt.ylabel('CO2 Concentration (ppmv)')

residuals = results.resid
tsquared = t**2                                     # squaring provides the 'quadratic' aspect
Tsquared = sm.add_constant(tsquared)                # again, by default, statsmodels doesn't compute y-intercept
residualModel = smf.ols(formula = 'residuals ~ T + Tsquared', data = residuals).fit()

plt.subplot(212)
plt.plot(t, residuals)
plt.plot(t, residualModel.fittedvalues)
plt.ylabel('Residuals (ppmv)')
plt.xlabel('Time (years)')
plt.title('Residuals showing quadratic fit')
plt.show()