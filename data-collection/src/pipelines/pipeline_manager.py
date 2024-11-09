from pipelines.airelines_pipeline import AirlinesPipeline
from pipelines.airports_pipeline import AirportsPipeline
from pipelines.countries_pipeline import CountriesPipeline
from pipelines.planes_pipeline import PlanesPipeline
from pipelines.routes_pipeline import RoutesPipeline


class PipelineManager:
    def __init__(self):
        self.pipelines = {
            'airports': AirportsPipeline(),
            'airlines': AirlinesPipeline(),
            'routes': RoutesPipeline(),
            'planes': PlanesPipeline(),
            'countries': CountriesPipeline()
        }

    def transform_data(self, category, data):
        pipeline = self.pipelines.get(category)
        if not pipeline:
            raise ValueError(f"No pipeline found for category: {category}")
        return pipeline.apply(data)
