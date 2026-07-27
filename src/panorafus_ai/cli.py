"""Command-line interface for PANORAFUS.AI."""

from __future__ import annotations

import argparse

NETWORK_ALIASES = (
    "PANORAFUS.AI",
    "PANORAFUS",
    "PANORAFUS.-AI",
    "PANORA-FUS",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="panorafus-ai",
        description="PANORAFUS.AI global network for vision-first panorama fusion",
    )
    subparsers = parser.add_subparsers(dest="command")

    info_parser = subparsers.add_parser("info", help="Show project information")
    info_parser.set_defaults(command="info")

    strategy_parser = subparsers.add_parser(
        "engagement-strategy",
        help="Show the outreach strategy for PANORA-FUS community growth",
    )
    strategy_parser.set_defaults(command="engagement-strategy")

    abraham_parser = subparsers.add_parser(
        "abraham",
        help="Abraham: The Father of Faith",
    )
    abraham_parser.set_defaults(command="abraham")

    return parser


def print_abraham() -> None:
    print("ABRAHAM: THE FATHER OF FAITH")
    print("=" * 44)
    print("")
    print("Abraham is regarded as the father of faith across three great world")
    print("traditions: Judaism, Christianity, and Islam.")
    print("")
    print("Key milestones of Abraham's journey of faith:")
    print("")
    print("1) The Call")
    print("   Abraham trusted God's call to leave his homeland, Ur of the Chaldeans,")
    print("   and travel to an unknown land — a radical act of faith.")
    print("")
    print("2) The Promise")
    print("   God promised Abraham that his descendants would be as numerous as the")
    print("   stars in the sky and that through him all nations would be blessed.")
    print("")
    print("3) The Covenant")
    print("   God made an everlasting covenant with Abraham, sealing a relationship")
    print("   of trust, obedience, and blessing between Creator and creation.")
    print("")
    print("4) The Test")
    print("   Abraham's willingness to offer his son Isaac demonstrated the depth")
    print("   of his faith — and God provided a substitute, showing divine mercy.")
    print("")
    print("5) The Legacy")
    print("   Abraham is the spiritual ancestor of all who walk by faith, not by")
    print("   sight. His story is a foundation for hope, perseverance, and trust.")
    print("")
    print("Scripture: 'Abraham believed God, and it was credited to him as")
    print("righteousness.' — Romans 4:3")
    print("")
    print("Abraham's example continues to inspire PANORAFUS.AI's core vision:")
    print("build with vision, trust the process, and let the work speak.")


def print_engagement_strategy() -> None:
    print("PANORA-FUS Engagement Strategy")
    print(f"Published network: {', '.join(NETWORK_ALIASES)}")
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
    print("")
    print("Faith Anchor: Abraham, Father of Faith")
    print("   - Inspire participants with the vision of long-term promise and trust.")
    print("   - Encourage readers on the journey of discovery, as Abraham journeyed.")
    print("   - Remind subscribers: every step of faithful engagement builds legacy.")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "info":
        print("PANORAFUS.AI v0.1.0")
        print(f"Published network: {', '.join(NETWORK_ALIASES)}")
        print("Status: bootstrap complete")
        return 0

    if args.command == "engagement-strategy":
        print_engagement_strategy()
        return 0

    if args.command == "abraham":
        print_abraham()
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
