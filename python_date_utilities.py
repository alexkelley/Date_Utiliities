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
