import time, os
import datetime
def get_time(value):
    logfile = open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r")
    logfile.seek(0,2)
    while True:
        line = logfile.readline()
        if "[CHAT] IC" in line and "!savemessage" in line:
            last_time = line[1:9]
            hours = int(last_time[0:2])
            minutes = int(last_time[3:5])
            seconds = int(last_time[6:8])
            last_time = datetime.timedelta(hours = hours,minutes = minutes ,seconds = seconds)
            first_time = last_time - value
            return first_time
def get_chat(time):
    logfile = open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r")
    thefile = logfile.readlines()
    output_file = open("output.txt","w+")
    for i in range(len(thefile)):
        line = thefile[i]
        if "[CHAT] IC" in line:
            linetime = line[1:9]
            hours = int(linetime[0:2])
            minutes = int(linetime[3:5])
            seconds = int(linetime[6:8])
            linetimefinal = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
            if  linetimefinal > time:
                output_file.write(line+"\n")
    output_file.close()
if __name__ == "__main__":
    value = int(input("Enter a value for the chat in minutes that you want to capture (USE INTEGERS): \n"))
    hours = value // 60
    minutes = value % 60
    time = datetime.timedelta(hours = hours, minutes = minutes)
    first_time = get_time(time)
    get_chat(first_time)
    #print(first_time)

