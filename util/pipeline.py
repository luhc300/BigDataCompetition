class Pipeline:
    def __init__(self):
        self._pipeline_list = []

    def add(self,item):
        self._pipeline_list.append(item)

    def execute(self, data, execution_params):
        return data

