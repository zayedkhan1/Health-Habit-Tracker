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

    def get_all_records():
        pass

    def get_dates_set():
        pass

    def get_weekly_records():
      pass


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
            study.append(record.study_hours)

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
    
    def get_warnings(self, date=None):

        if date is None:
            date = datetime.today().date().isoformat()

        record = self.get_record(date)

        warnings = []

        if record is None:
            return warnings

        if record.sleep < 7:
            warnings.append("Sleep is too low.")
        elif record.sleep > 9:
            warnings.append("Sleep is too high.")

      
        if record.water < 8:
            warnings.append("Water intake is too low.")
        elif record.water > 12:
            warnings.append("Water intake is too high.")

        
        if record.exercise < 30:
            warnings.append("Exercise is too low.")
        elif record.exercise > 60:
            warnings.append("Exercise is too high.")

      
        if record.screen_time > 3:
            warnings.append("Screen time is too high.")

        
        if record.study_hours < 2:
            warnings.append("Study hours are too low.")
        elif record.study_hours > 4:
            warnings.append("Study hours are too high.")

        return warnings
