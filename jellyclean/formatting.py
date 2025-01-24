import re


def validate(entry) -> re.Match | None:
    """Validate file or directory name to match dot-separated movie title and release year

    Example:
        Happy.Gilmore.1996
        Happy.Gilmore.1996.mkv
    """
    return re.match(r"^(\w+\.)+\d{4}(.mkv|.mp4)?$", entry)


def reformat(original_name: str) -> str:
    """Reformat file and directory names to dot-separated movie title and release year

    Example:
        Happy.Gilmore.1996
        Happy.Gilmore.1996.mkv
    """

    cleaned_name: str = re.sub(r"\s", ".", original_name)
    cleaned_name: str = re.sub(r"[\(\)]", "", cleaned_name)

    cutoff: int = 0
    for year_match in re.finditer(r"(?<=.)\b(?:19|20)\d{2}\b", cleaned_name):
        cutoff = year_match.end()

    ext_match: re.Match[str] | None = re.search(r"(.mkv|.mp4)", original_name)
    if ext_match:
        return cleaned_name[:cutoff] + ext_match.group()

    return cleaned_name[:cutoff]
