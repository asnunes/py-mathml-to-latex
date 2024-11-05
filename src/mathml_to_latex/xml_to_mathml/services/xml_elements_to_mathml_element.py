from typing import List, Dict
from xml.dom.minidom import Element as DOMElement, Node

from ...el_to_tex.protocols import MathMLElement, GenericMathMLElement


class ElementsToMathMLAdapter:
    def convert(self, els: List[DOMElement]) -> List[MathMLElement]:
        """
        Converts a list of DOM Elements to a list of MathMLElement instances.

        Args:
            els (List[DOMElement]): A list of DOM Elements to convert.

        Returns:
            List[MathMLElement]: A list of converted MathMLElement instances.
        """
        return [self._convert_element(el) for el in els if el.tagName is not None]

    def _convert_element(self, el: DOMElement) -> MathMLElement:
        attributes = self._convert_element_attributes(el.attributes)
        has_children = self._has_element_child(el)
        value = (
            "" if has_children else (el.firstChild.nodeValue if el.firstChild else "")
        )

        children = (
            self.convert(
                [
                    child
                    for child in el.childNodes
                    if child.nodeType == Node.ELEMENT_NODE
                ]
            )
            if has_children
            else []
        )

        return GenericMathMLElement(
            name=el.tagName,
            value=value.strip(),
            children=children,
            attributes=attributes,
        )

    def _convert_element_attributes(self, attributes) -> Dict[str, str]:
        attr_dict = {}
        for attr in attributes.values():
            # If the attribute value is the same as the attribute name, set it to an empty string
            attr_value = "" if attr.value == attr.name else attr.value
            attr_dict[attr.name] = attr_value
        return attr_dict

    def _has_element_child(self, el: DOMElement) -> bool:
        return any(child.nodeType == Node.ELEMENT_NODE for child in el.childNodes)

    def _is_there_any_no_text_node(self, children: List[Node]) -> bool:
        return any(child.nodeName != "#text" for child in children)
