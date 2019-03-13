from elastalert.enhancements import BaseEnhancement, DropMatchException
import datetime

class BBWorkingWeek(BaseEnhancement):
    def process(self, match):
        # no alerts at the weekend or out of hours mon-fri
        if datetime.datetime.now().weekday() in [5, 6]:
            raise DropMatchException
        if datetime.datetime.now().hour < 9:
            raise DropMatchException
        if datetime.datetime.now().hour >= 17:
            raise DropMatchException
