from pipelines.transformation_pipeline import TransformationPipeline
from transformers.transformation_steps import ValidateIDStep, ReplaceInvalidValuesWithNullStep, NormalizeTextStep, \
    RemoveDuplicatesStep, ReplaceValuesStep


class AirportsPipeline:
    def __init__(self):
        self.pipeline = TransformationPipeline()
        self._setup_pipeline()

    def _setup_pipeline(self):
        self.pipeline.add_step(ReplaceInvalidValuesWithNullStep())
        self.pipeline.add_step(ValidateIDStep())
        self.pipeline.add_step(RemoveDuplicatesStep(columns=['id']))
        self.pipeline.add_step(NormalizeTextStep(columns=['iata', 'icao'], is_upper_case=True))
        self.pipeline.add_step(NormalizeTextStep(columns=['name', 'city', 'country', 'type', 'source', 'tzd']))
        self.pipeline.add_step(ReplaceValuesStep(column='country', replacements={"Faroe Islands": "Faeroe Islands",
                                                                                 "Congo (Brazzaville)": "Congo Republic",
                                                                                 "Congo (Kinshasa)": "Congo Republic"}))
        self.pipeline.add_step(RemoveDuplicatesStep(columns=['name', 'lat', 'lon']))

    def apply(self, data):
        return self.pipeline.apply(data)
