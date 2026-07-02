"""Tests for the PANORAFUS.AI CLI."""

from __future__ import annotations

import sys

from panorafus_ai import cli


def test_info_command_prints_bootstrap_details(capsys, monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["panorafus-ai", "info"])

    exit_code = cli.main()
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "PANORAFUS.AI v0.1.0" in output
    assert "Published network:" in output
    assert "Status: bootstrap complete" in output


def test_engagement_strategy_command_prints_sections(capsys, monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["panorafus-ai", "engagement-strategy"])

    exit_code = cli.main()
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "PANORA-FUS Engagement Strategy" in output
    assert "1) Target groups" in output
    assert "6) Review cycle" in output


def test_no_command_prints_help(capsys, monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["panorafus-ai"])

    exit_code = cli.main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "usage:" in captured.out.lower()
