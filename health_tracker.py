import numpy as np
import json
import os
from datetime import datetime, timedelta
from record import HealthRecord


class HealthTracker:

    def __init__(self,filename='health.json'):
        self.filename=filename
        self.records=[]
        self.load_data()



    def add_record(self,record):
        for old_record in self.records:
            if old_record.date == record.date:
                self.records.remove(old_record)
                self.records.append(record)
                self.save_data()
                return

        self.records.append(record)
        self.save_data()

    # def get_record(self,date):
    #     for record in self.records:
    #         if record.date==date:
    #             return record
    #         else:
    #             return None
    #     return None    

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
            
        if self.record.study_hour < 2:
            self.warnings.append("Study hours are too low.")
        elif self.record.study_hour > 4:
            self.warnings.append("Study hours are too high.")
    
        return self.warnings
        
    def save_data(self):
        data = []
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
    
            
    

    def daily_summary(self, date):
        """Return a dictionary summary for a single day, or None if no record."""
        record = self.get_record(date)
        if record:
            return record.json_data()
        return None


    def weekly_summary(self, end_date=None):
      
        weekly_data = self.get_weekly_records(end_date)
        if not weekly_data:
            return None

        sleep = []
        water = []
        exercise = []
        screen = []
        study = []

        for record in weekly_data:
            sleep.append(record.sleep)
            water.append(record.water)
            exercise.append(record.exercise)
            screen.append(record.screen_time)
            study.append(record.study_hour)

        sleep_time = np.array(sleep)
        water_consume = np.array(water)
        exercise_time = np.array(exercise)
        screen_time = np.array(screen)
        study_hour = np.array(study)

        avg_sleep = np.mean(sleep_time)
        avg_water = np.mean(water_consume)
        avg_exercise = np.mean(exercise_time)
        avg_screen = np.mean(screen_time)
        avg_study = np.mean(study_hour)

        total_sleep = np.sum(sleep_time)
        total_water = np.sum(water_consume)
        total_exercise = np.sum(exercise_time)
        total_screen = np.sum(screen_time)
        total_study = np.sum(study_hour)

        return {
            'average': {
                'sleep': avg_sleep,
                'water': avg_water,
                'exercise': avg_exercise,
                'screen_time': avg_screen,
                'study_hours': avg_study
            },
            'total': {
                'sleep': total_sleep,
                'water': total_water,
                'exercise': total_exercise,
                'screen_time': total_screen,
                'study_hours': total_study
            },
            'numOfDays': len(weekly_data)
        }
    

    