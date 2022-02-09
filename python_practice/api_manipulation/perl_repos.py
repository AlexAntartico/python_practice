import requests

# API url calls that show github repositories from perl and R languages,
# ordered by stars. Query will return most popular repos info.
perl_url = "https://api.github.com/search/repositories?q=language:perl"\
    "&sort=stars"
r_url = "https://api.github.com/search/repositories?q=language:r&sort=stars"

def menu():
    """
    Interactive menu to navigate through options.
    You can query Perl or R repositories in github
    Any call to this method will return a url value stored at 
    perl_url or r_rul attributes
    """
    options = """
    Please type the number of your selection and press enter:
    1 to query perl repos
    2 to query r repos
    """
    menu = int(input(f"{options}\n"))
    if menu == 1:
        url = perl_url
    else:
        url = r_url
    return url


def run():
    url = menu()
    # header for API call that asks for use of v3
    headers = {"Accept": "application/vnd.github.v3+json"}
    # call requests.get and pass url value and header we defined
    r = requests.get(url, headers=headers)
    # print status code to ensure request was successful
    print(f"Status code: {r.status_code}")
    # store resulting dictionary in var response_dict
    response_dict = r.json()
    # process results
    print(response_dict.keys())

    # printing total_count which represents total number of GH repos
    print(f"Total repositories: {response_dict['total_count']}")

    # Explore information about the repositories
    # store dictionary list into repo_dicts
    repo_dicts = response_dict['items']
    # print lenght of dict list to know # of repos returned
    print(f"Repositories returned: {len(repo_dicts)}")

    # explore the first repository
    # to take a closer look at information returned about each repository, we
    # pull out the first item from repo_dicts and store it in repo_dict
    repo_dict = repo_dicts[0]
    # we then print the # of keys in the dict to see how much info we have
    print(f"\nKeys: {len(repo_dict)}\n")
    # print all dictionary keys to see what kind of info we have.
    for key in sorted(repo_dict):
        print(key)

if __name__ == '__main__':
    run()
