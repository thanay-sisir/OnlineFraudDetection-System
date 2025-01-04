# DEPLOYMENT

└── OnlinFraudDtection &nbsp;   /  #foldername <br>
├── app.py &nbsp;  # Your Flask application <br> 
├── model.pkl&nbsp;  # Your model file <br>
├── onlinefraud.csv &nbsp;  # Your CSV file <br>
└── templates/ <br>
       &nbsp; └── index.html   # Your HTML template file


The online payment fraud detection system developed in this project effectively demonstrates the application of machine learning algorithms, such as Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting, to predict fraudulent transactions. Acheiving 98% accuracy with Random Forest Classifier, While the model showed promising results in detecting fraud,challenges remain in minimizing false positives and false negatives

 # METHODOLOGY

This study utilized a dataset from Kaggle, an open platform, due to the challenges of accessing real-time datasets for privacy reasons. The dataset comprises 6,362,622 records with 11 attributes, including:

type (type of payment),
amount,
nameOrig (customer initiating the transaction),
oldbalanceOrg (balance before the transaction),
newbalanceOrig (balance after the transaction),
nameDest (transaction recipient),
oldbalanceDest (recipient's balance before the transaction),
newbalanceDest (recipient's balance after the transaction),
isFraud (1 if fraudulent, 0 if legitimate), and
isFlaggedFraud (flagged suspicious transactions).


Only relevant features like transaction type, amount, origin balance, and destination balance are used for training. Irrelevant or redundant features are dropped to improve model accuracy
# PROPOSED IMPLEMENTATION
![image](https://github.com/user-attachments/assets/8afad179-2fab-4e16-af6f-f242e2e53cfe)

# DATASET
![image](https://github.com/user-attachments/assets/39852558-d9db-4528-801e-f1874a6a0ddc)

# ACCURACY PREDICTION OF MODELS

![image](https://github.com/user-attachments/assets/d5dd680f-b9a9-47b4-b7d7-25a518522d6b)
# CLASSIFICATION REPORT
![image](https://github.com/user-attachments/assets/36f9bc38-bb08-4bf3-bc73-f2614aa84ebf)

# PREDICTION OF MODEL
![image](https://github.com/user-attachments/assets/1a166ee2-3ec7-4e3a-bcf6-0f5617e23af9)
![image](https://github.com/user-attachments/assets/5ebca294-ff57-4f56-9cf7-1f0a8a8bd7aa)







    
