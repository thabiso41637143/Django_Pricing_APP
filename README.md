✨ Author
Thabiso Mathebula

# 🌐 Pricing Case Study Web App (Django Version)

This Django project presents an interactive web interface to consolidate financial data across multiple banking products and compute client profitability metrics.

---

## 🚀 Tech Stack
- Python 3.x
- Django 5.x
- HTML5 + Bootstrap 5

---

## ✅ Features

- Multi-product selection (Credit Card, Overdraft, Guarantee)
- Dynamic income statement calculation with:
  - LIBT
  - LIACC
  - ROE (Return on Equity)
- Beautiful Bootstrap-styled frontend
- Modular backend logic using Django views + forms

---

## 📦 Project Structure

DjangoPricingApp/
├── statements/
│ ├── views.py
│ ├── forms.py
│ ├── utils.py
│ └── templates/
│ └── statements/home.html
├── DjangoPricingApp/
│ └── settings.py
└── manage.py


---

## 🖥️ Running Locally

### 1. Clone the Repo

```bash
git clone https://github.com/thabiso41637143/Django_Pricing_APP.git
cd DjangoPricingApp

2. Install Dependencies

pip install -r requirements.txt


3. Run Migrations

python manage.py migrate

4. Run the Server

python manage.py runserver

Then visit http://localhost:8000


🌍 Deployment (Render)

This app can be deployed on Render. Make sure to include:

render.yaml

build.sh

requirements.txt

📌 Notes

Taxation rate is fixed at 27%

Core equity capital values are predefined per product

ROE is calculated as (LIBT - Tax) / Core Capital Holding



