import json
from typing import Optional, Union
from ..preprocess import *

class PromptObject:
    def __init__(
        self,
        prompt_section: Optional[str] = "toxicity",  # Section of the prompt (available: "bias", "toxicity" or "value_alignment", default: "toxicity")
        data_item: Optional[Union[list, dict]] = None,  # Data items used in the default prompt template (default: None)
        prompt_type: Optional[str] = "default",  # Type of prompt (available: "default" or "custom")
        prompt_file: Optional[str] = "prompt_template/default.json",  # Prompt template file (default: "prompt_template/default.json")
        value_alignment: Optional[bool] = False  # Indicates if value alignment is enabled (default: False)
    ):
        self.customList = None
        self.prompt_template_value_alignment_good = None
        self.prompt_template_value_alignment_bad = None
        self.prompt_template_toxicity = None
        self.prompt_template_bias = None
        self.prompt_template = None
        self.constructDict = None
        self.constructList = None

        if data_item is None:
            data_item = []

        self.prompt_type = prompt_type
        self.prompt_section = prompt_section
        self.prompt_file = prompt_file
        self.data_item = data_item
        self.value_alignment = value_alignment

    def read_default(self):
        with open(self.prompt_file) as f:
            self.prompt_template = json.load(f)
            self.prompt_template_bias = self.prompt_template['bias']
            self.prompt_template_toxicity = self.prompt_template['toxicity']
            self.prompt_template_value_alignment_bad = self.prompt_template['value_alignment']['bad']
            self.prompt_template_value_alignment_good = self.prompt_template['value_alignment']['good']

    def default_prompt(self):
        assert self.prompt_type == "default"
        self.read_default()
        if self.prompt_section == 'bias':
            return self.prompt_template_bias
        elif self.prompt_section == 'toxicity':
            return self.prompt_template_toxicity
        elif self.prompt_section == 'value_alignment':
            return {"bad": self.prompt_template_value_alignment_bad, "good": self.prompt_template_value_alignment_good}
        else:
            raise NotImplementedError("Prompt type {} not implemented".format(self.prompt_section))  # Raise an error for unsupported prompt types

    def construct_default_prompt(self, prompt_words: str, groups: Optional[list] = None):
        if self.prompt_section == 'toxicity':
            self.constructList = []
            for item in self.data_item:
                prompt_item = self.prompt_template_toxicity
                prompt_item = replace_double_underscore(prompt_item, [prompt_words, item])  # Replace placeholders in the template with actual values
                self.constructList.append(prompt_item)
            return self.constructList
        elif self.prompt_section == 'bias':
            self.constructDict = {}
            for item in self.data_item:
                for group in groups:
                    if group not in self.constructDict:
                        self.constructDict[group] = []
                    prompt_item = self.prompt_template_bias
                    prompt_item = replace_double_underscore(prompt_item, [group, prompt_words, item])
                    self.constructDict[group].append(prompt_item)
            return self.constructDict
        elif self.prompt_section == 'value_alignment':
            assert self.value_alignment is True  # Ensure value alignment is enabled
            assert isinstance(self.data_item, dict)  # Ensure data items are in dictionary format
            self.constructList = []
            for item, norm_label in self.data_item.items():
                if norm_label == 'bad':
                    prompt_item = self.prompt_template_value_alignment_bad  # Use bad value alignment template
                    prompt_item = replace_double_underscore(prompt_item, [item])  # Replace placeholders in the template with actual values
                else:
                    prompt_item = self.prompt_template_value_alignment_good  # Use good value alignment template
                    prompt_item = replace_double_underscore(prompt_item, [item])  # Replace placeholders in the template with actual values
                self.constructList.append(prompt_item)
            return self.constructList
        else:
            raise NotImplementedError("Prompt type {} not implemented".format(self.prompt_section))  # Raise an error for unsupported prompt types

    def custom_prompt(self, prompt_template: str, custom_data: list):
        assert prompt_template.count("__") == len(custom_data)  # Ensure the number of placeholders in the template matches the length of custom data
        self.customList = []
        transposed_data = [list(x) for x in zip(*custom_data)]  # Transpose the custom data
        for item in transposed_data:
            prompt_item = prompt_template
            prompt_item = replace_double_underscore(prompt_item, item)  # Replace placeholders in the template with actual values
            self.customList.append(prompt_item)
        return self.customList
