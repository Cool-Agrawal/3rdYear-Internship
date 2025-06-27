import numpy as np
import re

#ques1
emails = np.array([
    'abc@gmail.com',
    'not-an-email',
    'abc@company.org'
])
pattern = r'.+@.+\..+'
results = [bool(re.match(pattern, email)) for email in emails]
print(results)

import numpy as np
import re

mobiles = np.array([
    '9876543210',
    '1234567890',
    '8123456789',
])
pattern = r'^[7-9]\d{9}$'
mobile_results = [bool(re.match(pattern, num)) for num in mobiles]
print(mobile_results)

strings = np.array([
    'HelloWorld',
    'Python3',
    'JustText',
    '123abc'
])

pattern = r'^[A-Za-z]+$'
string_results = [bool(re.match(pattern, s)) for s in strings]
print(string_results)

#ques2
import pandas as pd
print(pd.date_range(start='2025-01-01', periods=5))
dt_series = pd.to_datetime(['2025-06-27 14:30'])
print(dt_series[0].year)
print(dt_series[0].month)
print(dt_series[0].day_name())

#ques3
df = pd.read_csv('../customers-100.csv')
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.index)
filtered = df[df['Company']>"a"]
print(filtered)

print(df["First Name"].value_counts())
pd.options.display.max_rows = 2
df = pd.read_csv('../customers-100.csv')
print(df)