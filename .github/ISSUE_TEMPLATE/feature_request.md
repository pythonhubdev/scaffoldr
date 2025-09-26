---
name: Feature Request
about: Suggest a new feature for the VoxLoom SDK (Python · adapters · pipeline · RTC)
title: "[FEATURE] "
labels: "enhancement, needs-triage"
assignees: ""

---

## Summary

Briefly describe the feature and who benefits.

## Problem Statement

What problem does this feature solve? Who is affected and how?

## Affected Area

- [ ] SDK core (orchestration / pipeline)
- [ ] Adapter – LLM
- [ ] Adapter – STT
- [ ] Adapter – TTS
- [ ] RTC / Streaming
- [ ] Metrics / Instrumentation
- [ ] Configuration / Env vars
- [ ] Developer tooling / CI
- [ ] Examples / Docs
- [ ] Other (specify below)

## Proposed Solution

High-level approach and rationale. Mention alternatives considered.

## Public API Impact (Python SDK)

- New modules/classes/functions:
- Changed/removed APIs:
- Deprecations (timeline and migration path):
- Docstrings/type hints updated: yes | no

## Config / Env Changes

- New env vars (names only):
- Defaults and validation rules:
- Backward-compatible: yes | no

## Data / Contracts

- Schemas/payloads affected (if any):
- Backward compatibility considerations:

## Observability

- Logging: fields and levels to add
- Metrics: counters/histograms/gauges (e.g., stt, llm, tts, overall)
- Traces: spans of interest

## Performance Targets

- Latency targets (P50/P95) per component (STT/LLM/TTS):
- Throughput/concurrency:
- Resource constraints: CPU/memory/network

## Security

- Secrets/keys involved: list if applicable
- Permissions/model access changes:
- Input validation considerations:

## Testing Plan

- Unit tests (pytest): what to cover
- Integration tests (end-to-end pipeline): scenarios
- Edge cases: timeouts, retries, model unavailability, interruptions
- Commands to run locally:
  - [ ] task test
  - [ ] task lint

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Risks / Rollout

- Risks and mitigations:
- Feature flag or config toggle:
- Rollout plan and rollback strategy:

## Documentation

- [ ] README updates
- [ ] guides/setup.md
- [ ] guides/tasks.md
- [ ] Notes:

## Dependencies

- External services/adapters:
- Related issues/PRs:

## Out of Scope

What isn’t included in this feature.

## Additional Context

Links, prior art, design notes, and diagrams.
