#! /usr/bin/env python3

from dateutil import relativedelta
import datetime


def increment_month(when, direction, number):
    '''
    Change a datetime to the same day in a different month.
    Takes a datetime, direction (back or forward) and number of months
    Returns a datetime
    '''
    if direction == 'back':
        return when - relativedelta.relativedelta(months=number)
    else:
        return when + relativedelta.relativedelta(months=number)


def start_of_day(when):
    '''
    Takes a datetime
    Returns the datetime rounded to the start of the day
    '''
    return datetime.datetime(*when.timetuple()[:3])


def first_day_of_month(when):
    '''
    Takes a datetime
    Returns the first day of the month of the datetime rounded to the start of the day
    '''
    return start_of_day(when - datetime.timedelta(days=when.day-1))


def last_day_of_month(when):
    '''
    Takes a datetime
    Returns the last moment of the month of the datetime
    '''
    return datetime.datetime(when.year, when.month, when.day, 23, 59, 59) + relativedelta.relativedelta(day=31)


def diff_month(d1, d2):
    '''
    Takes two datetime objects

    Returns the number of months between them.  If they are the same month, 1 is
    returned.
    '''
    return (d1.year - d2.year)*12 + d1.month - d2.month

# assert diff_month(datetime.datetime(2010,10,1), datetime.datetime(2010,9,1)) == 1
# assert diff_month(datetime.datetime(2010,10,1), datetime.datetime(2009,10,1)) == 12
# assert diff_month(datetime.datetime(2010,10,1), datetime.datetime(2009,11,1)) == 11
# assert diff_month(datetime.datetime(2010,10,1), datetime.datetime(2009,8,1)) == 14
# assert diff_month(datetime.datetime(2016,05,15), datetime.datetime(2015,10,15)) == 7 
# assert diff_month(datetime.datetime(2016,05,01), datetime.datetime(2012,12,01)) == 41
