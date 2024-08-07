"""The main module for GitHub Issue Counter."""

from importlib.metadata import version

__version__ = version(__name__)


import json
import subprocess as sp
from datetime import datetime


def count_issues(user: str, from_date: datetime) -> int:
    """Count the number of open GitHub issues for a user since a date."""
    cmd = f"gh search issues --assignee {user} --state open -L 1000 --json updatedAt"

    ret = sp.run(cmd.split(" "), capture_output=True)
    dates = (datetime.fromisoformat(val["updatedAt"]) for val in json.loads(ret.stdout))
    return len(list(date > from_date for date in dates))
