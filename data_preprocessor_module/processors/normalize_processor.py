import numpy as np

from data_preprocessor_module.processors.processor import Processor


class normalize_processor(Processor):
    def __init__(self):
        Processor.__init__(self)

    def execute(self, data):
        if self._target is None:
            data = data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
        else:
            data[self._target] = data[self._target].apply(lambda x: (x-np.min(x)) / (np.max(x) - np.min(x)))
        return data
