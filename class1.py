class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self):
        """Returns person's name and age as a tuple."""
        return self.name, self.age


# Only run input prompts if the script is executed directly
if __name__ == "__main__":
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))  # Convert input to integer
    p1 = Person(name, age)
    print(p1.name)
    print(p1.age)