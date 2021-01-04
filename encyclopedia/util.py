import re
from markdown2 import Markdown
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def convert_markdown_to_html(markdown):
    """
    Basic markdown to HTML converter. 
    """    
    # I attempted to do a markdown to html converter, but I gave up in the middle, ignore the following code.

    """
    # Match h1's (1 #)
    heading_1_regex = re.compile(r"^#\s*(\w+)", re.MULTILINE)
    result = re.sub(heading_1_regex, r"<h1>\1</h1>", markdown)

    # Match h2's (2 ##)
    heading_2_regex = re.compile(r"^##\s*(\w+)", re.MULTILINE)
    result = re.sub(heading_2_regex, r"<h2>\1</h2>", result)

    # Match Bold Text (**TEXT**)
    bold_text_regex = re.compile(r"\*\*(.*?)\*\*")
    result = re.sub(bold_text_regex, r"<b>\1</b>", result)

    # Links
    link_regex = re.compile(r"\[(.*?)\]\((.*?)\)")
    result = re.sub(link_regex, r'<a href="\2">\1</a>', result)

    # Unordered Lists
    ul_list_regex = re.compile(r"^((?:[\*\-].*)+)", re.MULTILINE)
    result = re.sub(ul_list_regex, r'<ul>\1</ul>', result)

    """



    result = Markdown().convert(markdown)
    return result
    


    
