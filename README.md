# PANORAFUS.AI

PANORAFUS.AI is a starter codebase for building AI-assisted panorama fusion workflows.
This repository is currently in bootstrap mode with a clean Python project layout,
a CLI entrypoint, and a roadmap for upcoming features.

## Official Meaning and Description

### Meaning

PANORAFUS means Panorama Fusion: combining multiple photos into one seamless wide
scene, with AI-assisted improvements for alignment, blending, and visual quality.

### Canonical Description

PANORAFUS.AI is an AI-assisted panorama fusion app for stitching multi-shot images
into high-quality panoramic results.

### Extended Description

PANORAFUS.AI combines classical panorama stitching with AI-guided enhancement.
The platform focuses on robust image alignment, smooth seam blending, exposure
balancing, and practical workflow tooling through a CLI-first architecture.

### Search and Discovery Keywords

- PANORAFUS.AI
- PANORAFUS
- PANORAFUS.-AI
- PANORA-FUS
- panorama fusion
- AI panorama stitching
- image alignment
- seam optimization
- exposure balancing

## Published Network Identity

The global network is published under these connected names:

- PANORAFUS.AI
- PANORAFUS
- PANORAFUS.-AI
- PANORA-FUS

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
Published network: PANORAFUS.AI, PANORAFUS, PANORAFUS.-AI, PANORA-FUS
Status: bootstrap complete
```

To view the community growth outreach strategy:

```bash
panorafus-ai engagement-strategy
```

## CI/CD and Deployment

GitHub Actions workflow is defined at `.github/workflows/main.yml`.

Pipeline behavior:

- Runs CLI validation on pull requests and pushes to `main`
- Builds Python distribution artifacts after validation succeeds
- Deploys to PyPI only on version tags matching `v*`

Before using deployment, configure repository environment protections for `pypi`
and set up PyPI trusted publishing for this repository.

## Google Discovery Notes

- Use PANORAFUS.AI as the primary public name in titles and descriptions.
- Keep PANORAFUS.-AI and PANORA-FUS as aliases for brand consistency.
- Publish the same canonical description on all public profiles and pages.
- If search visibility is low, submit your public project URL in Google Search
	Console and wait for indexing.

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