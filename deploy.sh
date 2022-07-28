#!bin/bash
gcloud functions delete daily-ssc-acx  \
    --project=daily-ssc-acx  

gcloud functions deploy daily-ssc-acx  \
    --project=daily-ssc-acx  \
    --trigger-topic daily-ssc-acx  \
    --memory=1024MB \
    --env-vars-file .env.yaml \
    --region=us-central1 \
    --runtime python39 \
    --entry-point=post_tweet \
    --timeout=300