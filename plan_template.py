import datetime
class plan:
    def __init__(self,date:datetime.date,time:datetime.time,location:str,note:str) -> None:
        self.date = date
        self.time = time
        self.location = location
        self.note = note