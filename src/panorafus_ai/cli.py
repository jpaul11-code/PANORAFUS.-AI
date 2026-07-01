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

    strategy_parser = subparsers.add_parser(
        "engagement-strategy",
        help="Show the outreach strategy for PANORA-FUS community growth",
    )
    strategy_parser.set_defaults(command="engagement-strategy")

    return parser


def print_engagement_strategy() -> None:
    print("PANORA-FUS Engagement Strategy")
    print("")
    print("1) Target groups")
    print("   - Readers")
    print("   - Visitors")
    print("   - Subscribers")
    print("   - Participants")
    print("   - Vendors")
    print("")
    print("2) Tailored encouragement")
    print("   - Readers: Join the Eschatology reading journey.")
    print("   - Visitors: Discover value and start with one clear next step.")
    print("   - Subscribers: Receive ongoing updates and opportunities.")
    print("   - Participants: Engage in sessions and community discussion.")
    print("   - Vendors: Support events and connect with the audience.")
    print("")
    print("3) Engagement channels")
    print("   - Email")
    print("   - Social posts")
    print("   - Landing page")
    print("   - Events")
    print("   - Direct outreach")
    print("")
    print("4) Participation funnel")
    print("   awareness -> interest -> signup/subscription -> participation")
    print("")
    print("5) Key metrics")
    print("   - New readers")
    print("   - Visitor-to-subscriber conversion")
    print("   - Event participation")
    print("   - Vendor signups")
    print("")
    print("6) Review cycle")
    print("   - Review results monthly and refine messaging/channels.")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "info":
        print("PANORAFUS.AI v0.1.0")
        print("Status: bootstrap complete")
        return 0

    if args.command == "engagement-strategy":
        print_engagement_strategy()
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
