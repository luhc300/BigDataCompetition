from util.module import Module
from data_classifier_module.classifier_factory import ClassifierFactory
from data_classifier_module.classifier_pipeline import ClassifierPipeline

class DataClassifier(Module):
    def __init__(self):
        Module.__init__(self)
        self._pipeline = ClassifierPipeline()
        self._factory = ClassifierFactory()

