from dataclasses import dataclass


@dataclass
class Result:
  success: bool
  description: str
  score: int
