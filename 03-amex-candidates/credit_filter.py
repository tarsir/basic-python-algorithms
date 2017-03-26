"""
credit_filter.py: Filters American Express cardholders to find candidates for the Centurion card.
"""

SAMPLE_CLIENTS = [
    {
        'name' : 'Ned Stark',
        'credit_score': 790,
        'annual_spend' : 65000
    },
    {
        'name' : 'Randyll Tarly',
        'credit_score': 670,
        'annual_spend' : 75000
    },
    {
        'name' : 'Petyr Baelish',
        'credit_score': 981,
        'annual_spend' : -1453659
    },
    {
        'name' : 'Robert Baratheon',
        'credit_score': 343,
        'annual_spend' : 2345000
    },
    {
        'name' : 'Tywin Lannister',
        'credit_score': 850,
        'annual_spend' : 7450000
    }
]

def valid_credit_scores(client_list):
    return [client for client in client_list if client['credit_score'] >= 300 and client['credit_score'] <= 850]

def centurion_credit_scores(client_list):
    return [client for client in client_list if client['credit_score'] >= 780]

def valid_spend(client_list):
    return [client for client in client_list if client['annual_spend'] >= 0]

def centurion_spend(client_list):
    return [client for client in client_list if client['annual_spend'] >= 450000]

def show_client_list_names(client_list):
    print([client['name'] for client in client_list])

candidate_list = valid_credit_scores(SAMPLE_CLIENTS)
candidate_list = centurion_credit_scores(candidate_list)
candidate_list = valid_spend(candidate_list)
candidate_list = centurion_spend(candidate_list)
show_client_list_names(candidate_list)
