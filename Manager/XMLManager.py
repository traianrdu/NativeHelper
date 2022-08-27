import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


class XMLManager:
    """
        A class used to represent the XML Manager.

        ...

        Attributes
        ----------
        xml_text : str
            an xml string

        Methods
        -------
        get_root() -> str
            Returns the root
    """

    def __init__(self, xml_text: str):
        """
        Parameters
        ----------
        xml_text : str
            an xml string
        """
        self.xml_text = xml_text

    def get_root(self) -> Element:
        """Returns the root of the xml structure

        Parameters
        ----------

        Returns
        -------
        Element
            root element
        """
        return ET.fromstring(self.xml_text)

    def get_children(self, root: Element):
        """"""
        for child in self.get_root():
            """"""
        for item in root:
            if item.tag == "item":
                """"""