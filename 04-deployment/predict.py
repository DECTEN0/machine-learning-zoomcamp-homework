
import pickle



#open pipeline
with open("model.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)



#make preds
datapoint = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 6,
    'monthlycharges': 29.85,
    'totalcharges': 129.85
}


churn = pipeline.predict_proba(datapoint)[0,1]
print(f"probability of chrning: {churn}")
if churn >=0.5:
    print("Send promo")
else:
    print("Don't send promo")