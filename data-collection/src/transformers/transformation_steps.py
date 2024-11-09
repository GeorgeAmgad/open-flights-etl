import numpy as np
import pandas as pd

from transformers.base_transformation_step import TransformationStep


class ValidateIDStep(TransformationStep):
    def apply(self, data):
        data = data[data['id'].apply(lambda x: isinstance(x, int) and x >= 1)]
        return data


class ReplaceInvalidValuesWithNullStep(TransformationStep):
    def apply(self, data):
        for col in data.columns:
            data[col] = data[col].replace({"nan": None, "\\N": None, "-": None, "\\n": None, " ": None, np.nan: None})
        return data


class RemoveDuplicatesStep(TransformationStep):
    def __init__(self, columns):
        self.columns = columns

    def apply(self, data):
        return data.drop_duplicates(subset=self.columns, keep='first')


class ReplaceValuesStep(TransformationStep):
    def __init__(self, column, replacements):
        self.column = column
        self.replacements = replacements

    def apply(self, data):
        data[self.column] = data[self.column].replace(self.replacements).infer_objects(copy=False)
        return data


class NormalizeTextStep(TransformationStep):
    def __init__(self, columns, is_upper_case=False):
        self.columns = columns
        self.is_upper_case = is_upper_case

    def apply(self, data):
        for col in self.columns:
            if col in data.columns:
                data.loc[:, col] = data[col].apply(lambda x: self.normalize_text(x) if isinstance(x, str) else x)
        return data

    def normalize_text(self, text):
        text = text.replace("\xa0", " ").strip()
        if self.is_upper_case:
            text = text.upper()
        return text
