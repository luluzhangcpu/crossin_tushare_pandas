import tushare as ts
pro = ts.pro_api()
df1 = pro.stock_basic()
print(df1.head(10))
df1['riseDays'] = 0
print(df1.head(10))
print(ts.get_hist_data('600103').info())
for i in range(30):
    c = df1.iloc[i]
    code = c['symbol']
    history = ts.get_hist_data(code)
    if history.iloc[0]['price_change'] < 0:
        continue
    else:
        days = 0
        for j in range(len(history.index)):
            if history.iloc[j]['price_change']>0:
                days += 1
            else:
                break
        df1.iloc[i]['riseDays'] = days
print(df1.head(30))
df1.to_csv('/Users/apple/Desktop/stocks_infos.csv',encoding = 'gbk')
