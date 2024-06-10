from text_summariser.config.configuration import ConfigurationManager
from text_summariser.components.model_trainer import ModelTrainer
from text_summariser.logging import logging


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()