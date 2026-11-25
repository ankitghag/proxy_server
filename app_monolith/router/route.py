from dataclasses import dataclass

@dataclass
class croute:
    prefix: str
    upstream: list

@dataclass
class csroute:
    url: str
    health:bool= True

