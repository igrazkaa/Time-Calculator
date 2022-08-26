def add_time(start, duration, weekday=None):
    weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    start_hours = start.split(':')[0]
    start_minutes = start.split(':')[1].split()[0]
    start_meridiem = start.split()[-1]
    duration_hours = duration.split(':')[0]
    duration_minutes = duration.split(':')[1]

    if not start_hours.isdigit() or not start_minutes.isdigit() or start_meridiem not in ['AM', 'PM'] or int(
            start_hours) > 12 or int(start_minutes) > 59:
        raise ValueError('Start time should have the 12-hour clock format, e.g. 11:06 PM. Check your format.')

    if not duration_hours.isdigit() or not duration_minutes.isdigit():
        raise ValueError('Duration time should have 2 integers separated by colon, e.g. 2:11.')

    if not weekday is None:
        if not weekday.capitalize() in weekdays.values():
            raise ValueError('Starting day of the week should have full name with initial capital letter, e.g. Monday.')

    result_minutes = int(start_minutes) + int(duration_minutes)
    result_hours = int(start_hours) + int(duration_hours)
    add_half_days = 0

    if result_minutes > 59:
        result_minutes = result_minutes - 60
        result_hours += 1

    if result_hours >= 12:
        add_half_days = result_hours // 12

        if start_meridiem == 'PM':
            if add_half_days % 2 != 0:
                add_days = 1 + (add_half_days - 1) / 2
                result_meridiem = 'AM'
            else:
                add_days = add_half_days / 2
                result_meridiem = 'PM'
        else:  # start_meridiem == 'AM'
            if add_half_days == 1:
                add_days = 0
                result_meridiem = 'PM'
            elif add_half_days % 2 != 0:
                add_days = 1 + (add_half_days - 1) / 2
                result_meridiem = 'PM'
            else:
                add_days = add_half_days / 2
                result_meridiem = 'AM'

        if (not weekday is None):
            start_weekday = weekday.capitalize()
            start_weekday_num = list(weekdays.keys())[list(weekdays.values()).index(start_weekday)]
            result_weekday_num = (start_weekday_num + add_days) % 7
            if result_weekday_num == 0:
                result_weekday_num = 7
            result_weekday = weekdays[result_weekday_num]
        else:
            result_weekday = None

        if result_hours % 12 == 0:
            result_hours = 12
        else:
            result_hours = result_hours % 12

    else:
        result_meridiem = start_meridiem
        result_weekday = weekday
        add_days = 0

    new_time = str(result_hours) + ':' + str(result_minutes).rjust(2, '0') + ' ' + result_meridiem

    if not result_weekday is None:
        new_time = new_time + ', {}'.format(result_weekday)

    if add_days == 1:
        new_time = new_time + ' (next day)'
    elif add_days > 1:
        new_time = new_time + ' ({} days later)'.format(int(add_days))

    return new_time
