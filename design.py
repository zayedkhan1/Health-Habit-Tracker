# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from health_tracker import HealthTracker
from record import HealthRecord
from utility import dateValidation

class HealthApp:
    """Main GUI application with enhanced styling."""
    def __init__(self, root, tracker):
        self.root = root
        self.tracker = tracker
        self.root.title("Health Habit Tracker")
        self.root.geometry("950x700")
        self.root.configure(bg='#f0f4f8')

        # Configure ttk styles
        self.setup_styles()

        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Four tabs
        self.add_frame = ttk.Frame(self.notebook, padding=10)
        self.view_frame = ttk.Frame(self.notebook, padding=10)
        self.summary_frame = ttk.Frame(self.notebook, padding=10)
        self.warning_frame = ttk.Frame(self.notebook, padding=10)

        self.notebook.add(self.add_frame, text="➕ Add Record")
        self.notebook.add(self.view_frame, text="📋 View Records")
        self.notebook.add(self.summary_frame, text="📊 Summary")
        self.notebook.add(self.warning_frame, text="⚠️ Warnings")

        # Setup each tab
        self.setup_add_frame()
        self.setup_view_frame()
        self.setup_summary_frame()
        self.setup_warning_frame()
