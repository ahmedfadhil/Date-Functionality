import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Timestamp
timing = pd.Timestamp('9/1/2016 10:05AM')
print(timing)

# Period

testing1 = pd.Period('1/2016')

print(testing1)

# DatetimeIndex

t1 = pd.Series(list('abc'), [pd.Timestamp('2016/09/01'),
                             pd.Timestamp('2016/09/02'),
                             pd.Timestamp('2016/09/03')]
               )

print(t1)

print(type(t1.index))

t2 = pd.Series(list('def'), [pd.Period('2016/09/01'),
                             pd.Period('2016/09/02'),
                             pd.Period('2016/09/03')]
               )

print(t2)
print(type(t2.index))

# Converting to Datetime
d1 = ['2 June 2013', '2 June 2014', '2 June 2015', '2 June 2016']

t3 = pd.DataFrame(np.random.randint(10, 100, (4, 2)), index=d1, columns=list('AB'))
print(t3)

DateTime = t3.index = pd.to_datetime(t3.index)
print(DateTime)

dateFirst = pd.to_datetime('4.3.6', dayfirst=True)

print(dateFirst)

# TimeDeltas

TimeDeltas = pd.Timestamp('09/03/2016') - pd.Timestamp('08/06/2016')

print(TimeDeltas)

TimeLaps = pd.Timestamp('09/03/2016 8:10AM') + pd.Timedelta('12D 5H')
print(TimeLaps)

# Working with Dates in a Dataframe
DateRange = dates = pd.date_range('09/03/2016', periods=9, freq='2W-SUN')
print(DateRange)

df = pd.DataFrame({
    'Count1': 100 + np.random.randint(-5, 10, 9).cumsum(),
    'Count2': 120 + np.random.randint(-5, 10, 9).cumsum()
}, index=dates)

print(df.index.weekday_name)
print(df.diff())

# To find the mean count of the data

print(df.resample('M').mean())

print('Change Frequency:')

print(df.asfreq('W', method='ffill'))


print(df.plot())

plt.show()