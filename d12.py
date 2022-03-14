import pandas as pd

df1 = pd.read_csv('/Users/apple/Desktop/analysis-master/Pandas_Introduction/NBA/nba16-17.csv')
df1 = df1.dropna() # 删除缺失值行
print(df1.index)
print(df1.columns)
print(df1.info())
best_and_worst = {}
for i in df1.columns[3:]:
    print(i)
    df1 = df1.sort_values(by = i,ascending=False)
    print(df1)
    best_team_index = df1.index[0]
    print(best_team_index)
    worst_team_index = df1.index[-1]
    print(worst_team_index)
    best_team = df1.loc[best_team_index,'Team']
    best_score = df1.loc[best_team_index,i]
    worst_team = df1.loc[worst_team_index,'Team']
    worst_score = df1.loc[worst_team_index,i]
    best_and_worst[i] = {'best_team':best_team,'best_score':best_score,\
                         'worst_team':worst_team,'worst_score':worst_score}
# 将 best_and_worst 字典形式，转换成 DataFrame
best_and_worst = pd.DataFrame(best_and_worst).T
print(best_and_worst)
single_statistics_best = best_and_worst['best_team'].value_counts()
print(single_statistics_best)
single_statistics_worst = best_and_worst['worst_team'].value_counts()
print(single_statistics_worst)
print('联盟中单项第一次数最多的球队是 %s，有 %d 项为第一' % (single_statistics_best.index[0],single_statistics_best[0]))
print('联盟中单项倒数第一次数最多的球队是 %s，有 %d 项为倒一' % (single_statistics_worst.index[0],single_statistics_worst[0]))

# 对三分球的投入情况，进行分析
top5_of_3PA = df1.sort_values(by = '3PA',ascending=False).head()
print(top5_of_3PA)
best_3PA = pd.DataFrame([top5_of_3PA['Team'],top5_of_3PA['3P'],top5_of_3PA['3PA'],top5_of_3PA['3P%']]).T
print(best_3PA)
last5_of_3PA = df1.sort_values(by = '3PA').head(5)
print(last5_of_3PA)
worst_3PA = pd.DataFrame([last5_of_3PA['Team'],last5_of_3PA['3P'],last5_of_3PA['3PA'],last5_of_3PA['3P%']]).T
print(worst_3PA)
# 3分球高出手球队 与 低出手球队（各5只）在 3分球上总出手的差值
difference_on_3PA = best_3PA['3PA'].sum() - worst_3PA['3PA'].sum()
print(difference_on_3PA)
# 3分球高出手球队 与 低出手球队（各5只）在 3分球上命中数的差值
difference_on_3P = best_3PA['3P'].sum() - worst_3PA['3P'].sum()
print(difference_on_3P)
# 平均每只3分球高出手球队与 每只低出手球队 在 3分球上得分的差值
difference_on_points_due_to_3P = difference_on_3P / 5 * 3
print(difference_on_points_due_to_3P)
# 3分球高出手球队与 低出手球队（各5只）平均3分球命中率的差值
difference_on_3P_hit_rate = best_3PA['3P%'].mean() - worst_3PA['3P%'].mean()
print(difference_on_3P_hit_rate)

# 3分球 分析情况，汇总
print("单场多出手了%d记3分球, 多命中了%d记3分球" % (difference_on_3PA,difference_on_3P))
print("单场平均每支爱投3分球的球队在3分球上多得%.2f分" % difference_on_points_due_to_3P)
print("两种球队在3分球命中率上的差值是%.2f%%" % (difference_on_3P_hit_rate * 100))
