from xml.etree.ElementTree import Element
from Manager.XMLManager import XMLManager


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
    convert_to_iOS() -> str
        Converts Android string format to iOS Localizable
    parse_xml() -> void
        Parses xml
    is_plurals() -> bool
        Checks if the string is plural format
    is_string_array() -> bool
        Checks if the string is string-array format
    is_string() -> bool
        Checks if the string is string format
    is_comment() -> bool
        Checks if the string is a comment
    is_item() -> bool
        Checks if the string is item
    is_translatable() -> bool
        Checks if the string is translatable
    is_formatted() -> bool
        Checks if the string is formatted
    get_name()
    get_translatable()
    get_formatted()

    strings.xml format
    -------
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <plurals name="plural_name">
            <item quantity=["zero" | "one" | "two" | "few" | "many" | "other"]>text_string</item>
            ---
            <item quantity="one">%d song found.</item>
            <item quantity="other">%d songs found.</item>
            ---
            <item quantity="one">Znaleziono %d piosenkę.</item>
            <item quantity="few">Znaleziono %d piosenki.</item>
            <item quantity="other">Znaleziono %d piosenek.</item>
            ...
        </plurals>
        ...
        <string-array name="planets_array">
            <item>Mercury</item>
            <item>Venus</item>
            <item>Earth</item>
            <item>Mars</item>
        </string-array>
        ...
        <string name="string_name">text_string</string>
        <string name="string_name" translatable="false">text_string</string>
        <string name="string_name" formatted="false">text_string</string>
        <string name="welcome_messages">Hello, %1$s! You have %2$d new messages.</string>
        <string name="welcome">Welcome to <b>Android</b>!</string>
        ...
        <!--comment-->
        ...
    </resources>

    Info
    -------
    Plurals:
    zero	When the language requires special treatment of the number 0 (as in Arabic).
    one	    When the language requires special treatment of numbers like one (as with the number 1 in English and
            most other languages; in Russian, any number ending in 1 but not ending in 11 is in this class).
    two	    When the language requires special treatment of numbers like two (as with 2 in Welsh, or 102
            in Slovenian).
    few	    When the language requires special treatment of "small" numbers (as with 2, 3, and 4 in Czech;
            or numbers ending 2, 3, or 4 but not 12, 13, or 14 in Polish).
    many	When the language requires special treatment of "large" numbers (as with numbers ending 11-99 in
            Maltese).
    other	When the language does not require special treatment of the given quantity (as with all
            numbers in Chinese, or 42 in English).

    Special characters:
    Character                       Escaped form
    @	                            \@
    ----------------------------------------------------------------------------------------------------------------
    ?	                            \?
    ----------------------------------------------------------------------------------------------------------------
    New line	                    \n
    ----------------------------------------------------------------------------------------------------------------
    Tab	                            \t
    ----------------------------------------------------------------------------------------------------------------
    U+XXXX Unicode character	    \ uXXXX
    ----------------------------------------------------------------------------------------------------------------
    Single quote (')                Any of the following:
                                        \'
                                        Enclose the entire string in double quotes ("This'll work", for example)
    ----------------------------------------------------------------------------------------------------------------
    Double quote (")	            \"
                                    Note that surrounding the string with single quotes does not work.

    Formatting strings:
    %1$s is a string
    %2$d is a decimal number

    HTML markup:
    Bold: <b>, <em>
    Italic: <i>, <cite>, <dfn>
    25% larger text: <big>
    20% smaller text: <small>
    Setting font properties: <font face=”font_family“ color=”hex_color”>. Examples of possible font families include
                             monospace, serif, and sans_serif.
    Setting a monospace font family: <tt>
    Strikethrough: <s>, <strike>, <del>
    Underline: <u>
    Superscript: <sup>
    Subscript: <sub>
    Bullet points: <ul>, <li>
    Line breaks: <br>
    Division: <div>
    CSS style: <span style=”color|background_color|text-decoration”>
    Paragraphs: <p dir=”rtl | ltr” style=”…”>

    Styling with annotations:
    // values/strings.xml
    <string name="title">Best practices for <annotation font="title_emphasis">text</annotation> on Android</string>

    // values-es/strings.xml
    <string name="title"><annotation font="title_emphasis">Texto</annotation> en Android: mejores prácticas</string>

    More info:  https://developer.android.com/guide/topics/resources/string-resource
    """

    def __init__(self, strings_xml: str):
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

        """
        delete_list = ["<string name="]
        change_list = ["\">"]
        change_list2 = ["</string>"]
        line = self.strings_xml
        for word in delete_list:
            line = line.replace(word, "")
        for word in change_list:
            line = line.replace(word, "\" = \"")
        for word in change_list2:
            line = line.replace(word, "\"")
        print(line)"""
        localizable_list = []   # empty list of localizable
        xmlManager = XMLManager(self.strings_xml)   # init manager
        root = xmlManager.get_root()    # parse XML

        for child in root:  # get child
            if self.is_plurals(child):  # checks if it is plural
                plural_name = self.get_name(child)  # get the name attribute
                for item in child:  # get item
                    localizable_list.append(self.convert_plurals_item_to_IOS(item, plural_name))    # append the list
        print(localizable_list)

    def test(self):
        """Test functionalities"""
        xmlManager = XMLManager(self.strings_xml)
        root = xmlManager.get_root()

        print(self.strings_xml)
        for child in root:
            print(child.tag, child.attrib, child.text)
        print(root.tag, root.attrib, root.text)

    def test2(self):
        """Test functionalities"""
        xmlManager = XMLManager(self.strings_xml)
        root = xmlManager.get_root()

        for child in root:
            if self.is_plurals(child):
                plural_name = self.get_name(child)
                print(plural_name)
                for items in child:
                    print(items.tag, items.attrib, items.text)
                    # print(next(iter(items.attrib.values())))
                    item_quantity = self.get_quantity(items)
                    if "%d" in items.text:
                        localizable_text = "\"" + plural_name + "_" + item_quantity + "\" = \"" + \
                                           self.get_filtered_formatter(items.text) + "\";"
                    else:
                        localizable_text = "\"" + plural_name + "_" + item_quantity + "\" = \"" + items.text + "\";"
                    print(localizable_text)

    @staticmethod
    def is_plurals(child: Element) -> bool:
        """Checks if the string is plural format

        Parameters
        ----------
        child: Element
            a child element from the parsed XML

        Returns
        -------
        bool
            True if the string is a plural
            False if the string is not a plural
        """
        if child.tag == "plurals":
            return True
        return False

    def convert_plurals_item_to_IOS(self, item: Element, plural_name: str) -> str:
        """Converts plurals item to IOS Localizable

        Parameters
        ----------
        item: Element
            a child element from the parsed XML
        plural_name: str
            name used in Localizable naming

        Returns
        -------
        str
            Localizable text
        """
        item_quantity = self.get_quantity(item)
        if "%d" in item.text:
            localizable_text = "\"" + plural_name + "_" + item_quantity + "\" = \"" + \
                               self.get_filtered_formatter(item.text) + "\";"
        else:
            localizable_text = "\"" + plural_name + "_" + item_quantity + "\" = \"" + item.text + "\";"
        return localizable_text

    def is_string_array(self) -> bool:
        """Checks if the string is string-array format

        Parameters
        ----------

        Returns
        -------
        bool
            True if the string is a string-array
            False if the string is not a string-array
        """

    def is_string(self) -> bool:
        """Checks if the string is string format

        Parameters
        ----------

        Returns
        -------
        bool
            True if the string is a string type format
            False if the string is not a string type format
        """

    def is_comment(self) -> bool:
        """Checks if the string is a comment

        Parameters
        ----------

        Returns
        -------
        bool
            True if the string is a comment
            False if the string is not a comment
        """

    @staticmethod
    def get_name(child: Element) -> str:
        """Returns name of the element

        Parameters
        ----------
        child: Element
            a child element from the parsed XML

        Returns
        -------
        str
            name of the element
        """
        return child.attrib['name']

    @staticmethod
    def get_quantity(child: Element) -> str:
        """Returns quantity attribute

        Parameters
        ----------
        child: Element
            a child element from the parsed XML

        Returns
        -------
        str
            quantity attribute
        """
        return child.attrib['quantity']

    @staticmethod
    def get_filtered_formatter(string: str) -> str:
        """Filters the text and replaces the string with correct formatter

        Parameters
        ----------
        string: str
            basic string that contains %d

        Returns
        -------
        str
            formatted string
        """
        return string.replace("%d", "%@")
