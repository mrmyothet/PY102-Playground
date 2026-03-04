class mmdt:
    def __init__(self, id: str):
        self.id = id
        self.courses_taken = []

    def add_course(self, course_id: str):
        self.courses_taken.append(course_id)

mm1 = mmdt("PY102001009")
mm1.add_course("PY101")
mm1.add_course("PY102")
mm1.add_course("MMDT: DE")
mm1.add_course("MMDT: Tableau")

mm2 = mmdt("PY102001037")
mm2.add_course("PY101")
mm2.add_course("MMDT: DE")