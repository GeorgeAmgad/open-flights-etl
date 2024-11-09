from pipelines.transformation_pipeline import TransformationPipeline
from transformers.transformation_steps import ReplaceInvalidValuesWithNullStep, NormalizeTextStep


class PlanesPipeline:
    def __init__(self):
        self.pipeline = TransformationPipeline()
        self._setup_pipeline()

    def _setup_pipeline(self):
        self.pipeline.add_step(ReplaceInvalidValuesWithNullStep())
        self.pipeline.add_step(NormalizeTextStep(columns=['iata', 'icao'], is_upper_case=True))
        self.pipeline.add_step(NormalizeTextStep(columns=['name']))

    def apply(self, data):
        return self.pipeline.apply(data)
