# -Restaurant-Popularity-Predictor-ML

# 🍽️ Restaurant Popularity Predictor

A Machine Learning web application that predicts the popularity of a restaurant based on key factors such as ratings, reviews, cost, votes, and delivery time.

The system analyzes how different attributes influence restaurant success and customer preference.

---

## 🚀 Features

- Predict restaurant popularity score  
- User-friendly interactive interface  
- Real-time ML prediction  
- Input controls for restaurant attributes  
- Instant prediction result  
- Practical business insights  

---

## 🧠 Machine Learning Approach

The model predicts restaurant popularity using structured features:

- Location  
- Votes  
- Average Cost  
- Reviews Count  
- Rating  
- Delivery Time  

**Workflow:**

1. Data preprocessing  
2. Feature encoding  
3. Model training  
4. Prediction  
5. Web deployment  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Streamlit  
- Machine Learning  

---

## 📊 Input Parameters

| Feature | Description |
|---------|------------|
| Location | Restaurant city |
| Votes | Number of user votes |
| Average Cost | Cost for two |
| Reviews Count | Number of reviews |
| Rating | Average rating |
| Delivery Time | Delivery duration (minutes) |

---

## ✅ Example Test Cases

### 🔻 Low Popularity Restaurant

- Votes: 5  
- Average Cost: 1500  
- Reviews Count: 3  
- Rating: 2.5  
- Delivery Time: 60  

**Expected:** Low popularity  

---

### 🔺 High Popularity Restaurant

- Votes: 500  
- Average Cost: 300  
- Reviews Count: 200  
- Rating: 4.5  
- Delivery Time: 25  

**Expected:** High popularity  

---

## 📈 Model Behavior

Popularity increases with:

- Higher rating  
- More votes  
- More reviews  

Popularity decreases with:

- Higher cost  
- Longer delivery time  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
