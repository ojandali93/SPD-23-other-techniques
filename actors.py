# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

class Person:
    def __init__(self, f_name, l_name, dob, movies, email):
        self.firstf_name_name = f_name
        self.l_name = l_name
        self.dob = dob
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email)

    def get_full_name(self):
        print(self.first_name + " " + self.last_name)

    def get_movies_played(self):
        print('Movies Played: ' + '')
        for m in self.movies:
            print(m + ', ')
        print()
    
for i, value in enumerate(emails):
    person = Person(first_names[i], last_names[i], birth_year[i], movies[i], value)
    person.get_full_name()
    person.get_movies_played()
    person.send_hiring_email()