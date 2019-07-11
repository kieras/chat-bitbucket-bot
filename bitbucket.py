import json


def handle_bitbucket_event(request):
    event = request.get_json(silent=True)
    headers = request.headers

    event_key = headers.get('X-Event-Key')
    if 'pullrequest:' in event_key:
        return handle_pull_request(event, headers)
    elif 'repo: commit_status_' in event_key:
        return handle_commit_status(event, headers)
    else:
        return handle_unknown(event, headers)


def handle_pull_request(event, headers):
    return handle_unknown(event, headers)


def handle_commit_status(event, headers):
    return handle_unknown(event, headers)


def handle_unknown(event, headers):
    response = {
        'text': 'I know nothing about this kind of event.'
    }
    return json.dumps(response, indent=2)
