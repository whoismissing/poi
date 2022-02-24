import time
from pathlib import Path

from binaryninja.interaction import SaveFileNameField

def binja_get_all_comments(bv):
    entries = []
    for fun in bv.functions:
        for addr, comment in fun.comments.items():
            tokens = [hex(addr), str(fun), str(comment)]
            line = "|".join(tokens)
            entries.append(line)
    return entries

def extract_comments(bv):
    comments = binja_get_all_comments(bv)
    
    epoch = time.time()
    bfilepath = Path(bv.file.filename)
    out_file = str(epoch) + bfilepath.name + ".txt"
    save_file = Path.cwd() / out_file
    print("Extracting comments to", str(save_file))
    with open(str(save_file), "w") as fd:
        for comment in comments:
            fd.write(str(comment) + "\n")
    print("Finished extracting")
