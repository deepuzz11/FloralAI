import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your dataset
df = pd.read_csv('iris.csv')

# Encoding the target values (species)
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

X = df.iloc[:, :-1]
y = df['species']

# Train the decision tree model
model = DecisionTreeClassifier(max_depth=4)
model.fit(X, y)

# Save the model using joblib (recommended for larger models)
joblib.dump(model, 'model.joblib')
