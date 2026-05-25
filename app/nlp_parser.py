# app/nlp_parser.py

import re


def parse_math_query(text):
    """
    Mengubah natural language menjadi ekspresi matematika
    """

    # lowercase
    text = text.lower().strip()

    # HAPUS KATA TIDAK PENTING
    useless_words = ["berapa", "hitung", "hasil", "dari"]

    for word in useless_words:
        text = text.replace(word, "")

    # Mapping operator bahasa natural
    replacements = {
        "ditambah": "+",
        "tambah": "+",
        "plus": "+",
        "dikurangi": "-",
        "kurang": "-",
        "minus": "-",
        "dikali": "*",
        "kali": "*",
        "dibagi": "/",
        "bagi": "/",
    }

    # Replace kata jadi simbol
    for key, value in replacements.items():
        text = text.replace(key, value)

    # HANYA IZINKAN:
    # angka + operator matematika
    text = re.sub(r"[^0-9+\-*/(). ]", "", text)

    # Hapus spasi berlebih
    text = re.sub(r"\s+", "", text)

    if text == "":
        return None

    return text
