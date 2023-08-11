## Loan_Eligibility_prediction

### Goal

The goal of the problem is to determine which customers will be able to pay their bills and which
customers will most likely be unable to do so. Clearly, I need to develop a classification
system. Algorithms like logistic regression, decision trees, and random forests must be used. I
need to develop a model that is accurate and has a low error percentage. The major goal of this
study is to determine whether or not designating a loan to a certain person is safe. In this study, we
use machine learning algorithms such as classification, logic regression, Decision Tree, and
gradient boosting to predict loan data.

### Introduction
This is a loan prediction project. Using a set of variables, I will predict which of the bank's customers are more likely to have their loan application approved. This is a classification problem in Machine Learning, and banks can use these models to assess their customers for loan qualification and fitness.

### Process of the project
<img width="829" alt="i![CRISP-DM](https://github.com/kruti1028/LHL_Final_project/assets/126723087/097c2358-dc0f-4a1c-acc8-db9b1cd535ab)

### Data Description
The dataset contains a set of 613 records under 13 attributes:
Variable | Description
----------|--------------
Loan_ID | Unique Loan ID
Gender | Male/ Female
Married | Applicant married (Y/N)
Dependents | Number of dependents
Education | Applicant Education (Graduate/ Under Graduate)
Self_Employed | Self employed (Y/N)
ApplicantIncome | Applicant income
CoapplicantIncome | Coapplicant income
LoanAmount | Loan amount in thousands
Loan_Amount_Term | Term of loan in months
Credit_History | Credit history meets guidelines
Property_Area | Urban/ Semi Urban/ Rural
Loan_Status | Loan approved (Y/N)

As mentioned above this is a Binary Classification problem in which we need to predict our Target label which is “Loan Status”.

Loan status can have two values: Yes or No.

1. Yes: if the loan is approved
2. No: if the loan is not approved
So using the training dataset we will train our model and try to predict our target column which is “Loan Status” on the test dataset.

### Loan Prediction

Understanding data before making an algorithm to learn it is the correct way to approach it. It makes the ML problem-solving process much smoother and clearer for both us and the machine. In this notebook, we've formed a certain level of understanding and insights on the data as follows:

1. The Data is Biased
2. Credit History Column has the highest significance with the target variable(Loan Status).
3. There are some Typos in the dataset that leads to bad training, especially in the Loan Amount Term column.
4. Larger population appearing for loans are Males, Graduates, Not Self-employed, Married and with 0 dependents.
5. People who are Graduated and Not self-employed have better chances of getting a loan.
6. People with Property area in Semi-urban places has greater chances of loan approval.
7. People with > 0 Dependents are mostly Married
8. There's a slight linear relationship between Loan Amount and the Applicant's Income, which might be because greater rank business people need higher loans for higher trades.
9. It is also fascinating that some of those people also get lucky with loans.
10. There is no such thing as a Higher Applicant Income getting higher chances of receiving loans, however, people with low Total Income(Applicant Income + Co-applicant Income) have lesser chances compared to higher people with higher Total Income.
11. For the final prediction I haven't used the total income column because as per the data, I feel I will get a more accurate answer with separate applicant income and co-applicant income.
12. Here are my best models and I chose RndomForestClassifier based on the best score   
##### LogisticRegression
1. LogisticRegression score Before Hyperparameter Tuning: 80.47
2. LogisticRegression score after Hyperparameter Tuning: 80.48 
    
------------------------------------------------------
##### SVC
1. SVC score Before Hyperparameter Tuning: 79.39
2. SVC score after Hyperparameter Tuning: 80.66
    
--------------------------------------------------------
##### RandomForestClassifier
1. RandomForestClassifier score Before Hyperparameter Tuning: 77.76
2. RandomForestClassifier score after Hyperparameter Tuning: 80.66
   

13. Here is the final prediction demo app
    I chose the feature for the demo:
    1. gender: female
    2. married: married
    3. Dependents: 1
    4. Education: Uneducated
    5. Self-Employed: Self-Employed
    6. Applicant Income: 1000
    7. Co-Applicant Income: 0.0
    8. Loan Amount: 45000
    9. Loan term: 30
    10. credit History: 0
    11. Properties are: Urban
        based on above feature prediction i got Loan is Not Approved you can see in below Demo Picture
    
    <img width="506" alt="Screenshot 2023-08-11 at 11 03 03 AM" src="https://github.com/kruti1028/LHL_Final_project/assets/126723087/ecf03284-d086-4df9-8bde-73155ea01eca">

