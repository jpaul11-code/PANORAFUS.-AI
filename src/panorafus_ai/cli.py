"""Command-line interface for PANORAFUS.AI."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="panorafus-ai",
        description="PANORAFUS.AI - vision-first panorama fusion toolkit",
    )
    subparsers = parser.add_subparsers(dest="command")

    info_parser = subparsers.add_parser("info", help="Show project information")
    info_parser.set_defaults(command="info")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "info":
        print("PANORAFUS.AI v0.1.0")
        print("Status: bootstrap complete")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
