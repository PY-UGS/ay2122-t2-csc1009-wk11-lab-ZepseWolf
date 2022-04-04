class ClockTime:
    def __init__(self):
        self.hours = None
        self.minutes = None
        self.seconds = None

    def setHours(self):
        self.hours = int(input('Input Clock hour: ')) 
        while self.hours > 23 and  self.hours < 0:  
            print('Hour cannot be more than 23 or less then zero!')
            self.hours = int(input('Set Clock hour(s): '))
        

    def setMinutes(self):
        self.minutes = int(input('Input Clock minute: ')) 
        while self.minutes > 59 and self.minutes < 0:  
            print('Minute cannot be more than 59 or less then zero!')
            self.minutes = int(input('Set Clock minute(s): '))
        

    def setSeconds(self):
        self.seconds = int(input('Input Clock second: '))
        while self.seconds > 59 and self.seconds < 0:  
            print('Second cannot be more than 59 or less then zero!')
            self.seconds = int(input('Set Clock second: '))
        

    def setTime(self): 
        print('Please set clock values in 24-Hour format.')
        self.setHours()
        self.setMinutes()
        self.setSeconds()
        

    def showTime(self): 
        print('Clock time set is: ' + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))
        


Clock = ClockTime()  
Clock.setTime()
Clock.showTime()
