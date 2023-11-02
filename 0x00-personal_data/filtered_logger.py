#!/usr/bin/env python3
"""Personal data handling
"""
from typing import List
import logging
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter datum
    """
    pattern = '|'.join(map(re.escape, fields))
    return re.sub(f'({pattern})=[^({separator})]+', f'\\1={redaction}', message)
