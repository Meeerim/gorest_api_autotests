import dataclasses


@dataclasses.dataclass
class User:
    full_name: str = "Mary Sk "
    gender: str = "female"
    status: str = "active"


user = User()
