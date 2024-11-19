from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PriorityNode:
    priority: int
    item: Any=field(compare=False)