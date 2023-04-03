# Geddit
---
This program backs up a Reddit user's saved posts.


## Usage (Docker)
1. Clone the repository.
2. Frome the main directory, build an image from the Dockerfile.

    ```
    docker build --tag geddit .
    ```

3. Start a container from the built image. Replace `$(pwd)` with `%cd%` on Windows.

    ```
    docker container run -v $(pwd)/data:/geddit/data geddit

    docker container run -v %cd%/data:/geddit/data geddit
    ```

## To Do
- [ ] Implement bloom filter to determine whether post is already saved
- [ ] Modify code logic to use response content-type to determine download method for unknown sources
- [ ] Implement comment downloading
- [ ] Implement progress bar with tqdm
- [ ] Store data in database rather than JSON