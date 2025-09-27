---
name: Bug Report
about: Report a bug in the VoxLoom SDK (Python · adapters · pipeline · RTC)
title: '[BUG] '
labels: 'bug, needs-triage'
assignees: ''

---

## Summary

Briefly describe the issue.

## Affected Area

- [ ] SDK core (orchestration / pipeline)
- [ ] Adapter – LLM
- [ ] Adapter – STT
- [ ] Adapter – TTS
- [ ] RTC / Streaming
- [ ] Metrics / Instrumentation
- [ ] Configuration / Env vars
- [ ] Developer tooling
- [ ] Examples / Docs
- [ ] Other (specify below)

## Environment

- Commit SHA / Branch: e.g., 1a2b3c4 / feature/x
- vox-sdk version (tag if any): e.g., 1.3.0
- Python: e.g., 3.12.4
- OS: e.g., macOS 14.5, Ubuntu 22.04, Windows 11
- uv version: output of `uv --version`
- Task version: output of `task --version`
- Environment: local dev | CI | other
- Hardware (if relevant): CPU/GPU model, RAM
- Key deps (if relevant): torch, transformers, kokoro, ollama, openai, huggingface-hub
- Env vars (redact secrets):
	- OPEN_ROUTER_API_KEY (redacted)
	- HUGGINGFACE_API_KEY (redacted)
	- WHISPER_MODEL_SIZE (e.g., base)
	- DEFAULT_LLM_MODEL (e.g., openchat/openchat-3.5)
	- DEFAULT_VOICE_ID (e.g., en_US-lessac-medium)

## Steps to Reproduce

1. Provide a minimal code snippet or test case:

```python
from vox_sdk.sdk.pipeline import Pipeline

# Minimal repro
def build_pipeline():
    return Pipeline(
        stt_provider="whisper",
        llm_provider="ollama",
        tts_provider="kokoro",
    )

# Show how you invoke it / inputs (audio, text, settings)
```

2. Exact inputs/config used (models, sample rates, prompts)
3. Any artifacts (short audio clip or text) to reproduce
4. Observe the error

## Expected vs Actual

- Expected: what should happen
- Actual: what happened instead (include stack trace if applicable)
- Frequency: always | often | intermittent

## Evidence

- Metrics summary (if any): output of `pipeline.log_metrics_summary()`
- Exceptions / Traceback (trimmed):

```
paste relevant trace here
```

- Artifacts (small): audio snippet details, model outputs, etc.

## RTC / Streaming (if applicable)

- Client (browser/app + version):
- Transport details (if known): sample rate, channels, latency
- STUN/TURN configuration (if used): reachable yes | no

## Adapter / Model Context (if applicable)

- LLM: provider/model + versions
- STT: provider/model + config
- TTS: provider/model/voice + sample rate

## Logs

<details>
<summary>SDK logs (trimmed)</summary>

```
paste relevant logs here
```

</details>

## Tests / CI Signal

- Local test command output (pytest):

<details>
<summary>Pytest trace</summary>

```
paste failing test output here
```

</details>

- CI lint/type/test failures: link to run if applicable

## Additional Context

- Concurrency/load when observed
- Recent related changes (links to PRs/issues)
- Workarounds tried
