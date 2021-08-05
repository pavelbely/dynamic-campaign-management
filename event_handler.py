from collections import defaultdict
from functools import reduce

import actions as act_func
from db import save_event
from rule_checker import check_rule
from utils import create_reducer, get_with_generic


def handle_event(event, state, config, dry_run=False):
    '''
    Handle campaign event

        Parameters:
            event: campaign event
            state: previous events grouped by campaign and account
            config: campaign config
            dry_run: flag to disable performing actions, used for hydrating state after server restart as per event sourcing paradigm
    '''
    campaign_id = event['campaign_id']
    account_id = event['account_id']
    event_type = event['event_type']
    accounts = get_with_generic(config, campaign_id)
    event_types = get_with_generic(accounts, account_id)
    action_candidates = get_with_generic(event_types, event_type)

    account_state = state[campaign_id][account_id]
    if account_state.get('stopped'):
        return

    events = account_state['events']
    events.append(event)
    agg_events = reduce(create_reducer('event_type'), events, defaultdict(list))
    actions = [
        a
        for a in action_candidates
        if check_rule(event, a, agg_events)
    ]

    for a in actions:
        if a.get('stop'):
            account_state['stopped'] = True
        if not dry_run:
            getattr(act_func, a['action'])(a, event, account_state)
    if not dry_run:
        save_event(event)