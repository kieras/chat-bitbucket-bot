import json


def handle_bitbucket_event(event, headers):
    event_key = headers.get('X-Event-Key')
    if 'pullrequest:' in event_key:
        response = handle_pull_request(event, headers)
    elif 'repo:commit_status_' in event_key:
        response = handle_commit_status(event, headers)
    else:
        response = handle_unknown(event, headers)

    return json.dumps(response, indent=2)


def handle_pull_request(event, headers):
    pr_id = event.get('pullrequest').get('id')
    pr_title = event.get('pullrequest').get('title')
    pr_link = event.get('pullrequest').get('links').get('html').get('href')
    pr_state = event.get('pullrequest').get('state')
    pr_actor = event.get('actor').get('display_name')
    pr_source_branch = event.get('pullrequest').get('source').get('branch').get('name')
    pr_destination_branch = event.get('pullrequest').get('destination').get('branch').get('name')

    text = '<{}|PR#{} {}> from `{}` to `{}`\n*{}* by _{}_.'.format(
        pr_link, pr_id, pr_title, pr_source_branch, pr_destination_branch, pr_state, pr_actor)

    response = {
        'text': text
    }

    return response


def handle_commit_status(event, headers):
    cs_name = event.get('commit_status').get('name')
    cs_state = event.get('commit_status').get('state')
    cs_link = event.get('commit_status').get('url')

    text = '<{}|{}> is *{}*.'.format(cs_link, cs_name, cs_state)

    response = {
        'text': text
    }

    return response


def handle_unknown(event, headers):
    response = {
        'text': 'I\'ve received an event that I don\'t know how to handle.'
    }
    return response
