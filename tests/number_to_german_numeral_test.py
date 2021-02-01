import pytest
from number_to_german_numeral import number_to_german_numeral


def test_numbers():
    """
    text_of_number function must return the associated text of the number
    when number 0 until 100 is given
    """

    assert number_to_german_numeral(0) == "null"
    assert number_to_german_numeral(1) == "eins"
    assert number_to_german_numeral(2) == "zwei"
    assert number_to_german_numeral(3) == "drei"
    assert number_to_german_numeral(4) == "vier"
    assert number_to_german_numeral(5) == "fuenf"
    assert number_to_german_numeral(6) == "sechs"
    assert number_to_german_numeral(7) == "sieben"
    assert number_to_german_numeral(8) == "acht"
    assert number_to_german_numeral(9) == "neun"

    assert number_to_german_numeral(10) == "zehn"
    assert number_to_german_numeral(11) == "elf"
    assert number_to_german_numeral(12) == "zwoelf"
    assert number_to_german_numeral(13) == "dreizehn"
    assert number_to_german_numeral(14) == "vierzehn"
    assert number_to_german_numeral(15) == "fuenfzehn"
    assert number_to_german_numeral(16) == "sechzehn"
    assert number_to_german_numeral(17) == "siebzehn"
    assert number_to_german_numeral(18) == "achtzehn"
    assert number_to_german_numeral(19) == "neunzehn"

    assert number_to_german_numeral(20) == "zwanzig"
    assert number_to_german_numeral(21) == "einundzwanzig"
    assert number_to_german_numeral(22) == "zweiundzwanzig"
    assert number_to_german_numeral(23) == "dreiundzwanzig"
    assert number_to_german_numeral(24) == "vierundzwanzig"
    assert number_to_german_numeral(25) == "fuenfundzwanzig"
    assert number_to_german_numeral(26) == "sechsundzwanzig"
    assert number_to_german_numeral(27) == "siebenundzwanzig"
    assert number_to_german_numeral(28) == "achtundzwanzig"
    assert number_to_german_numeral(29) == "neunundzwanzig"

    assert number_to_german_numeral(30) == "dreissig"
    assert number_to_german_numeral(31) == "einunddreissig"
    assert number_to_german_numeral(32) == "zweiunddreissig"
    assert number_to_german_numeral(33) == "dreiunddreissig"
    assert number_to_german_numeral(34) == "vierunddreissig"
    assert number_to_german_numeral(35) == "fuenfunddreissig"
    assert number_to_german_numeral(36) == "sechsunddreissig"
    assert number_to_german_numeral(37) == "siebenunddreissig"
    assert number_to_german_numeral(38) == "achtunddreissig"
    assert number_to_german_numeral(39) == "neununddreissig"

    assert number_to_german_numeral(40) == "vierzig"
    assert number_to_german_numeral(41) == "einundvierzig"
    assert number_to_german_numeral(42) == "zweiundvierzig"
    assert number_to_german_numeral(43) == "dreiundvierzig"
    assert number_to_german_numeral(44) == "vierundvierzig"
    assert number_to_german_numeral(45) == "fuenfundvierzig"
    assert number_to_german_numeral(46) == "sechsundvierzig"
    assert number_to_german_numeral(47) == "siebenundvierzig"
    assert number_to_german_numeral(48) == "achtundvierzig"
    assert number_to_german_numeral(49) == "neunundvierzig"

    assert number_to_german_numeral(50) == "fuenfzig"
    assert number_to_german_numeral(51) == "einundfuenfzig"
    assert number_to_german_numeral(52) == "zweiundfuenfzig"
    assert number_to_german_numeral(53) == "dreiundfuenfzig"
    assert number_to_german_numeral(54) == "vierundfuenfzig"
    assert number_to_german_numeral(55) == "fuenfundfuenfzig"
    assert number_to_german_numeral(56) == "sechsundfuenfzig"
    assert number_to_german_numeral(57) == "siebenundfuenfzig"
    assert number_to_german_numeral(58) == "achtundfuenfzig"
    assert number_to_german_numeral(59) == "neunundfuenfzig"

    assert number_to_german_numeral(60) == "sechszig"
    assert number_to_german_numeral(61) == "einundsechszig"
    assert number_to_german_numeral(62) == "zweiundsechszig"
    assert number_to_german_numeral(63) == "dreiundsechszig"
    assert number_to_german_numeral(64) == "vierundsechszig"
    assert number_to_german_numeral(65) == "fuenfundsechszig"
    assert number_to_german_numeral(66) == "sechsundsechszig"
    assert number_to_german_numeral(67) == "siebenundsechszig"
    assert number_to_german_numeral(68) == "achtundsechszig"
    assert number_to_german_numeral(69) == "neunundsechszig"

    assert number_to_german_numeral(70) == "siebzig"
    assert number_to_german_numeral(71) == "einundsiebzig"
    assert number_to_german_numeral(72) == "zweiundsiebzig"
    assert number_to_german_numeral(73) == "dreiundsiebzig"
    assert number_to_german_numeral(74) == "vierundsiebzig"
    assert number_to_german_numeral(75) == "fuenfundsiebzig"
    assert number_to_german_numeral(76) == "sechsundsiebzig"
    assert number_to_german_numeral(77) == "siebenundsiebzig"
    assert number_to_german_numeral(78) == "achtundsiebzig"
    assert number_to_german_numeral(79) == "neunundsiebzig"

    assert number_to_german_numeral(80) == "achtzig"
    assert number_to_german_numeral(81) == "einundachtzig"
    assert number_to_german_numeral(82) == "zweiundachtzig"
    assert number_to_german_numeral(83) == "dreiundachtzig"
    assert number_to_german_numeral(84) == "vierundachtzig"
    assert number_to_german_numeral(85) == "fuenfundachtzig"
    assert number_to_german_numeral(86) == "sechsundachtzig"
    assert number_to_german_numeral(87) == "siebenundachtzig"
    assert number_to_german_numeral(88) == "achtundachtzig"
    assert number_to_german_numeral(89) == "neunundachtzig"

    assert number_to_german_numeral(90) == "neunzig"
    assert number_to_german_numeral(91) == "einundneunzig"
    assert number_to_german_numeral(92) == "zweiundneunzig"
    assert number_to_german_numeral(93) == "dreiundneunzig"
    assert number_to_german_numeral(94) == "vierundneunzig"
    assert number_to_german_numeral(95) == "fuenfundneunzig"
    assert number_to_german_numeral(96) == "sechsundneunzig"
    assert number_to_german_numeral(97) == "siebenundneunzig"
    assert number_to_german_numeral(98) == "achtundneunzig"
    assert number_to_german_numeral(99) == "neunundneunzig"

    assert number_to_german_numeral(100) == "einhundert"


def test_error_not_int():
    """
    text_of_number function should throw error if given number argument is not an int
    """

    with pytest.raises(TypeError, match="number must be int"):
        number_to_german_numeral("eins")


def test_error_smaller_than_zero():
    """
    text_of_number function should throw error if given number argument is below zero
    """

    with pytest.raises(ValueError, match="number must be int inbetween 0 and 100"):
        number_to_german_numeral(-1)


def test_error_greater_than_hundred():
    """
    text_of_number function should throw error if given number argument is above one hunderd
    """

    with pytest.raises(ValueError, match="number must be int inbetween 0 and 100"):
        number_to_german_numeral(101)
