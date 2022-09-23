from data import gamedata
import random
count = 0
game_continue = True
account_a = random.choice(gamedata)
account_b = random.choice(gamedata)
while game_continue:
    account_a = account_b
    account_b = random.choice(gamedata)

    if account_b == account_a:
        account_b = random.choice(gamedata)


    def account_details(account):
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f" {account_name} is a {account_description} from {account_country}"


    def followers_count(account):
        return account["follower_count"]


    print("############  The Up-Down game begins  ###########")
    print(f"Choice A:{account_details(account_a)}")
    print("vs")
    print(f"Against B:{account_details(account_b)}")
    user_choice = input("Enter your choice of a or b: ").lower()
    a_followers = followers_count(account_a)
    b_followers = followers_count(account_b)

    if user_choice == "a":
        user_guess = followers_count(account_a)

    elif user_choice == "b":
        user_guess = followers_count(account_b)
    else:
        print("")

    if user_guess > b_followers:
        if user_guess == a_followers:
            game_continue = True
            count = count + 1
            print(f"You are correct and your score is {count}")
    elif user_guess > a_followers:
        if user_guess == b_followers:
            game_continue = True
            count = count + 1
            print(f"You are correct and your score is {count}")

    else:
        count
        print(f"you loose and your score is {count}")
        game_continue = False


