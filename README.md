# ML Assignment 2 – Heart Failure Prediction 🫀
Evaluate 6 classification models

## a. Problem statement
The objective of this assignment is to train and evaluate multiple classification models. I have selected a data set to train and predict whether a patient with heart failure will survive or not based on their clinical records. The goal is to identify the high-risk patients, so required medical procedures can be suggested.

The target/outcome variable:
- __`y = 0 => Not Dead` → Survived__
- __`y = 1 => Dead` → Not Survived__

## b. Dataset description
[`Heart Failure Prediction`](https://www.kaggle.com/datasets/aadarshvelu/heart-failure-prediction-clinical-records) data from Kaggle.

The Heart Failure Clinical Records data contains clinical and demographic information of patients diagnosed with heart failure. It contains details about existing medical conditions and also clinical measurements such as ejection fraction, serum creatinine, and serum sodium. These attributes are highly useful for predicting a patient’s risk of mortality during the follow-up period.

__Features: _12___ - `age` `creatinine_phosphokinase` `ejection_fraction` `platelets` `serum_creatinine` `serum_sodium` `time` `anaemia` `diabetes` `high_blood_pressure` `sex` `smoking`

__Data set size: _5000___ (before cleaning)

__Instances/sample size: _1319___ (after removing the contradictory and duplicate samples)

__Train/Test split: 80:20 → _1055:264___

### Attribute details
- age: age of the patient (years)
- anaemia: decrease of red blood cells or hemoglobin (boolean)
- creatinine phosphokinase (CPK): level of the CPK enzyme in the blood (mcg/L)
- diabetes: if the patient has diabetes (boolean)
- ejection fraction: percentage of blood leaving the heart at each contraction (percentage)
- high blood pressure: if the patient has hypertension (boolean)
- platelets: platelets in the blood (kiloplatelets/mL)
- sex: woman or man (binary)
- serum creatinine: level of serum creatinine in the blood (mg/dL)
- serum sodium: level of serum sodium in the blood (mEq/L)
- smoking: if the patient smokes or not (boolean)
- time: follow-up period (days)
- DEATH_EVENT: if the patient died during the follow-up period (boolean)

## c. Models used
The following machine learning classification models were implemented and evaluated using the same dataset. The evaluation metrics used for comparison are Accuracy, AUC Score, Precision, Recall, F1 Score, and Matthews Correlation Coefficient (MCC).
1. Logistic Regression 
2. Decision Tree Classifier 
3. K-Nearest Neighbor Classifier 
4. Naive Bayes Classifier (Gaussian) 
5. Ensemble Model - Random Forest 
6. Ensemble Model - XGBoost

###  Comparison Table

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|-------------|--------------|-----|----------|--------|---------|-----|
| Logistic Regression | 0.856 | 0.886 | 0.797 | 0.696 | 0.743 | 0.647 |
| Decision Tree Classifier | 0.951 | 0.947 | 0.902 | 0.937 | 0.919 | 0.884 |
| K-Nearest Neighbor Classifier | 0.852 | 0.936 | 0.917 | 0.557 | 0.693 | 0.636 |
| Naive Bayes Classifier (Gaussian) | 0.799 | 0.850 | 0.703 | 0.570 | 0.629 | 0.499 |
| Random Forest (Ensemble) | 0.962 | 0.985 | 0.960 | 0.911 | 0.935 | 0.909 |
| XGBoost (Ensemble) | 0.936 | 0.984 | 0.943 | 0.835 | 0.886 | 0.844 |
