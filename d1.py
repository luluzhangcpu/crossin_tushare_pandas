import tushare as ts
pro = ts.pro_api() # 需要注册 tushare pro版，获得个人的 token number；重新设置，即可;
df1 = pro.ncov_global(country = '中国',fields='country,publish_date,confirmed_num,update_time')
print(df1)
