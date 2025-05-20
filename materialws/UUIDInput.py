import uuid
from django import forms

class UUIDInput(forms.TextInput):

    def is_initial(self, value):
        """
        Return whether value is considered to be initial value.
        """
        return (value is None)

    def format_value(self, value):
        if self.is_initial(value):
            return uuid.uuid4()
        return value

    def value_from_datadict(self, data, files, name):
        return data["model_id"]
