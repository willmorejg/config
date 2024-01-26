from dataclasses import dataclass

@dataclass
class ConfigFormatMixin():
    format_id: str
    extension: str
    library: object
