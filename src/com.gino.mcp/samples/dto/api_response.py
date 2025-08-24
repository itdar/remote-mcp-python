from typing import Any, Dict
from dataclasses import dataclass

@dataclass
class ApiResponse:
    status: str
    data: Any = None
    error: str = None
    example: str = None

    def to_dict(self) -> Dict[str, Any]:
        result = {"status": self.status}
        if self.data is not None:
            result["data"] = self.data
        if self.error is not None:
            result["error"] = self.error
        if self.example is not None:
            result["example"] = self.example
        return result
