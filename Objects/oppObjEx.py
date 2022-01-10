class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greetings = 0

    def greet(self, other_person):
        other_person.greetings += 1
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    def contact_info(self):
        print "%s's email: %s, phone number: %s" % (self.name, self.email, self.phone)

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.phone, self.email)

    def num_friends(self):
        print len(self.friends)

    def greeting_count(self):
        print self.greetings

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# Have sonny greet jordan using the greet method.

sonny.greet(jordan)

# Have jordan greet sonny using the greet method.

jordan.greet(sonny)

# Write a print statement to print the contact info (email and phone) of Sonny.

print "%s's phone number is %s and his email is %s." % (sonny.name, sonny.phone, sonny.email)

# Write another print statement to print the contact info of Jordan.

print "%s's phone number is %s and his email is %s." % (jordan.name, jordan.phone, jordan.email)

# Write another print statement to print the contact info of Jordan.

sonny.contact_info()

# add friends variable atrribute and call it.

sonny.friends.append(jordan)

print len(sonny.friends)

# add friend method

jordan.add_friend(sonny)
print len(jordan.friends)
print jordan.friends

# def function for num_friends

jordan.num_friends()

# Count Number of Greetings

jordan.greeting_count()

# =====================VEHICLE CLASS===============================
# class Vehicle(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print self.year, self.make, self.model 

# car = Vehicle("Toyota","Camry","2012")

# car.print_info()

       
