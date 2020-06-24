# convert_time

days_per_gregorian_year = 365.2425
days_per_nonleap_year = 365.0
hours_per_day = 24.0
minutes_per_hour = 60.0
seconds_per_minute = 60.0
seconds_per_hour = seconds_per_minute * minutes_per_hour
seconds_per_day = seconds_per_hour * hours_per_day


identity = lambda x: x


def days_to_gregorian_years(days):
    return days / days_per_gregorian_year


def days_to_nonleap_years(days):
    return days / days_per_nonleap_year


def gregorian_years_to_days(years):
    return years * days_per_gregorian_year


def nonleap_years_to_days(years):
    return years * days_per_nonleap_year


def seconds_to_gregorian_years(secs):
    return secs / (seconds_per_day * days_per_gregorian_year)


def seconds_to_nonleap_years(secs):
    return secs / (seconds_per_day * days_per_nonleap_year)


def gregorian_years_to_seconds(years):
    return years * (seconds_per_day * days_per_gregorian_year)


def nonleap_years_to_seconds(years):
    return years * (seconds_per_day * days_per_nonleap_year)


