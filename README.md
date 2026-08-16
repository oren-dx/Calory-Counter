# Calory-Counter
# 🔥 Django Calorie & BMR Tracking System

🚀 Live Website:
https://calory-counter.onrender.com/

A simple **Django-based Calorie and BMR Tracking System** that allows users to manage their basic personal information and keep track of daily calorie consumption.

The system uses a custom Django user model and provides separate functionality for storing user information such as **age, gender, height, weight, and BMR**, along with a calorie consumption history.

---

## ✨ Features

### 👤 User Management

The project uses a custom user model based on Django's `AbstractUser`.

Users can authenticate using Django's built-in authentication system.

Each user can have one associated basic information profile.

---

### 📋 Basic Information

Users can store their personal and physical information, including:

* Name
* Age
* Gender
* Height
* Weight
* BMR (Basal Metabolic Rate)

The basic information is connected to the user through a `OneToOneField`.

---

### 🔥 BMR Tracking

The system stores the user's **Basal Metabolic Rate (BMR)**.

BMR represents the approximate amount of energy the body uses at rest.

The calculated BMR can be stored in:

```text
bmr
```

The project can be extended to automatically calculate BMR based on:

* Age
* Gender
* Height
* Weight

---

### 🍎 Calorie Consumption Tracking

Users can record the food or drink items they consume.

Each calorie record contains:

* Food/item name
* Calories
* Date of consumption
* User who consumed the item

Example:

```text
Breakfast - 350 calories
Lunch     - 650 calories
Apple     - 95 calories
Dinner    - 550 calories
```

---

# 🏗️ System Architecture

The project contains three main models:

```text id="3q8d1f"
                  UserModel
                  /      \
                 /        \
                ▼          ▼
       BasicInfoModel   ConsumedCalories
              │               │
              │               │
        User Information   Food/Calories
              │               │
              └───────┬───────┘
                      │
                    User
```

---

# 🔗 Model Relationships

### User → Basic Information

Each user can have one basic information profile:

```text id="f6k2x8"
UserModel
    │
    └── BasicInfoModel
          One-to-One
```

The profile can be accessed through:

```python id="p7w4q1"
user.user_info
```

---

### User → Consumed Calories

A user can have multiple calorie records:

```text id="m9r3cz"
UserModel
    │
    └── ConsumedCalories
          One-to-Many
```

Because the model uses:

```python id="j2v8ha"
related_name='user_calorie'
```

the user's calorie records can be accessed with:

```python id="r5n1kd"
user.user_calorie.all()
```

---

# 🧰 Technologies Used

* **Python**
* **Django**
* **Django ORM**
* **SQLite / PostgreSQL**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Bootstrap** *(if used in the frontend)*

---

# 📁 Main Models

## 👤 `UserModel`

Custom user model extending Django's `AbstractUser`.

It currently uses Django's standard authentication fields such as:

```text
username
password
email
first_name
last_name
```

The model can be extended with additional fields as the project grows.

---

## 📋 `BasicInfoModel`

Stores the user's basic physical information.

Fields:

```text id="u3k7pb"
user
name
age
gender
height
weight
bmr
```

Available gender choices:

```text id="b8x5vm"
Male
Female
```

The model has a one-to-one relationship with `UserModel`.

---

## 🍎 `ConsumedCalories`

Stores the user's consumed food and calorie information.

Fields:

```text id="q4s9wt"
item_name
calorie
created_at
consumed_by
```

Each calorie record belongs to a specific user.

---

# 🔥 BMR Calculation

The project stores BMR in the `BasicInfoModel`.

A common approach is to calculate BMR using the **Mifflin-St Jeor equation**.

For males:

```text id="n7p3za"
BMR = (10 × weight) + (6.25 × height) - (5 × age) + 5
```

For females:

```text id="w2k8yd"
BMR = (10 × weight) + (6.25 × height) - (5 × age) - 161
```

Where:

```text
weight = kilograms
height = centimeters
age    = years
```

Example:

```text id="d5m1vx"
Weight = 70 kg
Height = 175 cm
Age    = 25

BMR ≈ 1674 calories/day
```

> **Note:** BMR is an estimate, not a medical diagnosis or individualized medical recommendation.

---

# 🍽️ Calorie Tracking Workflow

The basic workflow is:

```text id="x8v2nm"
             USER
              │
              ▼
       Create Account
              │
              ▼
      Add Basic Information
              │
              ├── Name
              ├── Age
              ├── Gender
              ├── Height
              ├── Weight
              └── BMR
              │
              ▼
        Track Food Intake
              │
              ▼
       Add Consumed Item
              │
              ├── Item Name
              └── Calories
              │
              ▼
        Save Calorie Record
              │
              ▼
       View Calorie History
```

---

# 📊 Example Calorie Records

A user could have records such as:

```text id="e7k4qs"
-------------------------------------
Food Item       Calories
-------------------------------------
Egg             78 kcal
Banana          105 kcal
Rice            200 kcal
Chicken         250 kcal
Apple           95 kcal
-------------------------------------
Total           728 kcal
```

The application can calculate the daily total using Django aggregation.

For example:

```python id="v3q9rx"
from django.db.models import Sum

total_calories = ConsumedCalories.objects.filter(
    consumed_by=user
).aggregate(
    total=Sum('calorie')
)
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash id="c4x8mz"
git clone https://github.com/your-username/your-repository-name.git
```

Navigate to the project:

```bash id="s7n2pk"
cd your-repository-name
```

---

## 2. Create a Virtual Environment

### Windows

```bash id="j6r4vx"
python -m venv venv
```

Activate it:

```bash id="t8q3nw"
venv\Scripts\activate
```

### Linux / macOS

```bash id="z5m1cy"
python3 -m venv venv
```

Activate it:

```bash id="h9k6qs"
source venv/bin/activate
```

---

## 3. Install Dependencies

If `requirements.txt` exists:

```bash id="r3v7px"
pip install -r requirements.txt
```

Otherwise:

```bash id="n8c4wa"
pip install django
```

Then create the requirements file:

```bash id="k5m2fz"
pip freeze > requirements.txt
```

---

# 🔐 Configure Custom User Model

Because the project uses a custom user model, add the following to `settings.py`:

```python id="x2q7mc"
AUTH_USER_MODEL = 'your_app_name.UserModel'
```

For example, if your Django application is called `calorie`:

```python id="w6p3zn"
AUTH_USER_MODEL = 'calorie.UserModel'
```

Replace `calorie` with your actual app name.

> **Important:** It is best to configure `AUTH_USER_MODEL` before creating the project's initial migrations.

---

# 🗄️ Database Setup

Create migrations:

```bash id="g8v2rs"
python manage.py makemigrations
```

Apply migrations:

```bash id="u4x9nk"
python manage.py migrate
```

---

# 👨‍💻 Create Superuser

Create a Django administrator:

```bash id="m3q7yb"
python manage.py createsuperuser
```

Follow the instructions to create the account.

---

# ▶️ Run the Project

Start the Django development server:

```bash id="p6w1cz"
python manage.py runserver
```

Open the application:

```text id="a9r4xm"
http://127.0.0.1:8000/
```

Django Admin:

```text id="y2k8vs"
http://127.0.0.1:8000/admin/
```

---

# 📂 Recommended Project Structure

```text id="n5x7qp"
calorie-tracker/
│
├── manage.py
│
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── calorie/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── templates/
├── static/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🔒 Security Recommendations

Before deploying this project to production:

* Set `DEBUG = False`
* Use a secure `SECRET_KEY`
* Configure `ALLOWED_HOSTS`
* Store secrets in environment variables
* Use PostgreSQL for production
* Enable HTTPS
* Add authentication to calorie-related views
* Ensure users can only access their own calorie records
* Validate calorie values
* Validate age, height, and weight values
* Use appropriate database constraints
* Avoid exposing personal user information

Example `.gitignore`:

```text id="q7v3mx"
venv/
__pycache__/
*.pyc
db.sqlite3
.env
staticfiles/
```

---

# 🔮 Future Improvements

The project can be extended with:

* 📊 Daily calorie dashboard
* 📅 Weekly and monthly calorie history
* 📈 Calorie consumption charts
* 🔥 Automatic BMR calculation
* ⚡ TDEE calculation
* 🎯 Daily calorie goals
* ⚖️ Weight tracking
* 📉 Weight progress charts
* 🍎 Food database
* 🥗 Meal planning
* 🥘 Breakfast/lunch/dinner categorization
* 🔔 Calorie goal notifications
* 📱 Responsive mobile interface
* 📊 User statistics dashboard
* 📥 Export calorie history
* 🔐 REST API using Django REST Framework

---

# 📌 Example User Profile

```text id="c8m4vz"
Name       : John Doe
Age        : 25
Gender     : Male
Height     : 175 cm
Weight     : 70 kg
BMR        : 1674 kcal/day
```

---

# 📌 Example Daily Calorie History

```text id="j6p2wr"
Date: August 11, 2026

Breakfast
├── Eggs       156 kcal
└── Banana     105 kcal

Lunch
├── Rice       250 kcal
└── Chicken    300 kcal

Snack
└── Apple       95 kcal

-------------------------
Total:         906 kcal
```

---

# 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

### 2. Create a new branch

```bash id="v8n5qa"
git checkout -b feature/new-feature
```

### 3. Make your changes

### 4. Commit your changes

```bash id="s4m7xy"
git add .
git commit -m "Add new feature"
```

### 5. Push your branch

```bash id="k9p2zw"
git push origin feature/new-feature
```

### 6. Create a Pull Request

---

# 📄 License

This project is developed for **educational and development purposes**.

You can add an **MIT License** or another open-source license depending on your requirements.

---

# 👨‍💻 Author

**Your Name**

If you find this project useful, please ⭐ the repository on GitHub.

---
