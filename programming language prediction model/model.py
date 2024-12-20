import pandas as pd
from sklearn.tree import DecisionTreeClassifier

feeded_contents = pd.read_csv("model.csv")
feeded_contents.dropna(inplace=True)
x = feeded_contents.drop(columns=['recommended programming language'])
y = feeded_contents['recommended programming language']
x = pd.get_dummies(x)

ai_model = DecisionTreeClassifier()
ai_model.fit(x, y)

a = input('Enter your age: ')
b = input('What is your interest: ')

input_data = pd.DataFrame({"age": [a], "interest": [b]})
input_data = pd.get_dummies(input_data).reindex(columns=x.columns, fill_value=0)


predictions = ai_model.predict(input_data)
print(f'Recommended programming language is {predictions[0]}')

