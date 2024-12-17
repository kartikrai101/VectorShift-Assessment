from pydantic import BaseModel
from typing import List, Dict

# defining model for node(vertex)
class Node(BaseModel):
    id: str
    type: str
    position: Dict[str, float]
    data: Dict[str, str]

# defining model for edge
class Edge(BaseModel):
    id: str
    source: str
    target: str
    type: str

# defining model for data
class PipelineData(BaseModel):
    nodes: List[Node]
    edges: List[Edge]