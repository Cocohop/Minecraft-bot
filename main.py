import time, os
import datetime
def get_chat(value):
    logfile = open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r")
    #print(last_line[1:8])
    logfile.seek(0,2)
    while True:
        line = logfile.readline()
        if "[CHAT] IC" in line:
            last_time = line[1:9]
            hours = int(last_time[0:2])
            minutes = int(last_time[3:5])
            seconds = int(last_time[6:8])
            last_time = datetime.time(hours, minutes , seconds)
            print(last_time)


if __name__ == "__main__":
    value = int(input("Enter a value for the chat in minutes that you want to capture (USE INTEGERS): \n"))
    hours = value // 60
    minutes = value % 60
    time = datetime.time(hours, minutes, 0)
    logfile = open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r")
    get_chat(time)


