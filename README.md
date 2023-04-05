# geddit
---
This program backs up a Reddit user's saved posts locally. It currently emphasizes saving media content, but the ability to download more saved content types will be implemented in the near future.

**It is now also able to download the user's <ins>entire saved post list (> 1000 items)</ins>. See below for details. Keep in mind that multiprocessing has not yet been implemented, so it will be somewhat inefficient when downloading many files, especially large Imgur albums.**

Posts that have already been downloaded will be skipped in subsequent executions of the program. A record of saved and unsaved posts will be serialized and stored in the data directory as JSON files.

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

## Usage (Docker)
1. Clone the repository.
2. Navigate into the cloned repository and build an image from the Dockerfile.

    ```
    docker build --tag geddit .
    ```

3. Start a container from the built image. Replace `$(pwd)` with `%cd%` on Windows.

    ```
    docker container run --network host -it -v $(pwd)/data:/geddit/data geddit

    docker container run --network host -it -v %cd%/data:/geddit/data geddit
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
    python3 -m main.py
    ```

## To Do
- [ ] Implement post and comment downloading
- [ ] Implement multithreading
- [ ] Implement progress bar with tqdm
- [ ] Implement bloom filter to determine whether post is already saved, improve seek time

- [ ] Investigate why Docker environment forces Requests to use IPv6 by default, leading to some weird hanging issues
