import json
import pandas as pd
#from pandas.io.json import json_normalize # as json_normalise

data = {
	"One": {
		"0": 60,
		"1": 60,
		"2": 60,
		"3": 45,
		"4": 45,
		"5": 60
	},
	"Two": {
		"0": 110,
		"1": 117,
		"2": 103,
		"3": 109,
		"4": 117,
		"5": 102
	}
}

#print (data)

jsonString = json.dumps(data)
df_read_json = pd.read_json(jsonString, orient='index')
#print("json dataframe: ")
#print(df_read_json)

df = pd.DataFrame([['a', 'b'], ['c', 'd']],
				index =['row 1', 'row 2'],
				columns = ['col 1', 'col 2'])
print("\n df \n")
print (df)
print("\n")
print(df.to_json(orient='split'))
print("\n")
print(df.to_json(orient='index'))

print ('\n *** Nested json parsing *** \n')

with open('rawData.json') as t:
    testScores = json.load(t)

normalisedDF = pd.json_normalize(testScores['TestResults'],
                                 meta=['Students', 'Scores'])

#columns = ['Name', 'Score']

normalisedDF = normalisedDF.set_index('Student')
normalisedDF.columns = ['Paper1', 'Paper2']
#normalisedDF.head(3)
#normalisedDF = pd.read_json(normalisedDF)

#normalisedDF.index = 
print(normalisedDF)


#SectionData = json_normalize(data = d),
#							record_path = 'sections',
#							meta = ['Section A', 'Section B']