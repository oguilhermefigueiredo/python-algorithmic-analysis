
# Object-oriented programming in Python with a real-world example.
# I Use destructuring inside the loop to check the values of a dictionary and 
# return as output a collection with online and offline users in according to
# their status.

users_dictionary = {'user1': 'online', 'user2': 'offline', 'user3': 'online', 'user4':
        'online', 'user5': 'offline'}

def analyze_dict(dictionary) :
    for user, status in dictionary.copy().items():
        # Online collection
        if 'online' in status:
            print(user, status)

        # Offline collection
        elif 'offline' in status:
            print(user, status)

analyze_dict(users_dictionary)
