from geoalchemy2 import Geometry
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, ForeignKey, text, Boolean
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError

from db.db_connector import get_db_engine


class DatabaseArchiver:
    def __init__(self, schema_name='open_flights'):
        self.schema_name = schema_name
        self.engine = get_db_engine()
        self.metadata = MetaData(schema=self.schema_name)

        self.create_schema()

        self.tables = self.define_tables()

        self.metadata.create_all(self.engine, checkfirst=True)

    def create_schema(self):
        """Create the schema if it does not already exist."""
        try:
            with self.engine.connect() as connection:
                connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.schema_name}"))
                connection.commit()
        except SQLAlchemyError as e:
            print(f"Error creating schema: {e}")

    def define_tables(self):
        tables = {'countries': Table(
            'countries', self.metadata,
            Column('name', String, primary_key=True),
            Column('iso', String),
            Column('dafif', String)
        ), 'airlines': Table(
            'airlines', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('alias', String),
            Column('iata', String),
            Column('icao', String),
            Column('callsign', String),
            Column('country', String, ForeignKey('countries.name')),
            Column('active', String)
        ), 'airports': Table(
            'airports', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('city', String),
            Column('country', String, ForeignKey('countries.name')),
            Column('iata', String),
            Column('icao', String),
            Column('lat', Float),
            Column('lon', Float),
            Column('alt', Integer),
            Column('tz', String),
            Column('dst', String),
            Column('tzd', String),
            Column('type', String),
            Column('source', String),
            Column('geom', Geometry('POINT', srid=4326))  # Spatial column
        ), 'planes': Table(
            'planes', self.metadata,
            Column('name', String, primary_key=True),
            Column('iata', String),
            Column('icao', String)
        ), 'routes': Table(
            'routes', self.metadata,
            Column('airline', String),
            Column('airline_id', Integer, ForeignKey('airlines.id')),
            Column('source', String),
            Column('source_id', Integer, ForeignKey('airports.id')),
            Column('destination', String),
            Column('destination_id', Integer, ForeignKey('airports.id')),
            Column('codeshare', Boolean),
            Column('stops', Integer),
            Column('equipment', String)
        )}

        return tables

    def insert_data(self, category, data):
        table = self.tables[category]
        with self.engine.connect() as connection:
            self.insert_rows(connection, data, table)

    def insert_data_ignore_fk(self, category, data):
        table = self.tables[category]
        with self.engine.connect() as connection:
            connection.execute(text("SET session_replication_role = replica;"))

            try:
                self.insert_rows(connection, data, table)
            finally:
                connection.execute(text("SET session_replication_role = DEFAULT;"))

    @staticmethod
    def insert_rows(connection, data, table):
        for row in data.to_dict(orient="records"):
            if "lat" in row and "lon" in row:
                row['geom'] = f'SRID=4326;POINT({row["lon"]} {row["lat"]})'
            connection.execute(insert(table).values(row).on_conflict_do_nothing())
        connection.commit()
