# geddit
---
This program backs up a Reddit user's saved posts locally. It currently emphasizes saving media content, but the ability to download more saved content types will be implemented in the near future.

## Features
* Back up your ***entire saved history (>1000 items)*** from a .csv file provided by Reddit
* Download saved text posts and media content (gifs, videos, albums) from a variety of sources
* Store a record of all saved and unsaved posts locally, skipping already-saved posts in subsequent program executions

## Preparing the config files
1. [Create an app on Reddit](https://www.reddit.com/prefs/apps) to obtain an API client ID and secret.
    - Set the name to whatever you want, e.g. `geddit`
    - Set `script` as the API type
    - Set the redirect URI to `http://localhost:8080`
2. [Obtain an Imgur API key](https://api.imgur.com/oauth2/addclient) to facilitate downloading Imgur albums.
    - Set the name to `geddit`
    - Set `Anonymous usage without user authorization` as the authorization type
    - Set the email and description fields accordingly
3. Rename the `user_template.json` file to `user.json`, and fill in its fields with their corresponding API information.

## Downloading all saved posts
1. [Request your Reddit data](https://www.reddit.com/settings/data-request) as a zip file.
2. Move the `saved_posts.csv` within the zip file into the home directory of the repository.
3. When starting the Docker environment or running the Python program, append `--csv` to the command.

## Usage (Docker)
1. Clone the repository.
2. Navigate into the cloned repository and build an image from the Dockerfile.

    ```
    docker build --tag geddit .
    ```

3. Start a container from the built image. Replace `$(pwd)` with `%cd%` on Windows.

    ```
    docker container run --network host -it -v $(pwd)/data:/geddit/data geddit [--csv]

    docker container run --network host -it -v %cd%/data:/geddit/data geddit [--csv]
    ```

## Usage (Python)
1. Clone the repository into a virtual environment.
2. Install the required Python packages.

    ```
    pip install -r requirements.txt
    ```

3. [Download ffmpeg](https://ffmpeg.org/download.html) for the video downloader.
4. Run the program.

    ```
    python3 -m geddit [--csv]
    ```

## To Do
- [x] Implement post ~~and comment~~ downloading
- [ ] Incoporate wayback machine API calls for deleted media
- [ ] Add multithreading
- [ ] Add progress bar with tqdm
- [ ] Add bloom filter to determine whether post is already saved, improve seek time
