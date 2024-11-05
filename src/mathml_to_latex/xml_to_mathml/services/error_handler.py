from xml.parsers.expat import ExpatError
from typing import List
import re


class ErrorHandler:
    def __init__(self):
        self.error_locator = {}

    def fix_error(self, xml: str, error: Exception) -> str:
        if not isinstance(error, ExpatError):
            return xml

        return self._fix_missing_attribute(error, xml)

    def _fix_missing_attribute(self, error: ExpatError, xml: str) -> str:
        result = self._fix_missing_attribute_value(error, xml)
        if result != xml:
            return result

        pattern = self._math_generic_missing_value()
        while re.search(pattern, xml):
            # Replace the matched pattern by removing the missing attribute value
            result = re.sub(pattern, r'\1\3', xml)
        return result

    def _fix_missing_attribute_value(self, error: ExpatError, xml: str):
        error_code = error.code
        if error_code != 4: return xml

        error_line = error.lineno
        error_offset = error.offset

        goal_line = xml.split('\n')[error_line - 1]
        word = self._get_word_at_str_pos(goal_line, error_offset)

        pattern = self._match_missing_value_for_attribute(word)
        return re.sub(pattern, '', xml)

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

    def _get_word_at_str_pos(self, string: str, pos: int) -> str:
        """
        Returns the word at the specified position in the string.
        """
        start = pos
        end = pos
        while start > 0 and string[start - 1] != ' ':
            start -= 1
        while end < len(string) and string[end] != ' ' and string[end] != '>':
            end += 1
        return string[start:end]