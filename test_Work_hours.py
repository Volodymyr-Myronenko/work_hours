import Work_hours

def test_Work_hours_1():
    start = '2019-12-01 09:30:00'
    finish = '2019-12-07 12:15:00'
    assert Work_hours.count_working_hours(start, finish) == 40

def test_Work_hours_2():
    start = '2019-12-02 08:00:00'
    finish = '2019-12-04 12:15:00'
    assert Work_hours.count_working_hours(start, finish) == 19