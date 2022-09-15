#!/usr/bin/env python3

import requests
import click


def main():
    urlList()
    check()


@click.command()
@click.option("--url", prompt="url link", help="url to check.")
def urlList(url):
    """Adds the inputted url into a txt file if not already"""
    with open("urlList.txt", "r") as f:
        # if url exists in file
        if url not in f.read():
            f.close()
            with open("urlList.txt", "a") as f:
                f.write(url + "\n")
                f.close()
        else:
            print("url already in file")
            f.close()


@click.command()
@click.option("--count", default=3, help="Number of requests to make.")
def check(count):
    """Simple program that check the availability of a url for a number of times."""
    try:
        url_list = open("urlList.txt", "r")
        urls = url_list.split("\n")
        for url in urls:
            for x in range(count):
                # Get Url
                get = requests.get(url)
                click.echo(f"{url}!")
                # if the request succeeds
                if get.status_code == 200:
                    return f"{url}: is reachable"
                else:
                    return f"{url}: is Not reachable, status_code: {get.status_code}"

    # Exception
    except requests.exceptions.RequestException as e:
        # print URL with Errs
        raise SystemExit(f"{url}: is Not reachable \nErr: {e}")


if __name__ == "__main__":
    main()
