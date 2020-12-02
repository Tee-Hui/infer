import joblib
import os.path
import logging

logger = logging.getLogger('Model')


class Model:
    model_object = None

    def __init__(self, model_id, model_lib=None, model_type=None, path=None, usage_example=None):
        self.model_id = model_id
        self.model_lib = model_lib
        self.model_type = model_type
        self.path = path
        self.usage_example = usage_example
        # Set a default path to local models directory, if no path provided by the application config
        if self.path is None:
            self.path = 'models/' + model_id + '.pkl'

    def get_model_object(self):
        # TODO Handle paths other than local disk. e.g. Docker registry, object storage etc.
        if self.model_object is None:
            if os.path.isfile(self.path):
                self.model_object = joblib.load(self.path)
            else:
                logger.error(f'Failed to load model_id {self.model_id} from path {self.path}')
                raise PredictionError(f'Failed to load model_id {self.model_id} from path {self.path}')
        return self.model_object


class PredictionError(Exception):
    pass
