import datetime
import calendar


def _next_month():
    today = datetime.date.today()
    year = today.year + today.month / 12
    month = today.month % 12 + 1
    day = min(today.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def _get_time(datetime_obj):
    hour = datetime_obj.hour
    minute = datetime_obj.minute
    if minute < 10:
        strminute = '0' + str(minute)
    else:
        strminute = str(minute)
    if hour > 12:
        mhour = (hour - 12)
        return str(mhour) + ':' + strminute + ' PM'
    elif hour == 12:
        return str(hour) + ':' + strminute + ' PM'
    elif hour == 0:
        return '12:' + strminute + ' AM'
    else:
        return str(hour) + ':' + strminute + ' AM'