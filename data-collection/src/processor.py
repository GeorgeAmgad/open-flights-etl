from archiver import DatabaseArchiver
from exporter import export_data
from pipelines.pipeline_manager import PipelineManager
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_table(table_name, export_func, transform_func, insert_func):
    """
    General function to process each table: export, transform, and insert.
    """
    logging.info(f"Starting processing for table: {table_name}")

    # Fetch data
    logging.info(f"Fetching data for table: {table_name}")
    data_df = export_func(table_name)
    logging.info(f"Fetched {len(data_df)} records for table: {table_name}")

    # Transform data
    logging.info(f"Transforming data for table: {table_name}")
    transformed_data = transform_func(table_name, data_df)
    logging.info(f"Transformed data for table: {table_name}")

    # Insert data into the database
    logging.info(f"Inserting data into database for table: {table_name}")
    insert_func(table_name, transformed_data)
    logging.info(f"Data inserted for table: {table_name}")


class DataProcessor:
    def __init__(self):
        self.manager = PipelineManager()
        self.archiver = DatabaseArchiver()

    def run(self):
        tables = {
            "countries": self.archiver.insert_data,
            "airports": self.archiver.insert_data_ignore_fk,
            "airlines": self.archiver.insert_data,
            "routes": self.archiver.insert_data,
            "planes": self.archiver.insert_data,
        }

        for table_name, insert_func in tables.items():
            fetch_func = export_data
            transform_func = self.manager.transform_data
            process_table(table_name, fetch_func, transform_func, insert_func)
        logging.info(f"Completed processing of data")