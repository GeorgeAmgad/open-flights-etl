from pipelines.transformation_pipeline import TransformationPipeline
from transformers.transformation_steps import ValidateIDStep, ReplaceInvalidValuesWithNullStep, NormalizeTextStep, \
    RemoveDuplicatesStep


class AirlinesPipeline:
    def __init__(self):
        self.pipeline = TransformationPipeline()
        self._setup_pipeline()

    def _setup_pipeline(self):
        self.pipeline.add_step(ReplaceInvalidValuesWithNullStep())
        self.pipeline.add_step(ValidateIDStep())
        self.pipeline.add_step(RemoveDuplicatesStep(columns=['id']))
        self.pipeline.add_step(NormalizeTextStep(columns=['iata', 'icao'], is_upper_case=True))
        self.pipeline.add_step(NormalizeTextStep(columns=['name', 'alias', 'callsign', 'country', 'active']))
        self.pipeline.add_step(RemoveDuplicatesStep(columns=['name', 'country', 'callsign']))

    def apply(self, data):
        return self.pipeline.apply(data)
