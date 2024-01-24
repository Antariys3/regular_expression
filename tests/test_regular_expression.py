import pytest

from regular.regular_expression import (
    find_emails,
    search_emails_using_groups,
    find_date,
    find_phone_numbers,
    find_sentences,
)


@pytest.mark.parametrize("input_text, expected_emails", [
    ("andre.33@gmail.com, andre-tarasenko@live.com", ["andre.33@gmail.com", "andre-tarasenko@live.com"]),
    ("123Dima-123@gmail.com, 123+321@live.ua", ["123Dima-123@gmail.com", "123+321@live.ua"]),
    ("example2gmail.com", []),
    ("example@gmail.", []),
])
def test_find_email(input_text, expected_emails):
    assert find_emails(input_text) == expected_emails


@pytest.mark.parametrize("input_text, expected_emails", [
    ("andre.33@gmail.com, andre-tarasenko@live.com", ["andre.33@gmail.com", "andre-tarasenko@live.com"]),
    ("123Dima-123@gmail.com, 123+321@live.ua", ["123Dima-123@gmail.com", "123+321@live.ua"]),
    ("example2gmail.com", []),
    ("example@gmail.", []),
])
def test_search_emails_using_groups(input_text, expected_emails):
    assert search_emails_using_groups(input_text) == expected_emails


@pytest.mark.parametrize("input_text, expected_date", [
    ("12/02/1989", ["12/02/1989"]),
    ("12,02,1989", []),
    ("12-02-1989", []),
    ("12.02.1989", []),
])
def test_find_date(input_text, expected_date):
    assert find_date(input_text) == expected_date


@pytest.mark.parametrize("input_text, expected_phone_numbers", [
    ("+380-63-768-1113, +1-345-540-450", ["+380-63-768-1113", "+1-345-540-450"]),
    ("+3 233 768 111", []),
    ("+3233768111", []),
    ("+1-345-540-4", []),
])
def test_find_phone_numbers(input_text, expected_phone_numbers):
    assert find_phone_numbers(input_text) == expected_phone_numbers


@pytest.mark.parametrize("input_text, expected_sentences", [
    ("One!", ["One!"]),
    ("One. Two?", ["One.", "Two?"]),
    ("One. Two. Three.", ["One.", "Two.", "Three."]),
])
def test_find_sentences(input_text, expected_sentences):
    assert find_sentences(input_text) == expected_sentences
