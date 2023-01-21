# chaining is ... user1.display_info().enroll().spend_points(50).display_info()
# each method must return self
# each method call will be equal to the instance that called it
# not possible to chain the method

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self
    def enroll(self):
        if self.is_rewards_member:
            print("Already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Cannot complete the transaction, not enough points")
        else:
            self.gold_card_points -= amount
        return self

melissa = User("Melissa", "Hernadez", "email@email.com", 38)
#print(melissa.is_rewards_member)
#print(melissa.display_info())
#print(melissa.enroll())
#print(melissa.enroll())
#print(melissa.spend_points(50))
#print(melissa.spend_points(50))

melissa.display_info().enroll().display_info().spend_points(50).display_info()
