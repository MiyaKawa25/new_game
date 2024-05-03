class Event:
    def __init__(self, type, params):
        self.type = type
        self.params = params

    def run(self):
        return self.params

class SayEvent(Event):
    def __init__(self, type, params):
        super().__init__(type, params)
        self.talker_id = params["talker_id"]
        self.message = params["message"]

    def run(self):
        print(f"[{self.talker_id}]: {self.message}")

class SelectEvent(Event):
    def __init__(self, type, params):
        super().__init__(type, params)
        self.selects = params["select"]

class SoundEvent(Event):
    def __init__(self, type, params):
        super().__init__(type, params)
        self.sound = params["sound"]
