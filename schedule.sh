#!bin/bash
# use create instead of update to create it for the first time
gcloud scheduler jobs update pubsub daily-ssc-acx  \
    --project=metaculus-alert \
    --schedule="0 10 * * *" \
    --location=us-central1 \
    --topic=metaculus-alert \
    --description="Run SSC bot" \
    --message-body="Run SSC bot" \
    --time-zone=GMT