import sys
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


df = pd.read_csv("BTC-USD.csv")

close_min = df["Close"].min()
close_max = df["Close"].max()
close_mean = df["Close"].mean()
close_gmean = stats.gmean(df['Close'])
close_hmean = stats.hmean(df['Close'])
close_median = df['Close'].median()
close_mode = df['Close'].mode()
close_std = np.std(df['Close'])

open_min = df["Open"].min()
open_max = df["Open"].max()
open_mean = df["Open"].mean()
open_gmean = stats.gmean(df['Open'])
open_hmean = stats.hmean(df['Open'])
open_median = df['Open'].median()
open_mode = df['Open'].mode()
open_std = np.std(df['Open'])

high_min = df["High"].min()
high_max = df["High"].max()
high_mean = df["High"].mean()
high_gmean = stats.gmean(df['High'])
high_hmean = stats.hmean(df['High'])
high_median = df['High'].median()
high_mode = df['High'].mode()
high_std = np.std(df['High'])

low_min = df["Low"].min()
low_max = df["Low"].max()
low_mean = df["Low"].mean()
low_gmean = stats.gmean(df['Low'])
low_hmean = stats.hmean(df['Low'])
low_median = df['Low'].median()
low_mode = df['Low'].mode()
low_std = np.std(df['Low'])

volume_min = df["Volume"].min()
volume_max = df["Volume"].max()
volume_mean = df["Volume"].mean()
volume_gmean = stats.gmean(df['Volume'])
volume_hmean = stats.hmean(df['Volume'])
volume_median = df['Volume'].median()
volume_mode = df['Volume'].mode()
volume_std = np.std(df['Volume'])


date = df.Date
mean_close_open = (df.Close + df.Open) / 2

plt.plot(date, df.Close,color="black", linestyle="solid", label="BTC-PRICE")
plt.plot(date, mean_close_open,color="red", linestyle="dashed", label="BTC")

plt.xlabel("Days")
plt.ylabel("Price")
plt.show()

index = ['Open','Close','High','Low','Volume']
columns = ['Min','Max','Mean','Gmean','Hmean','Median','std']
df_last = pd.DataFrame(index= index, columns= columns)

new_open_info = [open_min, open_max, open_mean, open_gmean, open_hmean, open_median, open_std]
df_last.loc['Open'] = new_open_info

new_close_info = [close_min, close_max, close_mean, close_gmean, close_hmean, close_median, close_std]
df_last.loc['Close'] = new_close_info

new_high_info = [high_min, high_max, high_mean, high_gmean, high_hmean, high_median, high_std]
df_last.loc['High'] = new_high_info

new_low_info = [low_min, low_max, low_mean, low_gmean, low_hmean, low_median, low_std]
df_last.loc['Low'] = new_close_info

new_volume_info = [volume_min, volume_max, volume_mean, volume_gmean, volume_hmean, volume_median, volume_std]
df_last.loc['Volume'] = new_volume_info

print(df_last)



