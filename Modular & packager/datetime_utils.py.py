import datetime
import time


def current_datetime():
    now = datetime.datetime.now()
    print("\nCurrent Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


def date_difference():
    d1 = input("Enter first date (YYYY-MM-DD): ")
    d2 = input("Enter second date (YYYY-MM-DD): ")

    date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

    diff = abs((date2 - date1).days)
    print("Difference:", diff, "days")


def custom_format():
    now = datetime.datetime.now()
    print(now.strftime("%d/%m/%Y"))
    print(now.strftime("%A, %B %d, %Y"))


def stopwatch():
    input("Press Enter to Start...")
    start = time.time()

    input("Press Enter to Stop...")
    end = time.time()

    print("Elapsed Time:", round(end - start, 2), "seconds")


def countdown():
    sec = int(input("Enter seconds: "))

    while sec > 0:
        print(sec)
        time.sleep(1)
        sec -= 1

    print("Time's Up!")
