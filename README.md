# Python Command-Line Todo Manager

## 📌 Project Overview

The **Python Command-Line Todo Manager** is a lightweight terminal-based application designed to help users manage daily tasks efficiently. The application allows users to add, view, delete, and mark tasks as completed, with all data stored locally using a JSON file.

This project was developed as part of **INT 331 – Fundamentals of DevOps**, focusing on Python fundamentals and practical Git workflows.

---

## 🎯 Objectives

- Develop a practical Python-based command-line application
- Apply core Python concepts such as functions, lists, dictionaries, and file handling
- Practice Git operations including branching, merging, and conflict resolution
- Maintain clean documentation and a structured GitHub repository

---

## ⚙️ Features

- Add new tasks
- View all tasks with completion status
- Delete tasks by ID
- Mark tasks as completed
- Persistent local storage using `tasks.json`
- Simple and user-friendly CLI menu

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Editor:** Visual Studio Code
- **Version Control:** Git (Git Bash)
- **Repository Hosting:** GitHub
- **Data Storage:** JSON
- **Documentation:** Markdown

---

## 📂 Project Structure

```text
todo-manager/
│── todo.py
│── tasks.json
│── README.md
│── screenshots/
```

---



## ▶️ How to Run the Project

```bash
git clone <repository-url>
cd INT331_TODO_MANAGER
python todo.py
```

---



## 📋 How the Application Works

- Tasks are stored in a local `tasks.json` file
- Each task includes:

  - Unique ID
  - Task title
  - Completion status
- Input validation prevents crashes due to invalid user input
- Defensive checks handle missing or corrupted data files

  ---

## 🔁 Git Workflow Followed

- Initialized a local Git repository
- Created multiple feature branches
- Made frequent and meaningful commits
- Performed branch merges
- Intentionally created and resolved a merge conflict
- Pushed all branches to GitHub

---

## 🧠 Challenges Faced

- Managing persistent data using JSON
- Ensuring unique task IDs after deletions
- Handling merge conflicts during development
- Validating user input in a CLI environment

---

## ✅ Outcomes

- Fully functional command-line todo manager
- Practical experience with Git branching and merging
- Clean, readable, and modular Python code
- Well-documented GitHub repository with commit history

---

## 📸 Screenshots

Screenshots demonstrating application usage, Git logs, branches, and merge conflict resolution are available in the `screenshots/` directory.

---

## 🏁 Conclusion

This project enhanced my understanding of Python programming and version control using Git. It provided hands-on experience in building a real-world application while following DevOps-oriented development practices.

---

## 📚 References

- Official Python Documentation
- Git Command Documentation
- Markdown Formatting Guide
