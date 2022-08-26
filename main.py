from Manager.AndroidManager import AndroidManager


global_string = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" \
                "<resources>" \
                "<plurals name=\"plural_name_abc_name\" abc=\"aaa\">" \
                "<item quantity=\"one\">%d song found.</item>" \
                "<item quantity=\"other\">%d songs found.</item>" \
                "<item quantity=\"one\">Znaleziono %d piosenkę.</item>" \
                "<item quantity=\"few\">Znaleziono %d piosenki.</item>" \
                "<item quantity=\"other\">Znaleziono %d piosenek.</item>" \
                "</plurals>" \
                "<string-array name=\"planets_array\">" \
                "<item>Mercury</item>" \
                "<item>Venus</item>" \
                "<item>Earth</item>" \
                "<item>Mars</item>" \
                "</string-array>" \
                "<string name=\"string_array_name\">text_string</string>" \
                "<string name=\"string_array_name\" translatable=\"false\">text_string</string>" \
                "<string name=\"string_array_name\" formatted=\"false\">text_string</string>" \
                "<string name=\"welcome_messages\">Hello, %1$s! You have %2$d new messages.</string>" \
                "<string name=\"welcome\">Welcome to <b>Android</b>!</string>" \
                "<!--comment-->" \
                "</resources>"

test_string = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" \
              "<resources>" \
              "<string name=\"string_name\">text_string</string>" \
              "</resources>"


def test_prototype():
    # Test and debug the given script.
    am = AndroidManager(global_string)
    #am.test2()
    am.convert_to_iOS()


if __name__ == '__main__':
    test_prototype()
