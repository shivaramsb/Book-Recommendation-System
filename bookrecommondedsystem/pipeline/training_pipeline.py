from bookrecommondedsystem.components.stage_01_data_ingestion import DataIngestion
from bookrecommondedsystem.components.stage_02_data_validation import DataValidation
from bookrecommondedsystem.components.stage_03_data_transformation import DataTransformation
from bookrecommondedsystem.components.stage_04_model_trainer import MadelTrainer

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_validation = DataValidation()
        self.data_transformation = DataTransformation()
        self.model_trainer = MadelTrainer()
    
    def start_training_pipeline(self):
        """
        Starts the training pipeline
        return: none
        
        """
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
        self.data_transformation.initiate_data_transformation()
        self.model_trainer.initiate_model_trainer()