import numpy as np
import json
import os
import datetime
from record import HealthRecord

class HealthTracker:

    def __init__(self,filename='health_tracker.py'):
        self.filename=filename
        self.records=[]



    def add_record(self,record):
        for old_record in self.records:
            if old_record.date == record.date:
                self.records.remove(old_record)
                self.records.append(record)
                self.save_data()
                return

        self.records.append(record)
        self.save_data()

    def get_record(self,date):
        for record in self.records:
            if record.date==date:
                return record
            else:
                return None
        return None    
              
    
    def delete_record():
        pass

    def get_all_record():
        pass

    
    def get_dates_set():
        pass

    def get_weekly_records():
      pass

    def save_data():
        pass
    from datetime import datetime, timedelta

def get_record(self, date):
    
    for record in self.records:
        if record.date == date:
            return record
    return None


def delete_record(self, date):
    
    new_records = []

    for record in self.records:
        if record.date != date:
            new_records.append(record)

    self.records = new_records
    self.save_data()

def get_all_records(self):
    
    return self.records


def get_dates_set(self):
    
    dates = set()

    for record in self.records:
        dates.add(record.date)

    return dates


def get_weekly_records(self, end_date=None):
    

    if end_date is None:
        end_date = datetime.today().date()
    else:
        if type(end_date) == str:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    start_date = end_date - timedelta(days=6)

    weekly_records = []

    for record in self.records:
        current_date = datetime.strptime(record.date, "%Y-%m-%d").date()

        if current_date >= start_date and current_date <= end_date:
            weekly_records.append(record)

    return weekly_records

    
