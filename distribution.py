import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use('ggplot')

print(np.random.binomial(1, 0.5))
print(np.random.binomial(1000, 0.5) / 1000)

chance_of_tornado = 0.01 / 100
tornado = np.random.binomial(100000, chance_of_tornado)
print(tornado)

chance_of_tornado = 0.01
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
two_days_in_a_row = 0
for j in range(1, len(tornado_events) - 1):
    if tornado_events[j] == 1 and tornado_events[j - 1] == 1:
        two_days_in_a_row += 1

print('{} tornados back to back in {} years'.format(two_days_in_a_row, 1000000 / 365))

print('Uniform:', np.random.uniform(0, 1))
print('Normal:', np.random.normal(0, 1))

distribution = np.random.normal(0.75, size=1000)

overall = np.sqrt(np.sum((np.mean(distribution) - distribution) ** 2) / len(distribution))
print(overall)

print(np.std(distribution))

first = stats.kurtosis(distribution)
second = stats.skew(distribution)

print(first)
print(second)

# Chi square distribution
chi_square_df2 = np.random.chisquare(2, size=10000)
print(stats.skew(chi_square_df2))

chi_square_df5 = np.random.chisquare(5, size=10000)
print(stats.skew(chi_square_df5))

output = plt.hist([chi_square_df2, chi_square_df5], bins=50, histtype='step',
                  label=['2 Degree of fredom', '5 Degree of fredom'])

plt.legend(loc='upper right')
plt.show()

# hypothesis Testing
df = pd.read_csv('grades.csv')
df.head()

early = df[df['assignment_submission'] <= '2015']
late = df[df['assignment_submission'] > '2015']

early.mean()
late.mean()

stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])
stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade'])
