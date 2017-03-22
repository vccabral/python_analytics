import pandas as pd
from sklearn.neural_network import MLPClassifier

def xor(row):
	return (row[0] or row[1]) and not (row[0] and row[1])

df = pd.read_csv('example16.csv')
df['answer'] = df.apply(xor, axis=1)

X = [
	[
		row[1][0], 
		row[1][1]
	] for row in df.iterrows()
]

y = [row[1][2] for row in df.iterrows()]

clf = MLPClassifier(
	solver='lbfgs', alpha=1e-5,
	hidden_layer_sizes=(6, 2), random_state=1
)

clf.fit(X, y)

print(clf.predict(X))


