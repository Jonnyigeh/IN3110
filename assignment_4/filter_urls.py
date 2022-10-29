import re
from urllib.parse import urljoin
from requesting_urls import get_html
## -- Task 2 -- ##


def find_urls(
    html: str,
    base_url: str = "https://en.wikipedia.org",
    output: str = None,
) -> set:
    """Find all the url links in a html text using regex
    Arguments:
        html (str): html string to parse
    Returns:
        urls (set) : set with all the urls found in html text
    """
    # create and compile regular expression(s)
    a_pat = re.compile(r"<a[^\<]+?href=\"[^#]?[^(\"|\>)]*?\"")

    url_base_pat = re.compile(r"href=\"\/[^\/].+(?=\")")            # Matches urls that require base_url in front
    url_other_pat = re.compile(r"href=\"\/\/.+(?=\")")                             # Matches urls from other host needing https:
    url_full_pat = re.compile(r"href=\"https:.+(?=\")")                              # Matches full urls (e.g https://someurl.org)

    # url_base_pat = re.compile(r"\/[a-zA-Z0-9][^\"]+?\"")
    # url_other_pat = re.compile(r"//[^\"]+")
    # url_pat = re.compile(r"https:.+\..[^(\")]{1,3}")
    url_fragment_pat = re.compile(r"#")
    # 1. find all the anchor tags, then
    # 2. find the urls href attributes

    match_set = set()

    for m in a_pat.findall(html):

        fragment_match = url_fragment_pat.search(m)
        if fragment_match:
            try:
                url, frag = re.split("#", m)
                m = "".join((url, "\""))
            except:
                pass

        url_full_match = url_full_pat.search(m)
        if url_full_match:
            href, match = re.split("\"", url_full_match.group(0))
            match_set.add(match)
            continue

        url_other_match = url_other_pat.search(m)
        if url_other_match:
            href, match = re.split("\"", url_other_match.group(0))
            match_set.add("".join(("https:", match)))
            continue

        url_base_match = url_base_pat.search(m)
        if url_base_match:
            href, match = re.split("\"", url_base_match.group(0))
            try:
                match_set.add("".join((base_url, match)))
                continue
            except NameError:
                print("Missing base URL, please specify")
    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        with open(output, "a") as outfile:
            for element in match_set:
                outfile.write(element + "\n")

    urls = match_set

    return urls


def find_articles(html: str, output=None) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
    returns:
        - (set) : a set with urls to all the articles found
    """
    urls = find_urls(html)
    pattern = re.compile(r"[^\.]+\.wikipedia\..+?(?=\/wiki\/)\/wiki\/.*")
    articles = set()
    for url in urls:
        prtcl, rest = re.split("://", url, maxsplit=1)
        excl_pat = re.compile("\:")
        excl = excl_pat.search(rest)
        if excl:
            continue
        match = pattern.search(url)
        if match:
            articles.add(url)

    # Write to file if wanted
    if output:
        with open(output, "a") as outfile:
            for article in articles:
                outfile.write(article + "\n")

    return articles


## Regex example
def find_img_src(html: str):
    """Find all src attributes of img tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        src_set (set): A set of strings containing image URLs

    The set contains every found src attibute of an img tag in the given HTML.
    """
    # img_pat finds all the <img alt="..." src="..."> snippets
    # this finds <img and collects everything up to the closing '>'
    img_pat = re.compile(r"<img[^>]+>", flags=re.IGNORECASE)
    # src finds the text between quotes of the `src` attribute
    src_pat = re.compile(r'src="([^"]+)"', flags=re.IGNORECASE)
    src_set = set()
    # first, find all the img tags
    for img_tag in img_pat.findall(html):
        # then, find the src attribute of the img, if any
        match = src_pat.search(img_tag)
        if match:
            src_set.add(match.group(1))
    return src_set

if __name__ == "__main__":
    html = get_html("https://en.wikipedia.org/wiki/Nobel_Prize")
    # html = """
    # <a href="#fragment-only">anchor link</a>
    # <a id="some-id" href="/relative/path#fragment">relative link</a>
    # <a href="//other.host/same-protocol">same-protocol link</a>
    # <a href="https://example.com">absolute URL</a>
    # <a href="https://examplo.com">absolute URL</a>
    # <a asfas="https://exampli.com">absolute URL</a><a href="https://examplu.com">absolute URL</a>"
    # https://en.wikipedia.org/a></sup> When a prize is awarded to recognise an achievement by a team of more than three collaborators, one or more will miss out. For example, in 2002, the prize was awarded to <a href='
    # <a href="https://en.wikipedia.org/wiki/File"
    # <a href="https://en.wikipedia.org/wiki/File:Nobel_Prize_by_Dimitri_O_Ledenyov_and_Viktor_O_Ledenyov.ogg"
    # """
    urls = find_urls(html)
    articles = find_articles(html)
    breakpoint()
