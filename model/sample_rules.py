"""Creation of rules"""
from load_configuration import load_configuration_file


def create_rules():
    """Creating rules , Returning string"""
    data = load_configuration_file()

    coins = "("
    for coin in data['cryptocoins']:
        coins = coins + coin + " OR "
    coins = coins[:-4]+')'

    sample_rules=[]
    for handle in data['Handle']:
        sample_rules.append({"value": "{} from:{}".format(coins, handle), "tag": "{}".format(handle)})

    return sample_rules


