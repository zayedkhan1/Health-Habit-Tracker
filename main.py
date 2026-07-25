# main.py
import tkinter as tk
from health_tracker import HealthTracker
# from desgine import HealthApp

def main():
    tracker = HealthTracker('health.json')
    root = tk.Tk()
    # app = HealthApp(root, tracker)
    root.mainloop()

if __name__ == "__main__":
    main()