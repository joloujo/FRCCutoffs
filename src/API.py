from abc import ABC, abstractmethod
from typing import Any
import json
from pathlib import Path
# import requests

class API(ABC):
    @classmethod
    @abstractmethod
    def dir(cls, endpoint: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def url(cls, endpoint: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get(cls, endpoint: str) -> Any:
        pass

    @classmethod
    def cahce(cls, endpoint: str, data: Any) -> None:
        path: Path = Path(cls.dir(endpoint))

        path.parent.mkdir(exist_ok=True, parents=True)

        with open(path, 'x') as f:
            json.dump(data, f)

    @classmethod
    def load(cls, endpoint: str) -> Any | None:
        path: Path = Path(cls.dir(endpoint))

        if not path.exists():
            return None
        
        with open(path, 'r') as f:
            return json.load(f)