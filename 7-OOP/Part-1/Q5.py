class Instructor:
    def __init__(self):
        self.__name = None
        self.__technology_skills = []
        self.__experience = 0
        self.__average_feedback = 0.0

    def set_name(self, name):
        self.__name = name

    def set_technology_skills(self, skills):
        if isinstance(skills, list):
            self.__technology_skills = skills
        else:
            raise ValueError("Skills should be a list.")

    def set_experience(self, experience):
        self.__experience = experience

    def set_average_feedback(self, feedback):
        self.__average_feedback = feedback


    def check_eligibility(self):
        if self.__experience > 3 and self.__average_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__average_feedback >= 4.0:
            return True
        else:
            return False

    def allocate_course(self, technology):
        if self.check_eligibility() and technology.lower() in [skill.lower() for skill in self.__technology_skills]:
            return True
        else:
            return False

    def display_details(self):
        print(f"Instructor: {self.__name}")
        print(f"Experience: {self.__experience} years")
        print(f"Feedback: {self.__average_feedback}")
        print(f"Skills: {', '.join(self.__technology_skills)}")

instructor1 = Instructor()
instructor1.set_name("Alice")
instructor1.set_technology_skills(["Python", "Java"])
instructor1.set_experience(5)
instructor1.set_average_feedback(4.6)

instructor2 = Instructor()
instructor2.set_name("Bob")
instructor2.set_technology_skills(["C++", "Python"])
instructor2.set_experience(2)
instructor2.set_average_feedback(3.9)

instructor1.display_details()
print("Eligible?", instructor1.check_eligibility())
print("Can be allocated Python course?", instructor1.allocate_course("Python"))
print()

instructor2.display_details()
print("Eligible?", instructor2.check_eligibility())
print("Can be allocated Python course?", instructor2.allocate_course("Python"))

