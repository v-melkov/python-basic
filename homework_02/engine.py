"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: int = 10
    pistons: int = 4
