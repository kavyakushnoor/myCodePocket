import pandas as pd

df = pd.read_csv("cereal.csv")

checkList = ['protein', 'fiber', 'vitamins', 'carbo']

for item in checkList:
    avg = df[item].mean()
    highest = df[item].max()
    lowest = df[item].min()
    stddev = df[item].std()
    print (item, ':', 'mean: ', avg, 'max: ' , highest, 'min: ', lowest, 'stdev: ', stddev)
'''
    new_df = df.agg({item: ['mean', 'std', 'max', 'min']})
agg_df = pd.DataFrame()
agg_df.columns = ['protein', 'fiber', 'vitamins', 'carbo']
agg_df.rows = ['mean', 'std', 'max', 'min']
    #print (new_df)
    #agg_df=agg_df.join(new_df)
    #agg_df=agg_df.rename(columns={item: item})
print (agg_df)
'''
