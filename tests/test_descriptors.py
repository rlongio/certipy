import pytest

from src.certipy.descriptors import (
    Path,
    File,
    Folder,
    Frequency,
    Required,
    _is_empty,
)


class TestPath:
    class DummyClass:
        path = Path()

        def __init__(self, path):
            self.path = path

    def testPath_whenGivenValidFile_returnsFilePath(self, create_file):
        file = create_file
        assert self.DummyClass(file).path == file

    def testPath_whenGivenValidFolder_returnsFolderPath(self, create_folder):
        folder = create_folder
        assert self.DummyClass(folder).path == folder

    def testPath_whenGivenInvalidPath_raisesValueError(self):
        with pytest.raises(ValueError) as error:
            self.DummyClass("invalid_path")
        assert "invalid_path" in str(error)


class TestFile:
    class DummyClass:
        path = File()

        def __init__(self, file):
            self.path = file

    def testFile_whenGivenValidFilePath_returnsFilePath(self, create_file):
        file = create_file
        assert self.DummyClass(file).path == file

    def testFile_whenGivenValidFolder_raisesValueError(self, create_folder):
        folder = create_folder
        with pytest.raises(ValueError) as error:
            self.DummyClass(folder)
        assert "whenGivenValidFolder" in str(error)


class TestFolder:
    class DummyClass:
        path = Folder()

        def __init__(self, folder):
            self.path = folder

    def testFile_whenGivenValidFolderPath_returnsFilePath(self, create_folder):
        folder = create_folder
        assert self.DummyClass(folder).path == folder

    def testFile_whenGivenValidFile_raisesValueError(self, create_file):
        file = create_file
        with pytest.raises(ValueError) as error:
            self.DummyClass(file)
        assert "whenGivenValidFile" in str(error)


class TestFrequency:
    class DummyClass:
        frequency = Frequency()

        def __init__(self, frequency):
            self.frequency = frequency

    def testFrequency_whenGivenValidFrequency_returnsFrequencyInSeconds(self):
        frequency = "2m"
        actual = self.DummyClass(frequency)
        assert actual.frequency == 120

    def testFile_whenGivenInvalidFrequency_raisesValueError(self):
        frequency = "2x"
        with pytest.raises(ValueError) as error:
            self.DummyClass(frequency)
        assert "frequency" in str(error)


class TestRequired:
    class DummyClass:
        required = Required()

        def __init__(self, required_value):
            self.required = required_value

    def testRequired_whenGivenData_returnsSameData(self):
        required_value = "some required value"
        actual = self.DummyClass(required_value)
        assert actual.required == required_value

    def testRequired_whenGivenFalsyValidData_returnsSameData(self):
        required_value = 0
        actual = self.DummyClass(required_value)
        assert actual.required == required_value

    def testRequired_whenGivenEmptyString_raisesValueError(self):
        required_value = ""
        with pytest.raises(ValueError) as error:
            self.DummyClass(required_value)
        assert "required" in str(error)


# class TestInteger:
#     class DummyClass:
#         _integer = Integer()

#         def __init__(self, _integer):
#             self._integer = _integer

#     def testInteger_whenGivenValidIntegerString_returnsValueAsString(self):
#         _integer = "2"
#         actual = self.DummyClass(_integer)
#         assert actual._integer == "2"


#     def testFile_whenGivenInvalidFrequency_raisesValueError(self):
#         _integer = "x"
#         with pytest.raises(ValueError) as error:
#             self.DummyClass(_integer)
#         assert "x" in str(error)


def testIsEmpty_returnsTrue_ifValueIsNoneOrEmptyString():
    assert _is_empty("") is True
    assert _is_empty(None) is True