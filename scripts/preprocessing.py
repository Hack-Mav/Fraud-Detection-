import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(data):
    label_encoder = LabelEncoder()
    data['Attrition_Flag'] = label_encoder.fit_transform(data['Attrition_Flag'])
    X = data.drop(['Attrition_Flag', 'CLIENTNUM'], axis=1)
    X = pd.get_dummies(X, drop_first=True)
    print(X.columns.tolist())
    y = data['Attrition_Flag']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler
