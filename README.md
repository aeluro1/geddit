# geddit
---
This program backs up a Reddit user's saved posts.

## Preparing the config files
1. [Create an app on Reddit](https://www.reddit.com/prefs/apps) to obtain an API client ID and secret key.
    - Set the name to whatever you want, e.g. `geddit`
    - Set 'script' as the API type
    - Set the redirect URI to `http://localhost:8080`
2. [Obtain an Imgur API key](https://api.imgur.com/oauth2/addclient) to facilitate downloading Imgur albums.
    - Set the name to `geddit`
    - Set 'Anonymous usage without user authorization' as the authorization type
    - Set the email and description fields accordingly
3. Rename the 'user_template.json' file to 'user.json', and fill in the fields with their corresponding API information.

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

3. [Download ffmpeg.](https://ffmpeg.org/download.html) for the video downloader.
4. Run the program.

    ```
    python3 -m main.py
    ```

## To Do
- [ ] Implement post and comment downloading
- [ ] Implement progress bar with tqdm
- [ ] Implement bloom filter to determine whether post is already saved, improve seek time

- [ ] Investigate why Docker environment forces Requests to use IPv6 by default, leading to some weird hanging issues