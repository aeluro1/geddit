# geddit
---
This program backs up a Reddit user's saved posts locally. It currently emphasizes saving media content, but the ability to download more saved content types will be implemented in the near future.

## Features
* Back up your ***entire saved history (>1000 items)*** from a .csv file provided by Reddit
* Download saved text posts and media content (gifs, videos, albums) from a variety of sources
* Extract deleted media using pushshift, cached reddit previews, and the wayback machine
* Store a record of all saved and unsaved posts locally, skipping already-saved posts in subsequent program executions
* Utilize a graphical user interface (GUI) to navigate saved posts and fetch a custom list of download targets

## Preparing the config files
1. [Create an app on Reddit](https://www.reddit.com/prefs/apps) to obtain an API client ID and secret.
    - Set the name to whatever you want, e.g. `geddit`
    - Set `script` as the API type
    - Set the redirect URI to `http://localhost:8080`
2. [Obtain an Imgur API key](https://api.imgur.com/oauth2/addclient) to facilitate downloading Imgur albums.
    - Set the name to `geddit`
    - Set `Anonymous usage without user authorization` as the authorization type
    - Set the email and description fields accordingly
    - Repeat these steps to obtain several more API keys to circumvent Imgur's rate limit (12500 requests per API)
3. Rename the `user_template.json` file to `user.json`, and fill in its fields with their corresponding API information.

## Downloading all saved posts
1. [Request your Reddit data](https://www.reddit.com/settings/data-request) as a zip file.
2. Move the `saved_posts.csv` within the zip file into the home directory of the repository.
3. When starting the Docker environment or running the Python program, append `--csv` to the command.

## GUI (WIP)
Geddit comes with a QT6-based user interface for easier usage. This interface may be used to search through saved media based on a variety of search parameters or download a custom list of targets (posts, subreddits, etc.).

| Search page | Download page |
| :---: | :---: |
| ![Search page](https://github.com/aeluro1/geddit/assets/103622874/9ac0d840-34ce-4dc3-97c4-4b6d06b0f738) | ![Download page](https://github.com/aeluro1/geddit/assets/103622874/d273bf8b-fc9f-4c03-b289-d458922285de) |

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
- [x] Incoporate wayback machine API calls for deleted media
- [ ] Add multithreading
- [ ] Add progress bar with tqdm
- [ ] Add bloom filter to determine whether post is already saved, improve seek time
