

def read_index_data(data_path):
    """Read file containing index keywords to find in source text.

    Must contain newline delimited data.
    """
    index_keywords = []
    with open(data_path) as data:
        for line in data:
            index_keywords.append(line.rstrip())
    return index_keywords


def build_index():
    """ Build index with link into text."""
    pass


def add_source_achors():
    """ Add anchors to the source text."""
    pass
