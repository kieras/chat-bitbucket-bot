# Google Hangout Chats Bitbucket Bot

It is a Google Hangout Chats Bitbucket Bot. :-)

## Setup virtual environment

```bash
pipenv install --ignore-pipfile --dev
```

## Run unit tests

```bash
pipenv run python -m pytest --junitxml=test-results/pytest/report.xml -vvs tests --log-cli-level WARNING
```

## Deploy

```bash
gcloud beta functions deploy chat-bitbucket-bot \
    --entry-point main \
    --runtime python37 \
    --memory 128MB \
    --timeout 5s \
    --max-instances 3 \
    --trigger-http \
    --allow-unauthenticated \
    --set-env-vars=CHAT_WEBHOOK_URL='<YOUR_CHAT_WEBHOOK_URL>' \
    --region=<YOUR_REGION> \
    --project <YOUR_PROJECT_ID>
```
