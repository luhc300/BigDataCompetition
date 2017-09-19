import pandas as pd
import numpy as np
from data_preprocessor_module.data_preprocessor import DataPreprocessor
from data_classifier_module.data_classifier import DataClassifier
if (__name__ == "__main__"):
    data = pd.read_csv("D:/Programs/Python/BigDataCompetition/data/train.csv")
    test_data = pd.read_csv("D:/Programs/Python/BigDataCompetition/data/test.csv")
    dp = DataPreprocessor()
    dp.add("normalize",attr={"target":["var3","var15"]})
    result = dp.execute(data)
    dc = DataClassifier()
    dc.add("random_forest", attr={"target":["TARGET"]})
    dc.set_execution_params({"action_type":"train"})
    dc.execute(result)
    dc.set_execution_params({"action_type":"test"})
    prediction = dc.execute(test_data)
    print(prediction)
