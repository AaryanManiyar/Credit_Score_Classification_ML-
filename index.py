import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("train.csv")
print(data.head())

#look at the information about the columns in the dataset
print(data.info())

#look if the dataset has any null values or not
print(data.isnull().sum())

#look at the Credit_Score column values
print(data['Credit_Score'].value_counts())

#Credit Scores based on Occupation
fig = px.box(data, x="Occupation", color="Credit_Score",
             title="Credit Scores Based on Occupation",
             color_discrete_map={
                 'Poor' : 'red',
                 'Standard' : 'yellow',
                 'Good' : 'green',
             })
fig.show()

#Credit Scores based on Annual Income
fig = px.box(data, x="Credit_Score", y="Annual_Income",
             color="Credit_Score", title="Credit Score Based on Annual Income",
             color_discrete_map={
                 'Poor' : 'red',
                 'Standard' : 'yellow',
                  'Good' : 'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Score based on Monthly Inhand Salary
fig = px.box(data, x="Credit_Score", y="Monthly_Inhand_Salary",
             color="Credit_Score", title="Credit Scores Based on Monthly Inhand Salary",
             color_discrete_map={
                 'Poor' : 'red',
                 'Standard' : 'yellow',
                 'Good' : 'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Score based on Number of Bank Account
fig = px.box(data, x="Credit_Score", y="Num_Bank_Accounts", 
             color="Credit_Score", title="Credit Scores Based on Number of Bank Accounts", 
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Score based on Number of Credit Cards
fig = px.box(data, x="Credit_Score", y="Num_Credit_Card", 
             color="Credit_Score", title="Credit Scores Based on Number of Credit cards", 
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Score based on the Average Interest Rates
fig = px.box(data, x="Credit_Score", y="Num_of_Loan", 
             color="Credit_Score", title="Credit Scores Based on Number of Loans Taken by the Person",
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Scores based on Avg Numbers of Days delayed for Credit Card Payments
fig = px.box(data, x="Credit_Score", y="Delay_from_due_date", 
             color="Credit_Score", title="Credit Scores Based on Average Number of Days Delayed for Credit card Payments", 
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Scores based on Number of Delayed Payments
fig = px.box(data, x="Credit_Score", y="Num_of_Delayed_Payment", 
             color="Credit_Score", title="Credit Scores Based on Number of Delayed Payments",
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Scores based on Outstanding Debt
fig = px.box(data, x="Credit_Score", y="Outstanding_Debt", 
             color="Credit_Score", title="Credit Scores Based on Outstanding Debt",
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Scores based on Credit Utilization Ratio
fig = px.box(data, x="Credit_Score", y="Credit_Utilization_Ratio", 
             color="Credit_Score",title="Credit Scores Based on Credit Utilization Ratio", 
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Scores based on Credit History Age
fig = px.box(data, x="Credit_Score", y="Credit_History_Age", 
             color="Credit_Score", title="Credit Scores Based on Credit History Age",
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Scores based on Total Number if EMIs per Month
fig = px.box(data, x="Credit_Score", y="Total_EMI_per_month", 
             color="Credit_Score", title="Credit Scores Based on Total Number of EMIs per Month",
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Scores based on Amount Invested Monthly
fig = px.box(data, x="Credit_Score", y="Amount_invested_monthly", 
             color="Credit_Score", title="Credit Scores Based on Amount Invested Monthly",
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Scores based on Monthly Balance Left
fig = px.box(data, x="Credit_Score", y="Monthly_Balance", 
             color="Credit_Score", title="Credit Scores Based on Monthly Balance Left",
             color_discrete_map={
                 'Poor':'red',
                 'Standard':'yellow',
                 'Good':'green'
             })
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Credit Mix : The credit mix feature tells about the types of credits and loans you have taken.
data['Credit_Mix'] = data["Credit_Mix"].map({
        "Standard" : 1,
        "Good" : 2,
        "Bad" : 0
    })

#Now I will split the data into features and labels by selecting the features we found important for our model
from sklearn.model_selection import train_test_split
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary", 
                   "Num_Bank_Accounts", "Num_Credit_Card", 
                   "Interest_Rate", "Num_of_Loan", 
                   "Delay_from_due_date", "Num_of_Delayed_Payment", 
                   "Credit_Mix", "Outstanding_Debt", 
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data[["Credit_Score"]])

#let’s split the data into training and test sets and proceed further by training a credit score classification model
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.33, random_state=42)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(xtrain, ytrain)

#let’s make predictions from our model by giving inputs to our model according to the features we used to train the model
print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
print("Predicted Credit Score = ", model.predict(features))
