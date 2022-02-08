import requests

perl_repositories = "https://api.github.com/search/repositories?q=language"\
    ":perl&sort=stars"


def run():
    print(perl_repositories)