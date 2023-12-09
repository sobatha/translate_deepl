import pytest
from app.deepl_translator.translate import translate_test_file


def test_translate():
    translate_test_file()
