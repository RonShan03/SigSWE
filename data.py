from auth import get_auth


def get_data():
def get_data(artist_id):
    '''This function gets the data from the Spotify API.'''
    access_token = get_auth()
    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)
    }

    URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id='6M2wZ9GZgrQXHCFfjv46we')
    URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=artist_id)
    data = requests.get(URL + "?market=US", headers = headers)

    data = data.json()

    #rand = random.randint(0, len(data['tracks']) - 1)
    rand = 2
    rand = random.randint(0, len(data['tracks']) - 1)

    artist_names = []
    for i in data["tracks"][rand]["artists"]: