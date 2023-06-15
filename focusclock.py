import time

def pomodoro_timer(minutes):
    """
    A function to create a Pomodoro timer for focus and productivity.
    
    Parameters:
    minutes (int): The number of minutes for which the timer should run.
    
    Returns:
    None
    """
    seconds = minutes * 60
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, sec)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == '__main__':
    pomodoro_timer(25)  # Set the timer for 25 minutes
