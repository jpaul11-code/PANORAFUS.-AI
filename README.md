# PANORAFUS.AI

PANORAFUS.AI is a starter codebase for building AI-assisted panorama fusion workflows.
This repository is currently in bootstrap mode with a clean Python project layout,
a CLI entrypoint, and a roadmap for upcoming features.

## Vision

PANORAFUS.AI aims to combine classic panorama stitching with AI-driven scene
understanding and enhancement.

Core goals:

- Robust image alignment and blending for multi-shot panoramas.
- AI-guided quality improvements (exposure balancing, seam optimization).
- A practical CLI and service-ready architecture for future deployment.

## Quick Start

### 1) Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install in editable mode

```bash
pip install -e .
```

### 3) Run the CLI

```bash
panorafus-ai info
```

You should see:

```text
PANORAFUS.AI v0.1.0
Status: bootstrap complete
```

To view the community growth outreach strategy:

```bash
panorafus-ai engagement-strategy
```

## Project Structure

```text
.
|-- README.md
|-- pyproject.toml
`-- src/
	`-- panorafus_ai/
		|-- __init__.py
		`-- cli.py
```

## Development Roadmap

1. Add image ingestion and metadata validation.
2. Implement feature matching and homography estimation.
3. Add seam finding and multi-band blending.
4. Add optional AI enhancement modules.
5. Ship tests, benchmarks, and containerized deployment.

## Status

Current milestone: `Bootstrap`

- [x] Python package layout
- [x] CLI entrypoint
- [ ] Panorama fusion pipeline
- [ ] AI enhancement stack
- [ ] Automated test suite

## Engagement Strategy Command

Use `panorafus-ai engagement-strategy` to print a structured growth plan that
covers:

- Target groups (readers, visitors, subscribers, participants, vendors)
- Tailored encouragement focus for each group
- Outreach channels
- Participation funnel
- Core engagement metrics
- Monthly review cycle