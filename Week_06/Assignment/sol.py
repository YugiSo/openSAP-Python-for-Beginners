# Week 6 - Assignment

import requests


def getData(artist: str) -> dict:
    URL = 'https://itunes.apple.com/search?term=' + artist + '&entity=album'

    resp = requests.get(URL)
    resp = resp.json()

    return resp


def showData(data: dict) -> None:
    count = data['resultCount']
    print(f'The search returned {count} results.')

    keys = ['artistName', 'collectionName', 'trackCount']
    albums = data['results']

    for alb in albums:
        artist, albumName, trackCount = (alb[key] for key in keys)
        print(f'Artist: {artist} - Album: {albumName} - Track Count: {trackCount}')


srch = input('Please enter a search term: ')
data = getData(srch)

showData(data)