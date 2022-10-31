# Event API Script

import requests

api_key = "67bd3054f69a3246128e93cd05645468"

# Setting header type for api calls
header = {
    'content-type': 'application/json',
    'api-key': api_key
}

# Post the address information to the correlating event in api

def create_event():
    post_url = "https://api-event-dev.inviol.com/api/v1/events"
    params = {
        "address": [
            {
                "city": "Auckland",
                "country": "New Zealand",
                "name": "Wellesley Street East",
                "postcode": 1010,
                "street_number": 55,
                "suburb": "Auckland City"
            }
        ],
        "confidence": 93.5,
        "device_id": "20d08b4e-c688-4ddb-b307-ec2e74b6a2ad",
        "event_time": "2022-9-28T20:43:56.390Z",
        "latitude": -36.8509,
        "longitude": 174.7645,
        "policy_id": "9b7d0d25-dedd-41f2-b86b-5a08e1dd1d50",
        "type": "edge",
    }

    response = requests.post(post_url, headers=header, json=params)
    get_id = response.json()
    event_id = get_id['id']

    post_video_url = "https://api-event-dev.inviol.com/api/v1/videos"
    params = {
        "bbox_video_uri": "",
        "camera_id": "123e4567-e89b-12d3-a456-426614174001",
        "event_id": "{}".format(event_id),
        "inference_uri": "",
        "original_video_uri": "https://steventdatadev001.blob.core.windows.net/events/vulcan/{}/out_0.mp4".format(event_id)
    }
    response = requests.post(post_video_url, headers=header, json=params)

    return event_id

# Pass in event_id to read blobs in storage
def put_event_bounding_box(event_id):
    post_video_url = "https://api-event-dev.inviol.com/api/v1/videos"
    params = {
        "bbox_video_uri": "https://steventdatadev001.blob.core.windows.net/events/vulcan/{}/out_bb_0.mp4".format(event_id),
        "camera_id": "123e4567-e89b-12d3-a456-426614174001",
        "event_id": "{}".format(event_id),
        "inference_uri": "",
        "original_video_uri": "https://steventdatadev001.blob.core.windows.net/events/vulcan/{}/out_0.mp4".format(event_id)
    }

    response = requests.post(post_video_url, headers=header, json=params)
    print(response)
