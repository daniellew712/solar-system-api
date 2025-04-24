# class Planet:
#     def __init__(self, id, name, description, size):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size

# planets = [
#     Planet(1, "Jupiter", "Orange and White", 142984),
#     Planet(2, "Saturn", "Yellow-Brown", 120536),
#     Planet(3, "Earth","Blue", 12742),
#     Planet(4, "Mars", "Red", 6792)
# ]


from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[int]