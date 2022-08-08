class AndroidManager:
    """
        A class used to represent the Android Manager

        ...

        Attributes
        ----------
        strings_xml : str
            a formatted string that contains Android string file

        Methods
        -------
        convert_to_iOS()
            Converts Android string format to iOS Localizable
        """
    def __init__(self, strings_xml):
        """
        Parameters
        ----------
        strings_xml : str
            a formatted string that contains Android string file
        """
        self.strings_xml = strings_xml

    def convert_to_iOS(self):
        """Converts the Android text to iOS Localizable format

        Parameters
        ----------

        Returns
        -------
        str
            string representation as a Localizable
        """