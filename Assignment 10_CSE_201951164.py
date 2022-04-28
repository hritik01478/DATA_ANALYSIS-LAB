# -*- coding: utf-8 -*-

#CS312 - ASSIGNMENT 10
#Urmila Rathore
#201951164

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import pylab as py
import numpy as np

location_loan_train_data = "Hp/Desktop/SHAPEAI/DATA_ANALYSIS-LAB/loan-train.csv"

loan_train_data = pd.read_csv(location_loan_train_data).fillna(0)
loan_train_data_applicant_income = loan_train_data["ApplicantIncome"].to_numpy()

mean_applicant_income = np.mean(loan_train_data_applicant_income)
standard_deviation_applicant_income = np.std(loan_train_data_applicant_income)
print("Mean of applicants income: ", mean_applicant_income)
print("Standard deviation of applicant income: ", standard_deviation_applicant_income)

loan_train_data_applicant_income = np.diff(np.log(loan_train_data_applicant_income[loan_train_data_applicant_income > 0]))
loan_train_data_applicant_income=(loan_train_data_applicant_income - np.mean(loan_train_data_applicant_income))/np.std(loan_train_data_applicant_income)
sns.histplot(loan_train_data_applicant_income,kde=True)
plt.xlabel("z-score")

sm.qqplot(loan_train_data_applicant_income, line ='45')
py.show()

