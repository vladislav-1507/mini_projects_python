from datetime import datetime

def is_available_date(booked_dates, date_for_booking):
    pattern = '%d.%m.%Y'
    set_of_booked_dates, set_of_date_for_booking = set(), set()

    for cur_date in booked_dates:
        if '-' not in cur_date:
            set_of_booked_dates.add(datetime.strptime(cur_date, pattern))
        else:
            for_start = datetime.strptime(cur_date[:10], pattern)
            for_end = datetime.strptime(cur_date[11:], pattern)
            for cur_el in get_date_range(for_start, for_end):
                set_of_booked_dates.add(cur_el)

    if '-' not in date_for_booking:
        set_of_date_for_booking.add(datetime.strptime(date_for_booking, pattern))
    else:
        for_start1 = datetime.strptime(date_for_booking[:10], pattern)
        for_end1 = datetime.strptime(date_for_booking[11:], pattern)
        for cur_el in get_date_range(for_start1, for_end1):
            set_of_date_for_booking.add(cur_el)
    
    return set_of_booked_dates.isdisjoint(set_of_date_for_booking)
    

def get_date_range(start, end):
    res = []
    if start <= end:
        for i in range(start.toordinal(), end.toordinal() + 1):
            res.append(datetime.fromordinal(i))

    return res

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))