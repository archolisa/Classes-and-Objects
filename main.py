class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__ (self,name,age,track,score):
        self.name = str(name)
        self.age = int(age)
        self.track = list(track)
        self.score = float(score)

    def change_name(self,new_name):
        self.name = new_name
        new_name = "peter"
        print(f"the student upated his name to {new_name}")

    def change_age(self, new_age):
        self.age = new_age
        new_age = 34
        print (f"the student updated his name to {new_age} years old")

    def add_track(self,new_track):
        self.track = new_track
        new_track = ("UI/UX")
        print (f"the student updated his score to {new_track}")

    def get_score(self, new_score):
        self.score = new_score
        new_score = 2.5
        print(f"the student updated his score to {new_score}")

Bob = Student(name = "Bob", age = 26, track = ["FE","BE"],score = 20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(2.5)