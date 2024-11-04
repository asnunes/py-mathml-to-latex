from typing import List, Optional
import re


class ErrorHandler:
    def __init__(self):
        self._errors: List[str] = []
        self.error_locator = {}

    def fix_error(self, xml: str, error_message: str) -> str:
        if not self._is_missing_attribute_value_error(error_message):
            return xml

        self._errors.append(error_message)
        return self._fix_missing_attribute(error_message, xml)

    def is_there_any_errors(self) -> bool:
        return len(self._errors) > 0

    def clean_errors(self) -> None:
        self._errors = []

    def _fix_missing_attribute(self, error_message: str, xml: str) -> str:
        parts = error_message.split('"')
        if len(parts) > 1:
            missing_attribute = parts[1]
            pattern = self._match_missing_value_for_attribute(missing_attribute)
            # Remove the missing attribute from the XML
            xml = re.sub(pattern, '', xml)
            return xml

        pattern = self._math_generic_missing_value()
        while re.search(pattern, xml):
            # Replace the matched pattern by removing the missing attribute value
            xml = re.sub(pattern, r'\1\3', xml)
        return xml

    def _match_missing_value_for_attribute(self, attribute: str) -> re.Pattern:
        """
        Constructs a regex pattern to find the specified attribute
        without a value (i.e., attribute= not followed by " or ').
        """
        escaped_attribute = re.escape(attribute)
        regex_pattern = rf'({escaped_attribute}=(?!(["\'])))|({escaped_attribute}(?!(["\'])))'
        return re.compile(regex_pattern, re.MULTILINE)

    def _math_generic_missing_value(self) -> re.Pattern:
        """
        Constructs a generic regex pattern to find any attribute
        without a value within a math element.
        """
        # This pattern matches:
        # Group 1: <... (anything up to a space)
        # Group 2: attribute= not followed by " or '
        # Group 3: ...> (anything up to >)
        return re.compile(r'(<.* )(\w+=(?!(["\'])))?(.*>)', re.MULTILINE)

    def _is_missing_attribute_value_error(self, error_message: str) -> bool:
        """
        Determines if the error message pertains to a missing attribute value.
        """
        return (
            ('attribute' in error_message and 'missed' in error_message) or
            'attribute value missed' in error_message
        )
