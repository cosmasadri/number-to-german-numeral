def number_to_german_numeral(number):
    """[summary]

    Args:
        number ([type]): [description]

    Raises:
        TypeError: [description]
        ValueError: [description]

    Returns:
        [type]: [description]
    """    
    if type(number) != int:
        raise TypeError("number must be int")

    if 0 > number or 100 < number:
        raise ValueError("number must be int inbetween 0 to 100")

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
        string_rev_number = str(number)[::-1]

        for i in range(len(string_rev_number)):

            if i == 0:
                text_number = dict_number[string_rev_number[i]]

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
