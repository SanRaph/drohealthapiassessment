from datetime import *
import math


def date_converter(date_as_string):
    dates = date_as_string.split("-")
    split_date = [int(item) for item in dates]
    try:
        new_date = date(split_date[0], split_date[1], split_date[2])
        return new_date
    except ValueError:
        return f'{date.today().year} {date.today().month} {date.today().day}'


def period_start_dates_estimate(last_period, cycle_averages, start_date_str, end_date_str):
    last_period_date = date_converter(last_period)
    end_date = date_converter(end_date_str)
    start_date = date_converter(start_date_str)
    if last_period_date > start_date:
        return {'msg': 'Estimation not in range'}
    if start_date > end_date:
        return {'msg': 'Estimation not in range'}
    date_list = []
    while last_period_date < end_date:
        cycle_average = timedelta(days=cycle_averages)
        last_period_date = last_period_date + cycle_average
        if start_date <= last_period_date <= end_date:
            date_list.append(last_period_date)
    return date_list


def check_date_between_range(start_date, check_date, end_date):
    date_range = (end_date - start_date).days
    date_diff = (check_date - start_date).days
    if date_diff > 0 and date_diff < date_range:
        return True
    return False


def period_start_list(last_period, cycle_averages, start_date_str, end_date_str):
    last_period_date = date_converter(last_period)
    end_date = date_converter(end_date_str)
    start_date = date_converter(start_date_str)
    if last_period_date > start_date:
        return {'msg': "date not within range"}
    if start_date > end_date:
        return {'msg': "date not within range"}
    date_list = []
    while last_period_date <= end_date:
        cycle_average = timedelta(days=cycle_averages)
        last_period_date = last_period_date + cycle_average
        date_list.append(last_period_date)
    return (date_list)


def get_closest_date(cycle_event_date, last_period, cycle_averages, start_date_str, end_date_str):
    event_date = date_converter(cycle_event_date)
    end_date = date_converter(end_date_str)
    start_date = date_converter(start_date_str)
    if event_date < start_date:
        return {"error": "date not in range"}
    if event_date > end_date:
        return {"error": "date not in range"}
    date_list = period_start_list(last_period, cycle_averages, start_date_str, end_date_str)
    cloz_dict = {abs(event_date - date): date
                 for date in date_list}
    res = cloz_dict[min(cloz_dict.keys())]
    res_check = (event_date - res).days
    if res_check < 0:
        res_index = date_list.index(res)
        last_period_date = date_list[res_index - 1]
        return [last_period_date, res]
    else:
        res_index = date_list.index(res)
        next_period_date = date_list[res_index + 1]
        return [res, next_period_date]


def predict_cycle_event(last_period, cycle_date, cycle_average, period_average, next_period):
    cycle_event_date = date_converter(cycle_date)
    if cycle_event_date == last_period:
        return {'event': 'period_start_date', 'date': cycle_event_date}
    period_end_date = last_period + timedelta(days=period_average)
    if cycle_event_date == period_end_date:
        return {'event': 'period_start_date', 'date': cycle_event_date}
    period = check_date_between_range(last_period, cycle_event_date, period_end_date)
    if period:
        return {'event': 'in_period', 'date': cycle_event_date}
    cycle_avg = math.floor(cycle_average / 2)
    ovulation_date = last_period + timedelta(days=cycle_avg)
    if cycle_event_date == ovulation_date:
        return {'event': 'ovulation_date', 'date': cycle_event_date}
    fertility_window_begins = ovulation_date - timedelta(days=5)
    fertility_window_ends = ovulation_date + timedelta(days=5)
    fore_fertility = check_date_between_range(fertility_window_begins, cycle_event_date, ovulation_date)
    if fore_fertility:
        return {'event': 'fertility_window', 'date': cycle_event_date}
    next_fertility = check_date_between_range(ovulation_date, cycle_event_date, fertility_window_ends)
    if next_fertility:
        return {'event': 'fertility_window', 'date': cycle_event_date}
    pre_ovulation_ends = ovulation_date - timedelta(days=4)
    pre_ovulation_window = check_date_between_range(period_end_date, cycle_event_date, pre_ovulation_ends)
    if pre_ovulation_window:
        return {'event': 'pre_ovulation_window', 'date': cycle_event_date}
    post_ovulation_starts = ovulation_date + timedelta(days=4)
    post_ovulation_window = check_date_between_range(post_ovulation_starts, cycle_event_date, next_period)
    if post_ovulation_window:
        return {'event': 'post_ovulation_window', 'date': cycle_event_date}
    if cycle_event_date == next_period:
        return {'event': 'period_start_date', 'date': cycle_event_date}
    else:
        return {'event': 'date_not_in_range', 'date': cycle_event_date}
