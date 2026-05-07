import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="portfolio-tracker",
        description="Cryptocurrency portfolio tracker"
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--asset", required=True)
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--price", type=float, required=True)

    subparsers.add_parser("balance")
    subparsers.add_parser("value")

    return parser
