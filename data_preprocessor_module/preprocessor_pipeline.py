from util.pipeline import Pipeline


class PreprocessorPipeline(Pipeline):
    def __init__(self):
        Pipeline.__init__(self)

    def execute(self, data, execution_params):
        data_for_process = data
        for processor in self._pipeline_list:
            data_for_process = processor.execute(data_for_process)
        result = data_for_process
        return result