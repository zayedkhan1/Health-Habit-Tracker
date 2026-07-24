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



    
