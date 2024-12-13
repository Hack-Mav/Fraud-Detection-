from scripts.data_loader import load_data
from scripts.eda import visualize_gender_distribution, visualize_target_distribution, plot_correlation_heatmap
from scripts.preprocessing import preprocess_data
from scripts.training import train_model
from scripts.evaluation import evaluate_model
import joblib
from app.app import create_app
from sklearn.model_selection import train_test_split

data_path = 'data/creditcard.csv'
data = load_data(data_path)

# EDA
# visualize_gender_distribution(data)
# visualize_target_distribution(data)
# plot_correlation_heatmap(data)

# Preprocessing
X, y, scaler = preprocess_data(data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Model Training
model = train_model(X_train, y_train)

# Evaluation
# evaluate_model(model, X_test, y_test)

# Save Model
joblib.dump(model, 'models/fraud_detection_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

# Flask App
app = create_app(model, scaler)
app.run(debug=True)
