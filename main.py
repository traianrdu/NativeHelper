from Manager.AndroidManager import AndroidManager


def test_prototype():
    # Test and debug the given script.
    am = AndroidManager("<string name=\"ioji\">abc</string>")
    am.convert_to_iOS()


if __name__ == '__main__':
    test_prototype()
