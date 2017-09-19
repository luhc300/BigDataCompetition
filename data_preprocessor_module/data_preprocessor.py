import pandas as pd
from data_preprocessor_module.preprocessor_pipeline import PreprocessorPipeline
from data_preprocessor_module.processor_factory import ProcessorFactory
from util.module import Module

class DataPreprocessor(Module):
    def __init__(self):
        Module.__init__(self)
        self._pipeline = PreprocessorPipeline()
        self._factory = ProcessorFactory()


