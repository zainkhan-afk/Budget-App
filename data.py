data = {
            "users" : ["user1", "user2"],
            "user1 Budget" : {
                "accounts" : {"A" : 10000}
            },
            "user2 Budget" : {
                "accounts" : {"SCB" : 5000, "ABL" : 10, "HBL" : 2000, "Credit Card" : -2000}
            }

        }


def get_user_data(username):
    return data[username]
