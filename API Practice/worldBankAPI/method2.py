import requests

#Method 1: API with all specification in URL

reader = requests.get('http://api.worldbank.org/v2/country/us;in;cn/indicators/SP.POP.TOTL?date=2017:2019&format=json')

#Method 2: API with specifications in a separate variable called load

load = {'date':'2017:2019','format':'json'}
reader_load = requests.get('http://api.worldbank.org/v2/country/us;in;cn/indicators/SP.POP.TOTL', params=load)

#Verify if both the strings have same value

print (reader.text == reader_load.text)

load1 = {'date':'2006:2019','format':'json'}
reader_load1 = requests.get('http://api.worldbank.org/v2/country/in;cn/indicators/SP.POP.TOTL', params=load1)

from collections import defaultdict

data_dictionary = defaultdict(list)

# Create a dictionary and match each country(key) with a list of values(date & population)

for values in reader_load1.json()[1]:
# Match country value from json output. Append corresponding values to the lists
    if data_dictionary[values['country']['value']]:
        data_dictionary[values['country']['value']][0].append(int(values['date']))
        data_dictionary[values['country']['value']][1].append(float(values['value']))
    else:
# If dictionary does not have country(key), then initialize it with x and y values(date & population) in lists.
        data_dictionary[values['country']['value']] = [[],[]]

# Print results from the data dictionary
for country in data_dictionary:
    print(country)
    print('year: ', data_dictionary[country][0])
    print('population: ', data_dictionary[country][1])

# Use matplotlib to visualize the results

import matplotlib.pyplot as plt

# Plot data of each country

for country in data_dictionary:
    plt.plot(data_dictionary[country][0], data_dictionary[country][1], label=country)

# Label all plots

plt.title('Population growth of China and India 2006 to 2019')
plt.xlabel('year')
plt.ylabel('Population Growth in billions')
plt.legend()
plt.show()
