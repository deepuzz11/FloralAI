# FloralAI: Iris Flower Classification Web App

FloralAI is a web-based application that classifies iris flowers into three species using a machine learning model. The application is built using Flask for the backend, Scikit-learn for the machine learning model, and modern web technologies (HTML, CSS, and JavaScript) for the frontend. The model is trained using the Iris dataset and predicts flower species based on four features.

## Features

- **Web Interface**: Simple and user-friendly interface to input flower measurements.
- **Machine Learning Model**: A decision tree classifier model to predict the species of an iris flower based on the input features.
- **Responsive Design**: The frontend is fully responsive, providing a smooth experience across devices.

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: Scikit-learn (Decision Tree Classifier)
- **Frontend**: HTML, CSS, JavaScript
- **Model File**: Stored using `joblib` for easy loading and deployment.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

Once the app is running, open a browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to interact with the application.

## How it Works

1. **Input Form**: Users enter four measurements: Sepal Length, Sepal Width, Petal Length, and Petal Width.
2. **Prediction**: The machine learning model processes the input and predicts the iris flower species: Setosa, Virginica, or Versicolor.
3. **Results**: The predicted species is displayed on the result page.
## Project Structure

FloralAI/
│
├── app.py                # Flask application
├── model.joblib          # Trained machine learning model
├── static/
│   ├── main.css          # Custom styles
│
├── templates/
│   ├── layout.html       # Base HTML template
│   ├── predict.html      # Input form template
│   ├── prediction.html   # Result display template
│
├── forms.py              # Flask form handling
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


## License

This project is licensed under the MIT License - see the LICENSE file for details.


