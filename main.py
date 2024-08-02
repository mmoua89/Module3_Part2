"""
Author: Meng Moua
Course: CSC500
Assignment: Module 3, Part 2
"""

def main():
    time_now = input('Please enter the current time in hour in the range of 0 to 23:\n')
    hour_wait = input('Please enter the number of hours greater than 0 to wait for the alarm:\n')
    if not valid_number(time_now) or not valid_number(hour_wait):
        print('Current time or wait time in hour is not a valid number.')
        return

    if int(time_now) < 0 or int(time_now) > 23:
        print('The current time is not in the range of 0 and 23. Please try again.')
        return

    if int(hour_wait) < 0:
        print('The wait time in hour(s) cannot be less than 0. Please try again.')
        return

    alarm_time = get_alarm_time(time_now, hour_wait)
    print('The alarm will ring at {}:00 {}'.format(alarm_time, 'AM' if alarm_time < 12 else 'PM'))

def get_alarm_time(time_now, hour_wait) -> int:
    """
    Get the time the alarm will sound.
    :param time_now: the current time given by the user
    :param hour_wait: the waiting hours given by the user
    :return: the alarm time
    """
    return (int(time_now) + int(hour_wait)) % 24

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
