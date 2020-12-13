import pandas as pd

df = pd.read_csv("cereal.csv")

checkList = ['protein', 'fiber', 'vitamins', 'carbo']

for item in checkList:
    avg = df[item].mean()
    highest = df[item].max()
    lowest = df[item].min()
    stddev = df[item].std()
    print (item, ' : ', '\n')
    print ('mean: ', avg, 'max: ' , highest, 'min: ', lowest, 'stdev: ', stddev)
    print ('\n')


