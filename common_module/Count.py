from common_module import Today
today=Today.get()

class makeCountObj:
    def __init__(self, name,message):
        self.name = today+name
        self.expectedmessage=message
    number=0
    result="ok"
    message=""
