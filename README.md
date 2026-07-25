# 🏥 Health Habit Tracker

> A desktop application built with Python (Tkinter + NumPy) to track your daily health habits – sleep, water intake, exercise, screen time, and study hours – with weekly summaries and health warnings.

## 📌 Overview

**Health Habit Tracker** is a simple yet powerful Python GUI application that helps users monitor five key daily health metrics:

- ** Sleep** (hours)
- ** Water intake** (glasses)
- ** Exercise** (minutes)
- ** Screen time** (hours)
- ** Study hours** (hours)

Users can add records for any date, view past entries, edit or delete them, and obtain daily/weekly summaries with health warnings when metrics fall outside recommended ranges.

The project was developed as a team of three, following a **backend‑frontend‑integration** split, and showcases practical use of Python's core concepts including OOP, file I/O, exception handling, data structures, and the NumPy library.

---

## ✨ Features

| Feature                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **➕ Add Record**        | Enter values for a specific date (defaults to today). Validates input and saves. |
| **📋 View Records**     | Display all saved records in a sortable table.                              |
| **✏️ Edit Record**      | Select a record and update its metrics in a separate window.                |
| **🗑️ Delete Record**    | Remove a record with confirmation.                                          |
| **📆 Daily Summary**    | View all metrics for a chosen date.                                        |
| **📈 Weekly Summary**   | Compute averages and totals for the last 7 days (using NumPy).             |
| **⚠️ Health Warnings**  | Alerts when a metric is below or above the healthy range.                  |
| **💾 Persistent Storage**| All records are saved to `health.json` and loaded automatically on startup.|

---

## 🛠️ Technologies Used

| Technology      | Purpose                                           |
|-----------------|---------------------------------------------------|
| **Python 3.6+** | Core language                                     |
| **Tkinter**     | GUI framework (built-in)                          |
| **NumPy**       | Calculate weekly averages and sums efficiently    |
| **JSON**        | Lightweight data storage format                   |
| **Git**         | Version control and team collaboration            |



## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Health-Habit-tracker.git
   cd Health-Habit-tracker
  
   pip install numpy

# Run the application from
python main.py
