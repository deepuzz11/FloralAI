from flask import Flask, render_template, request
from forms import Inputform
import numpy as np
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd5d4f3422a72273efb82e7a5904514a2'


@app.route("/", methods=['GET', 'POST'])
def predict():
    form = Inputform()
    if form.is_submitted():
        result = request.form

        # Collect input values
        lis = []
        for key, value in result.items():
            if key in ['sl', 'sw', 'pl', 'pw']:
                lis.append(value)

        # Convert input into np array for prediction
        inputs = np.array([lis])

        # Load the model and make the prediction
        model = joblib.load('model.joblib')
        pred = model.predict(inputs)

        # Get the predicted flower species
        if pred == 0:
            result = 'Setosa'
        elif pred == 1:
            result = 'Virginica'
        elif pred == 2:
            result = 'Versicolor'

        return render_template('prediction.html', result=result)
    return render_template('predict.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
