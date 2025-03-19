# Software Engineering with Python

## 📌 Overview
This repository contains best practices for **Software Engineering** using **Python**, covering:

- Concurrency and Multithreading
- Data Structures
- Microservices vs Monolithic Architecture
- Resilience and Fault Tolerance
- Unit vs Integration Testing
- Object-Oriented Programming (OOP)

## 📂 Project Structure
```
software_engineering_python/
│── src/  # Main source code
│   ├── main.py  # Entry point
│   ├── utils.py  # Helper functions
│   ├── services/
│   │   ├── database.py  # Database interaction
│   │   ├── api.py  # REST API interface
│── tests/  # Automated tests
│   ├── test_main.py  # Unit tests
│   ├── test_services.py  # Integration tests
│── docs/  # Documentation
│── notebooks/  # Jupyter Notebooks for analysis
│── pyproject.toml  # Poetry dependency management
│── README.md  # Project documentation
│── requirements.txt  # Dependencies for non-Poetry users
│── .gitignore  # Files ignored in the repository
│── .pre-commit-config.yaml  # Pre-commit hooks
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/orenatobr/software_engineering_data_science.git
cd software_engineering_data_science
```

### 2️⃣ Install Dependencies (Poetry Recommended)
```bash
poetry install
```

### 3️⃣ Run the Application
```bash
poetry run python src/main.py
```

### 4️⃣ Run Tests
```bash
poetry run pytest tests/
```

### 5️⃣ Set Up Pre-Commit Hooks
To ensure code quality before every commit:
```bash
pre-commit install
pre-commit run -a
```

## 🔥 Future Enhancements
- Advanced Concurrency Patterns
- Design Patterns in Python
- Cloud Deployment Best Practices
