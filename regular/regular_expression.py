import re

# I did this on purpose for easy reading
letter = "Hello, my personal email is andre.33@gmail.com, my work email is andre-tarasenko@live.com. "
letter += "My personal phone is +48-795-768-450, work number is +48-789-456-321. "
letter += "Date of birth (12,02,1989 or 12-02-1989 or 12/02/1989 or 12.02.1989)."


def find_emails(text):
    pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}")
    return pattern.findall(text)


def search_emails_using_groups(text):
    pattern = re.compile(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})")
    return pattern.findall(text)


def find_date(text):
    pattern = re.compile(r"\d{2}/\d{2}/\d{4}")
    return pattern.findall(text)


def find_phone_numbers(text):
    pattern = re.compile(r".\b[0-9+-]{13,15}")
    return pattern.findall(text)


def find_sentences(text):
    pattern = re.compile(r"(?<=[.!?])\s+")
    return re.split(pattern, text)


if __name__ == "__main__":
    result = find_emails(letter)
    print("list of all emails", result)

    result = search_emails_using_groups(letter)
    print("list of all emails", result)

    result = find_date(letter)
    print("Date in format MM/DD/YYYY.", result)

    result = find_phone_numbers(letter)
    print("list of all phone numbers", result)

    result = find_sentences(letter)
    print("list of all sentences", result)
