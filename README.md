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
Credit_History | credit history meets guidelines
Property_Area | Urban/ Semi Urban/ Rural
Loan_Status | Loan approved (Y/N)

As mentioned above this is a Binary Classification problem in which we need to predict our Target label which is “Loan Status”.

Loan status can have two values: Yes or No.

Yes: if the loan is approved
No: if the loan is not approved
So using the training dataset we will train our model and try to predict our target column which is “Loan Status” on the test dataset.


