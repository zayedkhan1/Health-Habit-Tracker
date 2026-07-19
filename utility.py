import datetime


def dateValidation(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False


def NumberValidation(number):
    try:
        number = float(number)

        if number >= 0:
            return True
        else:
            return False

    except:
        return False