from util.factory import Factory
from data_classifier_module.classifiers.rf_classifier import RFClassifier
from data_classifier_module.classifiers.lr_classifer import LRClassifier

class ClassifierFactory(Factory):
    def __init__(self):
        Factory.__init__(self)
        self._factory_index = {
            "random_forest": RFClassifier(),
            "logistic_regression": LRClassifier()
        }

