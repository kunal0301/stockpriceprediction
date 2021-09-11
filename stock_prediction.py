import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

stock_name = input("ENTER THE NAME OF THE STOCK: ")

if stock_name == 'HDFC':
    data = pd.read_csv('HDFC.csv')
    print(data)
elif stock_name =='tata motors':
    data = pd.read_csv('tata motors.csv')
    print(data)
elif stock_name == 'hero':
    data = pd.read_csv('hero.csv')
    print(data)
elif stock_name == 'cipla':
    data = pd.read_csv('cipla.csv')
    print(data)
elif stock_name == 'BANDHANBNK':
    data = pd.read_csv('BANDHANBNK.csv')
    print(data)
elif stock_name == 'aditya birla':
    data = pd.read_csv('aditya birla.csv')
    print(data)
else:
    data = pd.read_csv('PNB.csv')
    print(data)

# log returns
data['log_returns'] = np.log(data['Adj Close'] / data['Adj Close'].shift(1))
print("log returns")
print(data['log_returns'])

# plot the log returns
data['log_returns'].plot(figsize=(8,5))
plt.title('Log Returns')
plt.xlabel('Number Of Days')
plt.show()

# calculate average daily return
log_return_d = data['log_returns'].mean()
print("PRINTING DAILY RATE OF RETURN")
print(log_return_d)

# calculating annual  return of stock including holidays
log_return_a = data['log_returns'].mean()*250
print("PRINTING ANNUAL RETURN VALUE")
print(log_return_a)

#converting into %
print (str(round(log_return_a,5)*100)+ '%')


# market index
ind_data = pd.read_csv('^NSEI.csv')['Adj Close']

 # ploting on graph
(ind_data / ind_data[0] * 100).plot(figsize=(15,6));
plt.title('^NSEI Graph')
plt.xlabel('Number of Days')
plt.show()

ind_returns = (ind_data / ind_data.shift(1))-1
print("indicies simple return")
print(ind_returns)

annual_ind_returns = ind_returns.mean()*250
print("annual return of indicies")
print(annual_ind_returns)


# predicting stock price

log_return = np.log(1+ data['Adj Close'].pct_change())
data['Adj Close'].plot(figsize=(10,6));
log_return.plot(figsize=(10,6))
plt.title('Log Returns of ^NSEI index')
plt.xlabel("date")
plt.show()

u = log_return.mean()
print("mean")
print(u)

var = log_return.var()
print("variance")
print(var)

drift = u-(0.5*var)
print("drift")
print(drift)

stdev = log_return.std()
print("standard deviation")
print(stdev)

np.array(drift)
a = drift
print(a)
b = stdev
print(b)
norm.ppf(0.95)
x = np.random.rand(10,2)
print(x)

norm.ppf(x)
z = norm.ppf(np.random.rand(10,2))
print(z)

t_intervals = 1000
iterations = 10

daily_returns = np.exp(a+b * norm.ppf(np.random.rand(t_intervals,iterations)))
print("daily returns")
print(daily_returns)

s0 = data['Adj Close'].iloc[-1]

price_list = np.zeros_like(daily_returns)

price_list[0] = s0
print("price list")
print(price_list)

for t in range(1, t_intervals):
    price_list[t] = price_list[t-1] * daily_returns[t]

print("price list")
print(price_list)

plt.figure(figsize = (10,6))
plt.plot(price_list)
plt.title('Prediction Of Stock Price')
plt.show()










