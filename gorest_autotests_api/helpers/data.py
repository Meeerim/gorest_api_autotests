import dataclasses


@dataclasses.dataclass
class User:
    full_name: str = "Mary Sk "
    email: str = "test_onetwothree@gmail.com"
    gender: str = "female"
    status: str = "active"
    email2: str = "mtestsecond@gmail.com"


user = User()
