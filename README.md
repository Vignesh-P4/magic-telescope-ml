
# 🔭 MAGIC Telescope ML Project

This project uses machine learning to classify gamma ray vs hadron events based on data from the MAGIC gamma-ray telescope. It includes data preprocessing, model training, evaluation, and a deployable Streamlit app.

![Streamlit App Screenshot](https://github.com/Vignesh-P4/magic-telescope-ml/blob/main/Screenshot%202025-07-06%20165233.png)

---

## 📌 Overview

- 🎯 Goal: Classify particles as **gamma** or **hadron**
- 💡 ML Algorithm: **Random Forest Classifier**
- 🎓 Dataset: MAGIC Gamma Telescope Data from UCI ML Repository
- 📈 Accuracy Achieved: ~88%
- 🧑‍💻 Streamlit App: Realtime prediction frontend

---

## 📁 Project Structure

```
magic-telescope-ml/
├── data/
│   └── magic04.data
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_evaluation.ipynb
├── models/
│   └── model.pkl
├── app/
│   └── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset Details

- **Source**: [UCI ML Repository – MAGIC Gamma Telescope Data Set](https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope)
- **Total Rows**: 19,020
- **Features**: 10 continuous numerical values
- **Target**:  
  - `g` for gamma (signal)  
  - `h` for hadron (background)

---

## ⚙️ Machine Learning Pipeline

1. Data Cleaning
2. Label Encoding (`g` → Gamma, `h` → Hadron)
3. Train/Test Split (80/20)
4. Model: Random Forest Classifier
5. Evaluation Metrics: Accuracy, Precision, Recall, F1-Score

### 📊 Classification Report (Sample):

```
              precision    recall  f1-score   support
      Hadron       0.87      0.77      0.82      1344
       Gamma       0.88      0.94      0.91      2460
    accuracy                           0.88      3804
   macro avg       0.88      0.85      0.86      3804
weighted avg       0.88      0.88      0.88      3804
```

---

## 💻 Streamlit Web App

### 🖥️ Run Locally

```bash
# Clone the repository
git clone https://github.com/Vignesh-P4/magic-telescope-ml.git
cd magic-telescope-ml

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/streamlit_app.py
```

### 🌐 Hosted Version (optional)
🔗 Streamlit App (deploy this if needed)

---

## 🤖 Model

The trained Random Forest model is saved at:

```
models/model.pkl
```

It is used by the Streamlit app to make real-time predictions.

---

## 🧰 Tech Stack

| Tool        | Purpose           |
|-------------|-------------------|
| Python      | Core programming  |
| Pandas      | Data handling     |
| Scikit-learn| Model building    |
| Streamlit   | Web UI            |
| Git & GitHub| Version control   |

---

## 👨‍💻 Author

**Vignesh Pobbathi**  
📫 [GitHub](https://github.com/Vignesh-P4) | [LinkedIn]([https://www.linkedin.com/in/vignesh-p4](https://www.linkedin.com/in/vigneshpobbathi/))

---

## 🔗 GitHub Repository

[https://github.com/Vignesh-P4/magic-telescope-ml](https://github.com/Vignesh-P4/magic-telescope-ml)
