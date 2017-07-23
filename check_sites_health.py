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
    q = whois.whois(domain_name)
    if not q.expiration_date:
        return None
    if type(q.expiration_date) == list:
        expiration_date = q.expiration_date[0]
    else:
        expiration_date = q.expiration_date
    if (expiration_date - datetime.now()).days <= days_in_month:
        return False, expiration_date
    return True, expiration_date


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="Path to file with URLs")
    return parser.parse_args()


def get_formated_test_results(urls):
    test_results = ["{} | {} | {}".format(
                    url, "Good. Server is responding 200." if is_server_respond_with_200(url) else "!SOMETHING WRONG!",
                    "Domain extended enough." if is_domain_extended_enough(url) else "!DOMAIN DOESN'T EXTENDED ENOUGH!")
                    for url in urls]
    return test_results

if __name__ == '__main__':
    args = arg_parser()
    filepath = args.filepath
    urls = load_urls4check(filepath)
    if urls:
        test_results = get_formated_test_results(urls)
        print(*test_results , sep="\n")
