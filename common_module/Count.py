from common_module import Today
today=Today.get()

class makeCountObj:
    def __init__(self, name,typename,message):
        self.name = today+name
        self.testname=name
        self.testtype=typename
        self.expectedmessage=message
    number=0
    result="×"
    message=""
