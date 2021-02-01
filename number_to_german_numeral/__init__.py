def number_to_german_numeral(number):
    """This function is used to translate number into german numeral.
    Example:
        * 2 -> "zwei"
        * 21 -> "einundzwanzig"
        * 100 -> "einhundert"
    Currently, the function can only translate number from 0 to 100.

    Args:
        number (int): number which is to be translated to german numeral between 0 to 100

    Raises:
        TypeError: number arg must have type of int
        ValueError: number arg must be between 0 and 100

    Returns:
        string: german numeral of number given
    """
    # error handling: number argument must be int
    if type(number) != int:
        raise TypeError("number must be int")
    
    # error handling: number must be inbetween 0 and 100
    if 0 > number or 100 < number:
        raise ValueError("number must be int inbetween 0 and 100")
    
    dict_number = dict(
        [
            ("0", "null"),
            ("1", "eins"),
            ("2", "zwei"),
            ("3", "drei"),
            ("4", "vier"),
            ("5", "fuenf"),
            ("6", "sechs"),
            ("7", "sieben"),
            ("8", "acht"),
            ("9", "neun"),
        ]
    )

    if number == 100:
        return "einhundert"

    else:
        # number is converted to string and reversed
        string_rev_number = str(number)[::-1]

        for i in range(len(string_rev_number)):

            # numeral for the ones
            # (last digit of the actual number, first digit of the reversed number)
            if i == 0:
                text_number = dict_number[string_rev_number[i]]

            # numeral if the number has 2 digits
            elif i == 1:
                if string_rev_number[i] == "1":
                    if string_rev_number[i - 1] == "1":
                        text_number = "elf"
                    elif string_rev_number[i - 1] == "2":
                        text_number = "zwoelf"
                    else:
                        tens_text_number = "zehn"

                        if string_rev_number[i - 1] == "0":
                            text_number = tens_text_number
                        elif string_rev_number[i - 1] == "6":
                            text_number = "sech" + tens_text_number
                        elif string_rev_number[i - 1] == "7":
                            text_number = "sieb" + tens_text_number
                        else:
                            text_number = (
                                dict_number[string_rev_number[i - 1]] + tens_text_number
                            )
                else:
                    if string_rev_number[i - 1] == "1":
                        text_number = "ein"

                    if string_rev_number[i] == "2":
                        tens_text_number = "zwanzig"
                    elif string_rev_number[i] == "3":
                        tens_text_number = dict_number[string_rev_number[i]] + "ssig"
                    elif string_rev_number[i] == "7":
                        tens_text_number = "siebzig"
                    else:
                        tens_text_number = dict_number[string_rev_number[i]] + "zig"

                    if string_rev_number[i - 1] == "0":
                        text_number = tens_text_number
                    else:
                        text_number += "und" + tens_text_number

    return text_number
