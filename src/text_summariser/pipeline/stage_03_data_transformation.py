from text_summariser.config.configuration import ConfigurationManager
from text_summariser.logging import logger
from text_summariser.components.data_transformation import DataTransfromation


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransfromation(config = data_transformation_config)
        data_transformation.convert()

