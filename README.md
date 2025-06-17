# 🏦 Online Banking System using Django

A secure, user-friendly online banking platform developed with Django. It allows users to manage bank accounts, perform transactions, and view history — all through a responsive web interface.

---

## 🚀 Features

- **User Authentication**  
  Secure user registration, login, logout, and profile management.

- **Account Management**  
  View account balance, account details, and update profile information.

- **Transactions**  
  Deposit, withdraw, transfer funds, and view transaction history.

- **Loan Management**  
  Apply for loans, view loan status and history.

- **Customer Support**  
  Submit support tickets, view ticket status, and receive responses.

- **Notifications**  
  Receive and manage important alerts and notifications.

---

## 🛠 Tech Stack

- **Framework:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default), compatible with PostgreSQL/MySQL
- **Tools:** Django Admin, Django ORM, Django Authentication System

---

## 📁 Project Structure
## Project Structure

```plaintext
OnlineBankingSystem/
├── accounts/              # User account and profile management
│   └── templates/accounts/   # Base template
│   └── static/ accounts/  # styles.css
│       └──styles.css
├── banking/               # Deposit and withdrawal apps
│   └── templates/banking/
├── loans/                 # Loan management
│   └── templates/loans/
├── support/               # Customer support and ticket system
│   └── templates/support/
├── transactions/          # Transactions: transfer, history
│   └── templates/transactions/
├── manage.py              # Django project management script
├── db.sqlite3             # Default SQLite database
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/cosmicc0der78/OnlineBankingSystem.git
cd OnlineBankingSystem
```

### 2️⃣ Create and activate a virtual environment:

On macOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

On Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install required packages:

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply database migrations:

```bash
python manage.py migrate
```

### 5️⃣ Run the development server:

```bash
python manage.py runserver
```

### 6️⃣ Access the app in your browser:

Visit http://127.0.0.1:8000


## ✍️ Author

**Indu Sree Nanapu**  [GitHub](https://github.com/cosmicc0der78)      [Email](mailto:indusreen78@gmail.com)

> 📢 I'm open to collaborations, feedback, and contributing to exciting open-source adventures.  
> If you have ideas, suggestions, or just want to connect—feel free to reach out!

