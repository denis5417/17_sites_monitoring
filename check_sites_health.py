import argparse
import os
import requests
import whois
from datetime import datetime


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path) as f_urls:
        urls = f_urls.read().strip().split()
    return urls


def is_server_respond_with_200(url):
    try:
        return requests.get(url).status_code == 200
    except requests.exceptions.ConnectionError:
        return None
    except requests.exceptions.TooManyRedirects:
        return None


def is_domain_extended_enough(domain_name):
    days_in_month = 30
    query = whois.whois(domain_name)
    if not query.expiration_date:
        return None
    if type(query.expiration_date) == list:
        expiration_date = query.expiration_date[0]
    else:
        expiration_date = query.expiration_date
    if (expiration_date - datetime.now()).days <= days_in_month:
        return False
    return True


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="Path to file with URLs")
    return parser.parse_args()


def get_test_results(urls):
    formatted_server_respond_domain_extend = ["{} | {} | {}".format(
                    url, "Good. Server is responding 200." if is_server_respond_with_200(url) else "!SOMETHING WRONG!",
                    "Domain extended enough." if is_domain_extended_enough(url) else "!DOMAIN DOESN'T EXTENDED ENOUGH!")
                    for url in urls]
    return formatted_server_respond_domain_extend

if __name__ == '__main__':
    args = arg_parser()
    urls = load_urls4check(args.filepath)
    if urls:
        test_results = get_test_results(urls)
        print(*test_results , sep="\n")
    else:
        print("Файла не существует")
