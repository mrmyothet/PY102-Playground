class MMDT:
    def __init__(self):
        self.student_list = []
        self.index = []

    def generate_student_list(self):
        prefix = "PY102001"
        for x in range(45):
            student_id = f"{prefix}{x:03d}"
            # print(student_id)
            self.student_list.append(student_id)

    def hash_function(self, student_id, table_size=10):
        id = int(student_id[-3:])
        index = id % table_size
        print(index, "-", student_id)
        return index


mmdt = MMDT()
mmdt.generate_student_list()

for student_id in mmdt.student_list:
    mmdt.hash_function(student_id)
