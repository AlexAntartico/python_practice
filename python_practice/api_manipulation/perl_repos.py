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

    print(f"Total repositories: {response_dict['total_count']}")

    # Explore information about the repositories
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")


if __name__ == '__main__':
    run()
