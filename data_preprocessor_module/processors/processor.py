class Processor:
    def __init__(self):
        self._target = None

    def set_attr(self, attr):
        if "target" in attr:
            target = attr.get("target")
            self._target = target

    def execute(self, data):
        return data

