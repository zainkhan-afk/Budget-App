data = {
            "Faryal" : {
                "accounts" : {"HBL" : 10000}
            },
            "Zain" : {
                "accounts" : {"SCB" : 5000, "ABL" : 10, "HBL" : 2000, "Credit Card" : -2000}
            }

        }


def get_user_data(username):
    return data[username]