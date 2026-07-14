import datetime

class HealthRecord:
    def __init__(self,date=None,sleep=0,water=0,exercise=0,screen_time=0,study_hour=0):
        if date is None:
            date=datetime.date.today().isoformate()
            self.date=date
            self.sleep=sleep
            self.water=water
            self.exercise=exercise
            self.screen_time=screen_time
            self.study_hour=study_hour