from implementation.abstraction import FilePath, InferenceResult
from .abstraction import ModelBuilder, Model
import pathlib

MODULE_DIR = pathlib.Path(__file__).parent

class ModelImplementation(Model):

    def infer(self, input_file_paths: list[str]) -> InferenceResult:

        # inference happens here

        return {
            'data': str(MODULE_DIR) / 'assets' / 'sample.csv',
            'type': 'application/csv',
            'info': {},
        }
    
class ModelBuilderImplementation(ModelBuilder):
    
    def build(self, model_file_paths: list[str]) -> Model:
        
        # building of the model happens here

        return ModelImplementation()
    


builder_class = ModelBuilderImplementation


inference_metadata = {
    'input_files': [ ['application/csv'] ],
    'model_artifacts': [ ['.pt'] ],
}