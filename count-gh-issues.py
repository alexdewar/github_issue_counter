#!/usr/bin/env python

import json
import subprocess as sp
import sys
from datetime import datetime
import dateparser

def main(user: str, from_date_str: str):
    from_date = dateparser.parse(from_date_str)
    cmd = f"gh search issues --assignee {user} --state open -L 1000 --json updatedAt"

    ret = sp.run(cmd.split(" "), capture_output=True)
    dates = (datetime.fromisoformat(val["updatedAt"]) for val in json.loads(ret.stdout))
    count = len(list(date > from_date for date in dates))
    print(count)

if __name__ == "__main__":
    main(sys.argv[1])