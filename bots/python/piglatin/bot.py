#!/usr/bin/env python

import argparse
import sys

import handler


def main():
    """Main function."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--token", help="path to Telegram API Token", required=True)

    args = parser.parse_args()

    with open(args.token, "r") as f:
        bot_handler = handler.Handler(f.readline())

    bot_handler.run()

if __name__ == "__main__":
    try:
        main()
    except Exception, e:
        sys.exit("Error: {0}".format(e))
