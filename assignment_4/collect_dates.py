import re
from typing import Tuple

## -- Task 3 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

...


def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"\b(1[0-9]{3}|20[0-2][0-9])\b"
    # month should accept month names or month numbers
    month = r"\b([jJ]an(?:uary)?|[fF]eb(?:ruary)?|[mM]ar(?:ch)?|[aA]pr(?:il)?|[mM]ay|[jJ]un(?:e)?|[jJ]ul(?:y)?|[aA]ug(?:ust)?|[sS]ep(?:tember)?|[oO]ct(?:ober)?|[nN]ov(?:ember)?|[dD]ec(?:ember)?)\b"
    # day should be a number, which may or may not be zero-padded
    day = r"\b([1-9]|[0-2][0-9]|3[0-1])\b"

    return year, month, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    # If already digit do nothing
    if s.isdigit():
        return s
    else:                       # Convert to number as string
        month_pat = [
        r"[jJ]an(?:uary)?", r"[fF]eb(?:ruary)?", r"[mM]ar(?:ch)?", r"[aA]pr(?:il)?",
            r"[mM]ay", r"[jJ]un(?:e)?", r"[jJ]ul(?:y)?", r"[aA]ug(?:ust)?",
                r"[sS]ep(?:tember)?", r"[oO]ct(?:ober)?", r"[nN]ov(?:ember)?", r"[dD]ec(?:ember)?"
                        ]
        for indx, month in enumerate(month_pat):
            pat = re.compile(month)
            match = pat.search(s)
            if match:
                s = zero_pad(f"{indx + 1}")
                return s


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.
    """
    if len(n) == 2:
        return n
    else:
        n = "".join(("0",n))
        return n


def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """
    year, month, day = get_date_patterns()
    results = []

    # Date on format YYYY/MM/DD - ISO
    ISO = ...
    iso_pat = re.compile(r"\b(1[0-9][0-9][0-9]|20[0-2][0-9])-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-2])\b")
    ISO_matches = iso_pat.findall(text)
    for dates in ISO_matches:
        y, m, d = dates
        results.append("/".join((y,m,d)))

    # Date on format DD/MM/YYYY

    DMY_pat = re.compile(day+" "+month+" "+year)
    DMY_matches = DMY_pat.findall(text)
    for dates in DMY_matches:
        d, m, y = dates
        m = convert_month(m)
        d = zero_pad(d)
        results.append("/".join((y,m,d)))

    # Date on format MM/DD/YYYY
    MDY_pat = re.compile(month+" "+day+","+" "+year)
    MDY_matches = MDY_pat.findall(text)
    for dates in MDY_matches:
        m, d, y = dates
        m = convert_month(m)
        d = zero_pad(d)
        results.append("/".join((y,m,d)))

    # Date on format YYYY/MM/DD
    YMD_pat = re.compile(year+" "+month+" "+day)
    YMD_matches = YMD_pat.findall(text)
    for dates in YMD_matches:
        y, m, d = dates
        m = convert_month(m)
        d = zero_pad(d)
        results.append("/".join((y,m,d)))

    # list with all supported formats
    # formats = ...
    # dates = []

    # find all dates in any format in text

    # Write to file if wanted
    if output:
        with open(output, "a") as outfile:
            for date in results:
                outfile.write(date + "\n")


    return results


if __name__ == "__main__":
    some_dates = """
    2 January 2020
    february 4, 1987
    1996-12-23
    2010-10-12 1939-03-22 March 19, 1555 12 september 1948
    1 december 1789 1996-12-23
    """
    dates = find_dates(some_dates)
    breakpoint()
