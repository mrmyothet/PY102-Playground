from dataclasses import dataclass, field


@dataclass
class student:
    name: str = "MMDT"
    id: str = "PY102001009"
    password: str = field(repr=False, default="123")


myothet = student()
print(myothet)
