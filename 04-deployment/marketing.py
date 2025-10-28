
import requests

url = "http://localhost:9696/predict"

#customer
customer = {
  "gender": "female",
  "seniorcitizen": 0,
  "partner": "yes",
  "dependents": "no",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 6,
  "monthlycharges": 29.85,
  "totalcharges": 129.85
}


#send request
response = requests.post(url, json=customer)

churn = response.json()

print(f"Response : {churn}")

if churn['churn'] >=0.5:

    print("Send promo")
else:
    print("Don't send promo")