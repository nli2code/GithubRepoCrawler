# GithubRepoCrawler
Python2 scripts to download github repositories with a given query.

## Run
1. Config `config.json`, provide your: (a)query, (b)github id, (c) github password. Remember NOT to upload this file, add it to your .gitigonre.
2. Run `url_crawler.py` to get all related repository urls, the result is stored in `urlList.json`
3. Run `repo_downloader.py` to download all repositories, the result is stored in `repo` directory under script path.