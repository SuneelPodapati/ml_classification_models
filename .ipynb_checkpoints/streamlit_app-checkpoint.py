import streamlit as st
import joblib
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay 
import matplotlib.pyplot as plt


st.title("Heart Failure Prediction 🫀 ")
st.markdown(":rainbow[A Classification Models Evaluation Assignment]")

st.markdown("""
Interactively explore 6 trained classification models performance for [`Heart Failure Prediction`](https://www.kaggle.com/datasets/aadarshvelu/heart-failure-prediction-clinical-records) data from Kaggle.

The trained models are: 
1. Logistic Regression 
2. Decision Tree Classifier 
3. K-Nearest Neighbor Classifier 
4. Naive Bayes Classifier (Gaussian) 
5. Ensemble Model - Random Forest 
6. Ensemble Model - XGBoost 
""")
st.divider()

test_file_path = "data/test_data.csv"

with open(test_file_path, "rb") as file:
    test_data = file.read()

left, right = st.columns([3,1.2], vertical_alignment="center")

left.caption("Select a model and upload the test data to view the evaluation metrics for the model.")

right.download_button(
    label="Download test data",
    icon=":material/download:",
    data=test_data,
    file_name="test_data.csv",
    mime="text/csv"
)

models = {
    "Logistic Regression": "model/logistic_regression.pkl",
    "Decision Tree Classifier": "model/decision_tree.pkl",
    "K-Nearest Neighbor Classifier": "model/knn.pkl",
    "Naive Bayes Classifier (Gaussian)": "model/gaussian_nb.pkl",
    "Ensemble Model - Random Forest": "model/random_forest.pkl",
    "Ensemble Model - XGBoost": "model/xgboost.pkl"
}

selected_model = st.selectbox("Select Model", models.keys(), index=None, key="selected_model")
uploaded_file = st.file_uploader("Upload test data file for model evaluation", type="csv", key="uploaded_file")

if selected_model is None: 
    st.toast("Please select a model.", icon="🚨")

elif uploaded_file is None: 
    st.toast("Please upload a test CSV file.", icon="🚨")

else: 
	try: 
		X_test = pd.read_csv(uploaded_file) 
	except Exception as e: 
		st.toast(f"Error reading CSV: {e}", icon="🔥")
	
	if X_test.shape[1] != 12: 
		st.toast(f"Expected 12 columns in test file, but found {X_test.shape[1]}.", icon="🔥")
	
	try: 
		pkl_path = models[selected_model]
		with open(pkl_path, "rb") as pkl: 
			model = joblib.load(pkl) 
	except Exception as e: 
		st.error(f"Error loading model: {e}") 
	
	
	y_pred = model.predict(X_test)
	y_test = pd.read_csv("./data/test_target_data.csv") 
	
	cm = confusion_matrix(y_test, y_pred) 
	fig, ax = plt.subplots() 
	disp = ConfusionMatrixDisplay(confusion_matrix=cm) 
	ax.set_title("Confusion Matrix", fontsize = 10)
	disp.plot(ax=ax, cmap="Blues", colorbar=False)
	st.pyplot(fig)

    