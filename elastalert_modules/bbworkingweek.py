from elastalert.enhancements import BaseEnhancement, DropMatchException
import datetime

class BBWorkingWeek(BaseEnhancement):
    def process(self, match):
        # no alerts on saturday or sunday
        if datetime.datetime.now().weekday() in [5, 6]:
            raise DropMatchException
        if datetime.datetime.now().hour < 8:
            raise DropMatchException
        if datetime.datetime.now().hour > 5:
            raise DropMatchException
