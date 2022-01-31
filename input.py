# Probabilities:
alarm_was_set = {
    'depends_on': [],
    'probabilities': 0.85
}
put_on_charge = {
    'depends_on': [],
    'probabilities': 0.7
}
# dependent
phone_turned_off = {
    'depends_on': ['put_on_charge'],
    'probabilities': {
        '1': 0.02,
        '0': 0.77
    }
}

alarm_went_off = {
    'depends_on': ['alarm_was_set', 'phone_turned_off'],
    'probabilities': {
        '00': 0.001,
        '01': 0,
        '10': 0.99,
        '11': 0
    }
}

oversleep = {
    'depends_on': ['alarm_went_off'],
    'probabilities': {
        '1': 0.05,
        '0': 0.86
    }
}

bayesian_network = {
    'oversleep': oversleep,
    'alarm_went_off': alarm_went_off,
    'phone_turned_off': phone_turned_off,
    'put_on_charge': put_on_charge,
    'alarm_was_set': alarm_was_set
}


def is_independent(node) -> bool:
    return not node['depends_on']
