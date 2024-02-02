import calendar

calendar_data = {
    'january': 31,
    'february': 29,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31,
}

calendar_obj = calendar.TextCalendar()

month = calendar_obj.formatmonth(2023, 1)
print(month, end='')
