import requests
import pandas as pd
from io import StringIO

from src.openflight_utils import URLS, COLUMN_MAPPINGS


def export_data(category):
    """Fetch data from OpenFlights based on the category and return selected columns."""
    if category not in URLS:
        raise ValueError(f"Category '{category}' is not valid. Choose from {list(URLS.keys())}.")

    try:
        response = requests.get(URLS[category])
        response.raise_for_status()

        df = pd.read_csv(StringIO(response.text), header=None)

        if category in COLUMN_MAPPINGS:
            df.columns = COLUMN_MAPPINGS[category]

        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {category}: {e}")
        return None

