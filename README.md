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
