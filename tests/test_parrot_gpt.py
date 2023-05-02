import unittest
from unittest.mock import MagicMock
from parrot_gpt import ParrotGpt
from parrot_gpt.model_interface import ModelInterface

class TestParrotGpt(unittest.TestCase):

    class DummyModel(ModelInterface):
        def get_model(self):
            pass

        def get_tokenizer(self):
            pass

        def transform_prompt(self, prompt):
            pass

    def setUp(self):
        self.dummy_model = self.DummyModel()
        self.parrot_gpt = ParrotGpt(self.dummy_model)

    def test_model_initialization(self):
        self.assertEqual(self.parrot_gpt.model, self.dummy_model)

    def test_serialize(self):
        self.dummy_model.transform_prompt = MagicMock(return_value="transformed prompt")
        self.parrot_gpt._transform_metadata = MagicMock(return_value="transformed metadata")
        input_metadata = "dummy metadata"
        output = self.parrot_gpt.serialize(input_metadata)
        self.dummy_model.transform_prompt.assert_called_once()
        self.parrot_gpt._transform_metadata.assert_called_once()
        self.assertEqual(output, "transformed metadata")

if __name__ == '__main__':
    unittest.main()
