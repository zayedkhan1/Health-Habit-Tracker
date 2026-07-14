import datetime


class HealthRecord:
    # constractor for daily recorded data
    def __init__(self,date=None,sleep=0,water=0,exercise=0,screen_time=0,study_hour=0):
        if date is None:
            date=datetime.date.today().isoformate()
            
        self.date=date
        self.sleep=sleep
        self.water=water
        self.exercise=exercise
        self.screen_time=screen_time
        self.study_hour=study_hour
    
    def json_data(self):
        return{
            'date':self.date,
            'sleep':self.sleep,
            'water' : self.water,
            'exercise':self.exercise,
            'screen_time': self.screen_time,
            'study_hour': self.study_hour,
        }
    
    @classmethod
    def store_data(cls,data):
           return cls(
            data['date'],
           data['sleep'],
           data['water'],
           data['exercise'],
           data['screen_time'],
           data['study_hours']
    )
    
