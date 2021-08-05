def email_alert(action_config, event, state):
    for c in action_config['contacts']:
        print(f'Email alert sent to {c}')


def send_touchpoint_4(action_config, event, state):
    print(f'Schedule email to be sent to account_id={event["account_id"]}')


def send_touchpoint_5(action_config, event, state):
    print(f'Email sent to account_id={event["account_id"]}')