from collections import deque
import random


class MMDT:
    def __init__(self):
        self.requests = deque()

    def add_request(self, request):
        self.requests.append(request)

    def process_requests(self) -> bool:
        while self.requests:
            request = self.requests.popleft()
            return self.generateLogin(request)

    def generateLogin(self, username: str) -> str:
        random_numbers = ""

        random_number = random.randint(0, 999)
        random_number = f"{random_number:03d}"

        return username + random_number

    def is_empty(self) -> bool:
        return len(self.requests) == 0

    def size(self) -> int:
        return len(self.requests)


mmdt = MMDT()

print("Type 'exit' to stop adding requests")
while True:
    user_name = input("Enter your username: ")
    if user_name == "exit":
        break
    mmdt.add_request(user_name)


while not mmdt.is_empty():
    print(mmdt.size())
    print(mmdt.process_requests())
