from .binja_extract_comments import extract_comments

from binaryninja import *

PluginCommand.register("Comment Extractor", "Extracts function comments", extract_comments)    