from data_preprocessor_module.processors.normalize_processor import normalize_processor
from util.factory import Factory

class ProcessorFactory(Factory):
    def __init__(self):
        Factory.__init__(self)
        self._factory_index = {
            "normalize": normalize_processor()
        }

