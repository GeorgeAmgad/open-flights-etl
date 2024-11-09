from pipelines.transformation_pipeline import TransformationPipeline
from transformers.transformation_steps import NormalizeTextStep, ReplaceInvalidValuesWithNullStep, RemoveDuplicatesStep


class CountriesPipeline:
    def __init__(self):
        self.pipeline = TransformationPipeline()
        self._setup_pipeline()

    def _setup_pipeline(self):
        self.pipeline.add_step(ReplaceInvalidValuesWithNullStep())
        self.pipeline.add_step(NormalizeTextStep(columns=['name', 'iso', 'dafif']))
        self.pipeline.add_step(RemoveDuplicatesStep(columns=['name']))

    def apply(self, data):
        return self.pipeline.apply(data)
