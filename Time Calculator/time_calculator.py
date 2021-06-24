import re
class AddTime():
    def __init__(self, start, duration, day = None):
        self.start = start
        self.duration = duration
        self.day = day
        self.days = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY",
                     "SATURDAY", "SUNDAY")
    
    def newTime(self):
        startNumericalTime = self.timeCalculator(self.start)
        durationNumericalTime = self.timeCalculator(self.duration)
        newTime = self.newTimeCalculator(startNumericalTime, durationNumericalTime)
        message = self.messageCreator(newTime[0], newTime[1], newTime[2], newTime[3])        
        return message

    def timeCalculator(self, time):
        times = re.findall("[0-9]+", time)
        hours = int(times[0])
        minutes = int(times[1])
        numericalTime = (hours*60) + minutes
        timeOfDay = re.findall("PM", time)
        if timeOfDay != None:
            numericalTime += 12*60
        return numericalTime

    def newTimeCalculator(self, startNumericalTime, durationNumericalTime):
        totalMinutes = startNumericalTime + durationNumericalTime
        totalHours = totalMinutes//60
        days = totalHours//24
        hours = totalHours - (days*24)
        minutes = totalMinutes - (totalHours*60)
##        days = totalTime//(24*60)
##        remainder = totalTime%(24*60)
##        hours = remainder//60
##        minutes = remainder%60
        timeOfDay = self.timeOfDayCalculator(hours)
        if timeOfDay == "PM":
            hours = hours - 12
        return [hours, minutes, timeOfDay, days] 

    def timeOfDayCalculator(self, hours):
        print(hours)
        if hours > 12:
            return "PM"
        else:
            return "AM"

    def messageCreator(self, hours, minutes, timeOfDay, days):
        formattedMinutes = self.formatTime(minutes)
        message = str(hours) + ":" + formattedMinutes + " " + timeOfDay
        if days == 1:
            message += " (next day)"
        elif days != 0:
            message += " (" + str(days) + " days later)"
        print(message)
        return message

    def formatTime(self, time):
        time = str(time)
        if len(time) < 2:
            time = "0" + time
        return time
