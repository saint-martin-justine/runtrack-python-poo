class Student:
    def __init__(self, first_name, last_name, student_id):
        self._first_name = first_name
        self._last_name = last_name
        self._student_id = student_id
        self._credits = 0
        self._level = self._studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits

    def studentInfo(self):
        print("Student name:", self._first_name, self._last_name)
        print("Student ID:", self._student_id)
        print("Credits:", self._credits)
        print("Level:", self._level)

    def _studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien."
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Excellent"


# Instancier un objet représentant l’étudiant John Doe qui possède le numéro d’étudiant 145
john = Student("John", "Doe", 145)

# Ajouter des crédits à trois reprises
john.add_credits(30)
john.add_credits(20)
john.add_credits(40)

# Afficher les informations de l'étudiant
john.studentInfo()