"""
Author: Meng Moua
Course: CSC500
Assignment: Module 3, Part 2
"""

def main():
    time_now = input('Please enter the (current time) from 0 to 24:\n')
    hour_wait = input('Please enter the (wait time) greater than or equal to 0:\n')
    if not valid_number(time_now) or not valid_number(hour_wait):
        print('The (current time) or (wait time) is not a valid number.')
        return

    if int(time_now) < 0 or int(time_now) > 24:
        print('Please try again. The (current time) is not in the range of 0 to 23.')
        return

    if int(hour_wait) < 0:
        print('Please try again. The (wait time) in hours cannot be less than 0.')
        return

    # get the alarm time in 24-hour clock
    alarm_time_24_hr = get_alarm_time(time_now, hour_wait)
    # determine morning 'AM' or afternoon 'PM' time
    am_or_pm = get_am_or_pm(alarm_time_24_hr)
    # calculate the alarm time in 12-hour clock
    alarm_time_12_hr = alarm_time_24_hr % 12

    print('The alarm will ring at {}:00 {} ({}:00 {})'.format(
        alarm_time_24_hr, am_or_pm, alarm_time_12_hr, am_or_pm))

def get_alarm_time(time_now, hour_wait) -> int:
    """
    Get the time the alarm will sound.
    :param time_now: the current time given by the user
    :param hour_wait: the waiting hours given by the user
    :return: the alarm time
    """
    return (int(time_now) + int(hour_wait)) % 24

def get_am_or_pm(time) -> str:
    """
    Determine the morning or afternoon time
    :param time: user time in hour
    :return: 'AM' or 'PM'
    """
    return 'AM' if time < 12 else 'PM'

def valid_number(num) -> bool:
    """
    Validate a number
    :param num: a number
    :return: true or false
    """
    try:
        int(num)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    main()
