import numpy as np
import pandas as pd

name1 = np.loadtxt('/Users/apple/Desktop/analysis-master/Pandas_Introduction/score/Data/name.txt',\
                   delimiter='\n',dtype='str')
score1 = np.loadtxt('/Users/apple/Desktop/analysis-master/Pandas_Introduction/score/Data/score1.txt',\
                    delimiter='\n',dtype='int')
score2 = np.loadtxt('/Users/apple/Desktop/analysis-master/Pandas_Introduction/score/Data/score2.txt',\
                    delimiter='\n',dtype='int')
score3 = np.loadtxt('/Users/apple/Desktop/analysis-master/Pandas_Introduction/score/Data/score3.txt',\
                    delimiter='\n',dtype='int')
print(name1)
print(score1)
print(score2)
print(score3)
score1 = pd.Series(score1,index=name1)
score2 = pd.Series(score2,index=name1)
score3 = pd.Series(score3,index=name1)
print(score1)
print(score2)
print(score3)
bins = [0] + list(range(60,101,10))
print(bins)
cuts1 = pd.cut(score1,bins,right=False)
print(pd.value_counts(cuts1))
cuts2 = pd.cut(score2,bins,right=False)
print(pd.value_counts(cuts2))
cuts3 = pd.cut(score3,bins,right=False)
print(pd.value_counts(cuts3))
print(score1.max())
print(score1.describe())
total_score = pd.concat([score1,score2,score3],axis=1)
total_score.rename(columns={0:'literature',1:'mathematics',2:'english'},inplace=True)
print(total_score)
def score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
total_score['literature_grade'] = total_score['literature'].map(score_to_grade)
total_score['mathematics_grade'] = total_score['mathematics'].map(score_to_grade)
total_score['english_grade'] = total_score['english'].map(score_to_grade)
total_score['personal_total'] = total_score.sum(axis=1)
total_score['personal_average'] = total_score.iloc[:,:-1].mean(axis=1)
print(total_score)
total_score = total_score.reindex(columns = ['literature','literature_grade','mathematics',\
                                             'mathematics_grade','english','english_grade',\
                                             'personal_total','personal_average'])
print(total_score)
print(total_score.describe())
score_level_data = total_score.loc[:,'literature':'english_grade']
score_level_data.columns = [['literature','literature','mathematics','mathematics',\
                             'english','english'],['score','grade','score','grade','score','grade']]
print(score_level_data)
score_level_data['personal_total'] = score_level_data.sum(axis = 1)
score_level_data['personal_average'] = score_level_data.iloc[:,:-1].mean(axis = 1)
score_level_data = score_level_data.sort_values(by = 'personal_total',ascending=False)
print(score_level_data)
print(score_level_data.describe())
score_level_data.to_csv('/Users/apple/Desktop/score_level_data.csv')
