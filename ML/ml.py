from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas
import numpy


# Get dataset
print('Reading data')
data_frame = pandas.read_csv('data.csv', header=0)
print(data_frame.shape)
print('- - -')
print('Getting column names')
column_names = list(data_frame.columns.values)
print('- - -')
print('Splitting into training and testing sets')
X, Y = data_frame.iloc[:, :-1], data_frame.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
print('- - -')

# Model
random_classifier = RandomForestClassifier(n_estimators=100, max_leaf_nodes=15, n_jobs=-1, random_state=42)
random_classifier.fit(X_train, y_train)
y_prediction = random_classifier.predict(X_test)
print(f"RandomForestClassifier accuracy: {accuracy_score(y_test, y_prediction)}")