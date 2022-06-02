from pydantic import BaseModel
from pydantic.types import Optional
from pydantic.typing import Literal


class TestResult(BaseModel):
    name: str
    class_name: Optional[str]
    method: str
    status: Literal['passed', 'failed']
    assertion_message: str
    description: str
