import json
import streamlit as st
from google.cloud import storage
from datetime import datetime

project_id = st.secrets["project_id"]
bucket_name = st.secrets["bucket_name"]

storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)

st.title("Upload Tweet to Cloud Storage")

entity = st.text_input("Entity")
tweet_text = st.text_area("Tweet Text")

if st.button("Upload Tweet"):
    tweet = {"entity": entity, "text": tweet_text}
    tweet_json = json.dumps(tweet)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{entity.lower().replace(' ', '_')}_{timestamp}_tweet.json"
    blob = bucket.blob(filename)
    blob.upload_from_string(tweet_json)
    st.success(f"Tweet uploaded successfully to {filename}")


