import os

import requests
import yaml
import tidalapi
from pathlib import Path

def tidal_login():
    session_file1 = Path("tidal-session-oauthn.json")

    session = tidalapi.session.Session()

    # Load session from file; create a new OAuth session if necessary
    session.login_session_file(session_file1)

    return session

def download_folder(album, folder="albums"):
    os.makedirs(folder, exist_ok=True)

    image_id = album.cover

    if not image_id:
        return None
    
    image_id = image_id.replace('-', '/')

    url = f"https://resources.tidal.com/images/{image_id}/1280x1280.jpg"
    resp = requests.get(url)

    filename = f"{album.id}.jpg"
    path = os.path.join(folder, filename)

    with open(path, "wb") as f:
        f.write(resp.content)

    return filename

def export_metadata(albums, filename='_data/albums.yml'):
    data = []
    
    for album in albums:
        # year = None

        # if album.release_date:
        #     year = album.release_date[:4]

        data.append({
            "id": album.id,
            "title": album.name,
            "artist": album.artist.name,
            "year": album.year,
            "cover": f"{album.id}.jpg",
            "link": album.listen_url,
            # "artists": album.artists,
            # "tracks":albums.tracks(limit=100, offset=1),
            "duration": f"{int(album.duration // 60)}",
            "copyright": album.copyright

        })

    with open(filename, 'w') as f:
        yaml.dump(data, f, sort_keys=False)

def main():
    session = tidal_login()
    albums = session.user.favorites.albums()

    export_metadata(albums)

    for album in albums:
        ...
        # print("Downloading:", album.artist.name, "-", album.name)
        # download_folder(album)


if __name__ == "__main__":
    main()
