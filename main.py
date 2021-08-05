from collections import defaultdict
from functools import reduce
import json

from datetime import datetime
from event_handler import handle_event
from utils import create_reducer


def aggregate_config(source):
    '''
        Example:

            { "account_id" : "account1", "campaign_id" : "A", "touchpoint": "2", "event_type" : "approve", "action" : "send_touchpoint_5", "delay": "1h"},
            { "account_id" : "*", "campaign_id" : "A", "touchpoint": "3", "event_type" : "click", "action" : "send_thanks_gift_card"},
            { "account_id" : "*", "campaign_id" : "B", "touchpoint": "3", "event_type" : "click", "action" : "send_thanks_gift_card"},

        -> 

        {
            'A': {
                'account1': [
                    { "account_id" : "account1", "campaign_id" : "A", "touchpoint": "2", "event_type" : "approve", "action" : "send_touchpoint_5", "delay": "1h"},
                ],
                '*': [
                    { "account_id" : "*", "campaign_id" : "A", "touchpoint": "3", "event_type" : "click", "action" : "send_thanks_gift_card"},
                ],
            },
            'B': {
                '*': [
                    { "account_id" : "*", "campaign_id" : "B", "touchpoint": "3", "event_type" : "click", "action" : "send_thanks_gift_card"},
                ]
            }
        }

    '''          
    grouped_by_campaign = reduce(create_reducer('campaign_id'), source, defaultdict(list))
    for campaign_id in grouped_by_campaign:
        grouped_by_account = reduce(create_reducer('account_id'), grouped_by_campaign[campaign_id], defaultdict(list))
        grouped_by_campaign[campaign_id] = grouped_by_account
        for account_id in grouped_by_account:
            grouped_by_event_type = reduce(create_reducer('event_type'), grouped_by_account[account_id], defaultdict(list))
            grouped_by_account[account_id] = grouped_by_event_type
    res = grouped_by_campaign
    return res


config_file = open('config.json')
raw_config = json.load(config_file)
raw_actions_config = raw_config["actions"]
actions_config = aggregate_config(raw_actions_config)
state = defaultdict(lambda : defaultdict(lambda : {'events': []}))

events = [
    {
        'account_id': 'a',
        'campaign_id': 'A',
        'contact_id': 'c001',
        'step_id': '1',
        'channel': 'email',
        'event_type': 'open',
        'data': {
            'touchpoint': '1',
        },
        'createdAt': datetime.now(),
    },
    {
        'account_id': 'sergeyBrin1',
        'campaign_id': 'A',
        'contact_id': 'c001',
        'step_id': '1',
        'channel': 'email',
        'event_type': 'open',
        'data': {
            'touchpoint': '1',
        },
        'createdAt': datetime.now(),
    },
    {
        'account_id': 'sergeyBrin1',
        'campaign_id': 'A',
        'contact_id': 'c001',
        'step_id': '1',
        'channel': 'email',
        'event_type': 'open',
        'data': {
            'touchpoint': '1',
        },
        'createdAt': datetime.now(),
    },
    {
        'account_id': 'sergeyBrin1',
        'campaign_id': 'A',
        'contact_id': 'c001',
        'step_id': '1',
        'channel': 'email',
        'event_type': 'click',
        'data': {
            'touchpoint': '1',
        },
        'createdAt': datetime.now(),
    },
]

for e in events:
    handle_event(e, state, actions_config)
