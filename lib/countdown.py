import time  
def countdown(my_int):
    while my_int > 0:
        print(f"{my_int} SECOND(S)!")
        my_int -= 1
    print("HAPPY NEW YEAR!")
countdown(10)


def countdown_with_sleep(my_int):
    while my_int > 0:
        print(f"{my_int} SECOND(S)!")
        time.sleep(1)  
        my_int -= 1

    print("HAPPY NEW YEAR!")

# Test the countdown_with_sleep function
countdown_with_sleep(10)
