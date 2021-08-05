from utils import wrap_list

def rule_interpolator(event, all_events, rule_config):
    # HACK Since rules interpolator is out of scope of this assignment
    # we use the simplest hack to make it work
    return eval(f'all_events.{rule_config["rule"].replace("count", "__len__")}')


def check_rule(event, rule_config, agg_events):
    event_touchpoint = event.get('data').get('touchpoint')
    rule_touchpoint = rule_config.get('touchpoint')
    event_step = event.get('step_id')
    rule_step = rule_config.get('step_id')
    if (
        (rule_touchpoint and event_touchpoint != rule_touchpoint)
        or (rule_step and event_step != rule_step)
    ):
        return False

    if 'rule' not in rule_config:
        return True    
    all_matching_events = [
        e
        for et in wrap_list(rule_config['event_type'])
        for e in agg_events[et]
    ]
    res = rule_interpolator(event, all_matching_events, rule_config)
    return res
