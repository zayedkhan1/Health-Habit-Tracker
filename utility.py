import datetime


def dateValidation(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False


