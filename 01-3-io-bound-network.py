import requests

proxies = {
    "http": "",
    "https": "",
}


def io_bound_func():
    response = requests.get("https://google.com", proxies=proxies)

    # print(response.get(url))
    return response


if __name__ == "__main__":

    result = io_bound_func()

    print(result)
