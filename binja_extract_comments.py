import time
from pathlib import Path
from typing import List

from binaryninja.interaction import (
    get_form_input, 
    SaveFileNameField
)

def binja_get_all_comments(bv) -> List[str]:
    """
    Return all the function comments from a given binary view in a special format.
    :params bv: binaryninja.binaryview.BinaryView
    :returns entries: list of function comments in the form of a string 
                      0xaddress|function_prototype(int arg1, int arg2)|comment
    """
    entries = []
    for fun in bv.functions:
        for addr, comment in fun.comments.items():
            tokens = [hex(addr), str(fun), str(comment)]
            line = "|".join(tokens)
            entries.append(line)
    return entries

def extract_comments(bv):
    """
    Ask the user for an outgoing filepath for saving the comments extracted from
    a given binary view.
    :params bv: binaryninja.binaryview.BinaryView
    """
    comments = binja_get_all_comments(bv)
    
    field = SaveFileNameField("Save file as")
    get_form_input([field], "Outgoing file")
    if field.result is None:
        print("File save was cancelled!")
        return
    if field.result == "":
        print("Empty filename provided!")
        return
    
    save_file = Path(field.result)
    print("Extracting comments to", str(save_file))
    with open(str(save_file), "w") as fd:
        for comment in comments:
            fd.write(str(comment) + "\n")
    print("Finished extracting.")
