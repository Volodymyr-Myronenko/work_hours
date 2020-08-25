import datetime

def count_working_hours(begin_ts: str, end_ts: str):
    """
    Function takes start and end timestamp-strings as arguments.
    Returns number of working hours between timestamps.
    Takes into account weekends and normal working time range of a day.

    Args:
        begin_ts (str): Beginning of count
        end_ts (str): End of count

    Returns:
        working hours (int): Number of full working hours between start and end
    """
    workday_start = datetime.datetime.strptime('9:00:00', '%H:%M:%S')
    workday_end = datetime.datetime.strptime('17:00:00', '%H:%M:%S')
    iso_weekend = [6, 7]
    seconds_in_hour = 3600
    
    begin_count = datetime.datetime.strptime(begin_ts, '%Y-%m-%d %H:%M:%S')
    end_count = datetime.datetime.strptime(end_ts, '%Y-%m-%d %H:%M:%S')
    
    working_hours = 0
    if begin_count > end_count:
        print('End timestamp is earlier than start')
        working_hours = None
    elif begin_count == end_count:
        print('Start and end timestamps are the same')
        working_hours = None
    else: 
        time_diff_hours = int((end_count-begin_count).total_seconds()) // seconds_in_hour
        datetimes = [begin_count + datetime.timedelta(seconds = seconds_in_hour) * x for x in range(time_diff_hours)]
        working_hours = len(list(filter(lambda x: (not (x.isoweekday() in iso_weekend)) and (x.hour in range(workday_start.hour, workday_end.hour)), datetimes)))
    return working_hours