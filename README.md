# Google Hangout Chats Bitbucket Bot

It is a Google Hangout Chats Bitbucket Bot. :-)

## Run unit tests

```bash
pipenv run python -m pytest --junitxml=test-results/pytest/report.xml -vvs tests --log-cli-level WARNING
```

## Deploy

```bash
gcloud functions deploy chat-bitbucket-bot --entry-point main --runtime python37 --trigger-http --project <YOUR_PROJECT_ID>
```
