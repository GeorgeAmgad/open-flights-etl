URLS = {
    "airports": "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports-extended.dat",
    "airlines": "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat",
    "routes": "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat",
    "planes": "https://raw.githubusercontent.com/jpatokal/openflights/master/data/planes.dat",
    "countries": "https://raw.githubusercontent.com/jpatokal/openflights/master/data/countries.dat",
}

COLUMN_MAPPINGS = {
    "airports": ["id", "name", "city", "country", "iata", "icao", "lat", "lon", "alt", "tz","dst", "tzd", "type", "source"],
    "airlines": ["id", "name", "alias", "iata", "icao", "callsign", "country", "active"],
    "routes": ["airline", "airline_id", "source", "source_id", "destination", "destination_id", "codeshare", "stops", "equipment"],
    "planes": ["name", "iata", "icao"],
    "countries": ["name", "iso", "dafif"],
}