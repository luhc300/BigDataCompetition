from util.pipeline import Pipeline
import numpy as np

class ClassifierPipeline(Pipeline):
    def __init__(self):
        Pipeline.__init__(self)

    def execute(self, data, execution_params):
        result = []
        action_type = execution_params.get("action_type")
        if action_type == "train":
            for classifier in self._pipeline_list:
                classifier.train(data)
        if action_type == "test":
            for classifier in self._pipeline_list:
                ans = classifier.predict(data)
                result.append(ans)
            result = np.array(result)
            final_result = np.mean(result, axis=0)
            return final_result
