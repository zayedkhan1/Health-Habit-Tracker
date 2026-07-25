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
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')  # modern base theme

        # Configure colors
        style.configure('TFrame', background='#f0f4f8')
        style.configure('TLabel', background='#f0f4f8', foreground='#2c3e50', font=('Segoe UI', 10))
        style.configure('TButton', font=('Segoe UI', 10), padding=6)
        style.map('TButton',
                  background=[('active', '#3498db'), ('pressed', '#2980b9')],
                  foreground=[('active', 'white')])

        # Custom button styles
        style.configure('Success.TButton', background='#27ae60', foreground='white')
        style.map('Success.TButton',
                  background=[('active', '#2ecc71'), ('pressed', '#1e8449')])
        style.configure('Danger.TButton', background='#e74c3c', foreground='white')
        style.map('Danger.TButton',
                  background=[('active', '#c0392b'), ('pressed', '#922b21')])
        style.configure('Primary.TButton', background='#2c3e50', foreground='white')
        style.map('Primary.TButton',
                  background=[('active', '#34495e'), ('pressed', '#1a252f')])

        # Treeview styling
        style.configure('Treeview', background='white', foreground='#2c3e50',
                        rowheight=28, fieldbackground='white')
        style.map('Treeview', background=[('selected', '#3498db')])

        # Notebook tabs
        style.configure('TNotebook', background='#f0f4f8', tabmargins=[2, 5, 2, 0])
        style.configure('TNotebook.Tab', background='#d5dbe0', padding=[12, 4],
                        font=('Segoe UI', 10, 'bold'))
        style.map('TNotebook.Tab',
                  background=[('selected', '#2c3e50'), ('active', '#34495e')],
                  foreground=[('selected', 'white'), ('active', 'white')])

    # ---------- Add Record Tab ----------
    def setup_add_frame(self):
        fields = ['Date (YYYY-MM-DD)', 'Sleep (hours)', 'Water (glasses)',
                  'Exercise (minutes)', 'Screen Time (hours)', 'Study Hours (hours)']
        self.add_entries = {}

        # Title
        title = ttk.Label(self.add_frame, text="📝 Add or Update Daily Record",
                          font=('Segoe UI', 14, 'bold'), foreground='#2c3e50')
        title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        for i, field in enumerate(fields):
            label = ttk.Label(self.add_frame, text=field, font=('Segoe UI', 10))
            label.grid(row=i+1, column=0, padx=10, pady=8, sticky='e')
            entry = ttk.Entry(self.add_frame, width=25, font=('Segoe UI', 10))
            entry.grid(row=i+1, column=1, padx=10, pady=8)
            self.add_entries[field] = entry

        # Default date to today
        self.add_entries['Date (YYYY-MM-DD)'].insert(0, datetime.date.today().isoformat())

        # Buttons
        btn_frame = ttk.Frame(self.add_frame)
        btn_frame.grid(row=len(fields)+1, column=0, columnspan=3, pady=20)

        add_btn = ttk.Button(btn_frame, text="💾 Save Record", style='Success.TButton',
                             command=self.add_record)
        add_btn.pack(side='left', padx=10)

        clear_btn = ttk.Button(btn_frame, text="🗑️ Clear Fields", style='Primary.TButton',
                               command=self.clear_add_fields)
        clear_btn.pack(side='left', padx=10)

    def clear_add_fields(self):
        for key in self.add_entries:
            self.add_entries[key].delete(0, tk.END)
        self.add_entries['Date (YYYY-MM-DD)'].insert(0, datetime.date.today().isoformat())

    def add_record(self):
        date_str = self.add_entries['Date (YYYY-MM-DD)'].get().strip()
        if not dateValidation(date_str):
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
            return
        try:
            sleep = float(self.add_entries['Sleep (hours)'].get().strip())
            water = float(self.add_entries['Water (glasses)'].get().strip())
            exercise = float(self.add_entries['Exercise (minutes)'].get().strip())
            screen = float(self.add_entries['Screen Time (hours)'].get().strip())
            study = float(self.add_entries['Study Hours (hours)'].get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for all metrics.")
            return
        if any(v < 0 for v in [sleep, water, exercise, screen, study]):
            messagebox.showerror("Invalid Input", "Values cannot be negative.")
            return

        record = HealthRecord(date_str, sleep, water, exercise, screen, study)
        self.tracker.add_record(record)
        messagebox.showinfo("Success", "Record saved successfully.")
        self.clear_add_fields()
       
       
         # ---------- View Records Tab ----------
    def setup_view_frame(self):
        # Treeview with alternating row colors
        self.tree = ttk.Treeview(self.view_frame, columns=('Date', 'Sleep', 'Water',
                                                           'Exercise', 'Screen', 'Study'),
                                 show='headings', selectmode='browse')
        for col in ['Date', 'Sleep', 'Water', 'Exercise', 'Screen', 'Study']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor='center')

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.view_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side='left', fill='both', expand=True, padx=(0, 5))
        scrollbar.pack(side='right', fill='y')

        # Button panel
        btn_panel = ttk.Frame(self.view_frame)
        btn_panel.pack(fill='x', pady=10)

        ttk.Button(btn_panel, text="🔄 Refresh", style='Primary.TButton',
                   command=self.refresh_view).pack(side='left', padx=5)
        ttk.Button(btn_panel, text="✏️ Edit Selected", style='Primary.TButton',
                   command=self.edit_record).pack(side='left', padx=5)
        ttk.Button(btn_panel, text="🗑️ Delete Selected", style='Danger.TButton',
                   command=self.delete_record).pack(side='left', padx=5)

        self.refresh_view()

   
        # Bind double-click to edit
        self.tree.bind('<Double-1>', lambda e: self.edit_record())

    def refresh_view(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        records = sorted(self.tracker.get_all_records(), key=lambda r: r.date)
        for rec in records:
            # Alternate row colors are handled by the theme's 'alternate' style
            self.tree.insert('', 'end', values=(rec.date, rec.sleep, rec.water,
                                                rec.exercise, rec.screen_time, rec.study_hour))

    def edit_record(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Please select a record to edit.")
            return
        values = self.tree.item(selected[0], 'values')
        date = values[0]

        # Create edit window
        edit_win = tk.Toplevel(self.root)
        edit_win.title("✏️ Edit Record")
        edit_win.geometry("400x350")
        edit_win.configure(bg='#f0f4f8')
        edit_win.transient(self.root)  # make it modal-like
        edit_win.grab_set()

        fields = ['Sleep (hours)', 'Water (glasses)', 'Exercise (minutes)',
                  'Screen Time (hours)', 'Study Hours (hours)']
        entries = {}

        label_title = ttk.Label(edit_win, text=f"Editing record for {date}",
                                font=('Segoe UI', 12, 'bold'), foreground='#2c3e50')
        label_title.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        for i, field in enumerate(fields):
            label = ttk.Label(edit_win, text=field, font=('Segoe UI', 10))
            label.grid(row=i+1, column=0, padx=10, pady=8, sticky='e')
            entry = ttk.Entry(edit_win, width=25, font=('Segoe UI', 10))
            entry.grid(row=i+1, column=1, padx=10, pady=8)
            entry.insert(0, values[i+1])  # values[0] is date
            entries[field] = entry
