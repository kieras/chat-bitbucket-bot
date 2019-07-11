import flask
import pytest
import json

from main import main


@pytest.fixture(scope="module")
def app():
    return flask.Flask(__name__)


def load_fixture(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def test_pull_request_created(app):

# X-Request-UUID	afe23a8c-dde6-4cde-8eaa-3e50077849f4
# X-Event-Key	pullrequest: created
# X-Event-Time	Wed, 10 Jul 2019 20: 23: 28 GMT
# X-Attempt-Number	1
# X-Hook-UUID	fee8a257-2939-4b3a-aa64-2e07be1a8fb8
# User-Agent	Bitbucket-Webhooks/2.0
# Content-Type	application/json

    data = load_fixture('./tests/fixtures/pullrequest-created.json')
    with app.test_request_context(method='POST', json=data):
        res = main(flask.request)
        assert 'pullrequest' in res


def test_pull_request_fulfilled(app):

# X-Request-UUID	a607b1c4-be59-4a27-83e5-208de2fa7e81
# X-Event-Key	pullrequest: fulfilled
# X-Event-Time	Wed, 10 Jul 2019 21: 41: 04 GMT
# X-Attempt-Number	1
# X-Hook-UUID	fee8a257-2939-4b3a-aa64-2e07be1a8fb8
# User-Agent	Bitbucket-Webhooks/2.0
# Content-Type	application/json

    data = load_fixture('./tests/fixtures/pullrequest-fulfilled.json')
    with app.test_request_context(method='POST', json=data):
        res = main(flask.request)
        assert 'pullrequest' in res


def test_pull_request_rejected(app):

# X-Request-UUID	a391cc1e-c057-4168-b5fd-2e52b911d5fd
# X-Event-Key	pullrequest: rejected
# X-Event-Time	Wed, 10 Jul 2019 20: 23: 44 GMT
# X-Attempt-Number	1
# X-Hook-UUID	fee8a257-2939-4b3a-aa64-2e07be1a8fb8
# User-Agent	Bitbucket-Webhooks/2.0
# Content-Type	application/json

    data = load_fixture('./tests/fixtures/pullrequest-rejected.json')
    with app.test_request_context(method='POST', json=data):
        res = main(flask.request)
        assert 'pullrequest' in res


def test_commit_status_updated_successful(app):

# X-Request-UUID	01e7f365-6430-4a79-bd5a-976acc8e228e
# X-Event-Key	repo: commit_status_updated
# X-Event-Time	Thu, 11 Jul 2019 15: 01: 11 GMT
# X-Attempt-Number	1
# X-Hook-UUID	fee8a257-2939-4b3a-aa64-2e07be1a8fb8
# User-Agent	Bitbucket-Webhooks/2.0
# Content-Type	application/json

    data = load_fixture('./tests/fixtures/commit-status-updated-successful.json')
    with app.test_request_context(method='POST', json=data):
        res = main(flask.request)
        assert 'SUCCESSFUL' in res


def test_commit_status_updated_failed(app):

# X-Request-UUID	1450daa7-5036-4b25-b24d-13fe76363b25
# X-Event-Key	repo: commit_status_updated
# X-Event-Time	Thu, 11 Jul 2019 14: 36:20 GMT
# X-Attempt-Number	1
# X-Hook-UUID	fee8a257-2939-4b3a-aa64-2e07be1a8fb8
# User-Agent	Bitbucket-Webhooks/2.0
# Content-Type	application/json

    data = load_fixture('./tests/fixtures/commit-status-updated-failed.json')
    with app.test_request_context(method='POST', json=data):
        res = main(flask.request)
        assert 'FAILED' in res
