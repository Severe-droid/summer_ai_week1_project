class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
        self.blocked_friends = []
        self.messages = []

    def add_friend(self, person):
        if person not in self.friends:
            self.friends.append(person)
            person.friends.append(self)

    def block_friend(self, person):
        if person in self.friends:
            self.friends.remove(person)
            person.friends.remove(self)
            self.blocked_friends.append(person)
            person.blocked_friends.append(self)

    def send_message(self, person, message):
        if person in self.friends:
            person.messages.append((self.name, message))
        else:
            print(f"Cannot send message. {person.name} is not your friend.")

class SocialNetwork:
    def __init__(self):
        self.list_of_people = []

    def create_account(self, name, age):
        person = Person(name, age)
        self.list_of_people.append(person)
        print("Account created successfully!")

    def find_person(self, name):
        for person in self.list_of_people:
            if person.name == name:
                return person
        return None

    def add_friend(self, person_name, friend_name):
        person = self.find_person(person_name)
        friend = self.find_person(friend_name)
        if person and friend:
            person.add_friend(friend)
            print(f"{friend_name} added as a friend for {person_name}.")
        else:
            print("Person or friend not found.")

    def block_friend(self, person_name, friend_name):
        person = self.find_person(person_name)
        friend = self.find_person(friend_name)
        if person and friend:
            person.block_friend(friend)
            print(f"{friend_name} blocked by {person_name}.")
        else:
            print("Person or friend not found.")

    def send_message(self, sender_name, recipient_name, message):
        sender = self.find_person(sender_name)
        recipient = self.find_person(recipient_name)
        if sender and recipient:
            sender.send_message(recipient, message)
            print(f"Message sent from {sender_name} to {recipient_name}.")
        else:
            print("Sender or recipient not found.")
