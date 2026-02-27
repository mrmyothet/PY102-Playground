from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    id: str = "PY102001009"
    subjects: list = field(default_factory=list)


student1 = Student(name="Alice")
student2 = Student(name="Bob")

student1.subjects.append("Math")
print(student1)
print(student2)
