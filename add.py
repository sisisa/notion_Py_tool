import requests
import datetime
import pytz

today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
date = format(today, '%Y-%m-%d')

headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer " + NOTION_API_KEY
}

url = 'https://api.notion.com/v1/pages'

# データ追加
data = {
    "parent": {
        "database_id": DATABASE_ID
    },
    "properties": {
    "Name": {
        "title": [
        {
            "text": {
                "content": date
            }
        }
        ],
    },
    "日付": {
        "date": {
            "start": date
            }
        },
    },
}
response = requests.post(url, headers=headers, json=data)
