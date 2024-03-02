import requests


def create_facebook_post(page_id, access_token, message):
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'access_token': access_token,
        'message': message
    }

    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print("Post created successfully!")
        else:
            print("Error creating post:", response.json())
    except Exception as e:
        print("Exception:", e)


# Replace these with your own values
page_id = 'YOUR_PAGE_ID'
access_token = 'YOUR_ACCESS_TOKEN'
message = 'Hello from Python! This is an automatic post.'

create_facebook_post(page_id, access_token, message)
