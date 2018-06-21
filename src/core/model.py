class BaseModel(object):
    def __init__(self, data_source, save_path=None, **kwargs):
        self.data_source = data_source
        self.save_path = save_path
        self.training_accuracy = 0.0
        self.validation_accuracy = 0.0

    def train(self, **kwargs):
        raise NotImplementedError("The train() method need to be implemented be subclasses!")
    
    def predict(self, X):
        raise NotImplementedError("The predict() method need to be implemented be subclasses!")
    
    def score(self, X, y):  # for visualization of validation error
        raise NotImplementedError("The predict() method need to be implemented be subclasses!")

    def set_save_path(self, save_path):
        self.save_path = save_path

    def evaluate_for_kaggle(self, output_src):
        import logging
        logger = logging.getLogger(self.__class__.__name__)
        logger.info("Predicting on test set...")
        predictions = self.predict(self.data_source.testX)

        logger.info("Writing to submission file...")
        from utils import ensure_dir
        ensure_dir(output_src)
        with open(output_src, "w") as f:
            f.write("Id,Prediction\n")
            for idx, val in enumerate(predictions):
                f.write("%d,%d\n" % (idx + 1, val))
        logger.info("Submission file saved: " + output_src)
