from typing import Dict, Optional

import requests

## -- Task 1 -- ##


def get_html(url: str, params: Optional[Dict] = None, output: Optional[str] = None):
    """Get an HTML page and return its contents.

    Args:
        url (str):
            The URL to retrieve.
        params (dict, optional):
            URL parameters to add.
        output (str, optional):
            (optional) path where output should be saved.
    Returns:
        html (str):
            The HTML of the page, as text.
    """
    # passing the optional parameters argument to the get function
    if params:
        response = requests.get(url, params=params)
    else:
        response = requests.get(url)
    html_str = response.text

    if output:
        # if output is specified, the response txt and url get printed to a
        # txt file with the name in `output`
        with open(output, "a") as outfile:
            outfile.write(response.url + "\n")
            outfile.write(html_str)

        return None

    return html_str

if __name__ == "__main__":
    str = get_html("https://en.wikipedia.org/wiki/Studio_Ghibli")
