
{
    "id": "A",
    "touchpoints": [
        {
            "id": "1",
            "channel": "email",
            "action": "send",
            "content": "Hi {first_name},\n\nI noticed that in {company_name} you have {number_of_open_positions} open positions,..."
        },
        {
            "id": "2",
            "channel": "linkedin",
            "action": "connect"
        },
        {
            "id": "3",
            "channel": "email",
            "action": "send",
            "content": "Hi {first_name},\n\nWe’re performing a  <a href=\"{url}\">short survey</a> of trends in HR in US companies and would appreciate your..."
        },
        {
            "id": "4",
            "channel": "email",
            "action": "send",
            "content": "Hi,\n\nI noticed you read the case study I sent - would be happy to elaborate more on a quick call - do you have any open slot in {next_business_day}..."
        },
        {
            "id": "5",
            "channel": "channel",
            "action": "message",
            "content": "Hi {first_name},\n\nNice to e-meet...."
        }
    ],
    "steps": [
        [
            {
                "touchpoint": "1",
                "percentage": 0.5,
            },
            {
                "touchpoint": "2",
                "delay": "3d",
            },
            {
                "touchpoint": "3",
                "delay": "3d",
            }
        ],
        [
            {
                "touchpoint": "3",
                "percentage": 0.5,
            },
            {
                "touchpoint": "2",
                "delay": "3d",
            },
            {
                "touchpoint": "1",
                "delay": "3d",
            }
        ],
    ],
    "actions": [
        { "account" : "*", "touchpoint": "2", "event_type" : "approve", "action" : "send_touchpoint_5", "delay": "1h"},
        { "account" : "*", "touchpoint": "3", "event_type" : "click", "action" : "send_thanks_gift_card"},
        { "account" : "*", "touchpoint": "1", "event_type" : "click", "action" : "send_touchpoint_4", "delay": "1d"},
        { "account" : "*", "touchpoint": "1", "event_type" : "doc_read", "rule": "duration()>60s", "action" : "email_alert", "contacts" : ["sdr@b.com"]},
        { "account" : "*", "event_type" : "reply", "action" : "email_alert", "contacts" : ["sdr@b.com"], "stop": true},
        { "account" : "*", "event_type" : ["open", "click"], "rule": "count()>3", "action" : "email_alert", "contacts" : ["sdr@b.com"]}
    ],
    "accounts": ["sergeyBrinId", "larryPageId", ...<other accounts ids>...],
    "schedule": {
        "startAt",
        "endAt",
    },
    "status": "in_progress" # "scheduled", "finished", "paused",
    "customFields": [
        {
            "amazonGiftCardsU": ,
            "caseStudyTech": "case_study_tech_url",
            ...
        }
    ]
}