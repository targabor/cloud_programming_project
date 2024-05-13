import pandas as pd
import time 
from google.cloud import storage
import json
from datetime import datetime 

storage_client = storage.Client(project="cloud-programming")
bucket = storage_client.bucket("h8mc7c-twitter-post-bucket")

data = pd.read_csv("twitter_validation.csv")
for row in data.values:
    tweet = {"entity": row[1], "text": row[3]}
    tweet_json = json.dumps(tweet)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{row[1].lower().replace(' ', '_')}_{timestamp}_tweet.json"
    blob = bucket.blob(filename)
    blob.upload_from_string(tweet_json)
    print(f"{filename} uploaded")
    time.sleep(1)