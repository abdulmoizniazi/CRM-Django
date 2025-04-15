# 🧠 Django CRM App

This is a **Customer Relationship Management (CRM)** web application built using the Django framework. It provides core CRM features such as lead management, customer tracking, user authentication, and role-based access control. This project is designed to help businesses organize and manage customer data efficiently.

## 🚀 Features

- User registration and authentication
- Role-based user access (admin, agent)
- Lead creation, update, assignment, and deletion
- Admin dashboard to manage agents and leads
- Customizable lead categories and statuses
- Simple and clean user interface
- Fully functional backend built with Django

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (can be switched to PostgreSQL or others)
- **Frontend**: HTML, CSS (Bootstrap)
- **Deployment**: Compatible with Heroku / PythonAnywhere / EC2

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/abdulmoizniazi/CRM-Django.git
   cd CRM-Django
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Visit: `http://127.0.0.1:8000/`

## 📂 Project Structure

- `leads/`: Main app containing lead logic and views
- `agents/`: Handles agent management
- `templates/`: HTML files for rendering views
- `accounts/`: User authentication and registration
- `static/`: Static assets like CSS, images
- `crm/`: Django project settings and URL configuration

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📧 Contact

For any inquiries, contact: **abdulmoizniazi@gmail.com**

---

**Made with ❤️ by Moiz Khan**
```
