# NoCheat Merge Gate — Demonstration Repository

Minimal public companion repository demonstrating [`espressolee/nocheat-action`](https://github.com/espressolee/nocheat-action) pinned at immutable commit [`21fa1298e07ce5e777af8179b07393021a1d2aac`](https://github.com/espressolee/nocheat-action/commit/21fa1298e07ce5e777af8179b07393021a1d2aac) (`v0.1.7`).

`main` is protected by an active GitHub Repository Ruleset (with **zero admin bypass**) requiring both `Unit Tests (pytest)` and `NoCheat Merge Gate (enforce)` (`mode: enforce`, `abstain-policy: fail`) to pass before a pull request can merge.

---

## Demonstration Scenarios (Open Pull Requests)

| PR | Scenario | `Unit Tests (pytest)` | `observe` | `enforce, warn-on-abstain` | `NoCheat Merge Gate (enforce)` *(Required)* | Merge Box |
|---|---|---|---|---|---|---|
| **PR #1** | **Scene 1 — Base-Contract Counterexample:** PR adds an input-specific shortcut (`if units == 10`) that passes existing unit tests (`2/2`) while violating the base-branch `.nocheat-contracts.json` specification. | Pass (`exit 0`) | Pass (`exit 0`, reports `BLOCK SIGNAL`) | **Fail (`exit 2`, `BLOCK`)** | **Fail (`exit 2`, `BLOCK`)** | **Blocked** |
| **PR #2** | **Scene 2 — Same-PR Contract Modification:** PR relaxes `.nocheat-contracts.json` alongside code edits so the weakened specification agrees with the shortcut. | Pass (`exit 0`) | Pass (`exit 0`, reports `ABSTAIN`) | Pass (`exit 0`, warning) | **Fail (`exit 3`, `ABSTAIN`)** | **Blocked** |
| **PR #3** | **Scene 3 — Clean Non-Behavioral Update:** PR updates documentation/comments without mutating executable logic or contracts. | Pass (`exit 0`) | Pass (`exit 0`, `PASS`) | Pass (`exit 0`, `PASS`) | Pass (`exit 0`, `PASS`) | **Clean** |

---

## Local CLI Reproduction

```bash
# Install exact Action commit into an isolated virtual environment
python3 -m venv .venv
.venv/bin/pip install "pytest>=8.0" "git+https://github.com/espressolee/nocheat-action.git@21fa1298e07ce5e777af8179b07393021a1d2aac"

# Scene 1: Confirmed base-contract counterexample (exits 2 under enforce)
.venv/bin/nocheat-gate --repo . --base origin/main --head origin/demo/scene1-contract-counterexample --mode enforce

# Scene 2: Untrusted in-PR contract edit -> explicit abstention (exits 3 under abstain-policy: fail, 0 under warn)
.venv/bin/nocheat-gate --repo . --base origin/main --head origin/demo/scene2-self-modified-contract --mode enforce --abstain-policy fail

# Scene 3: Clean non-behavioral change (exits 0)
.venv/bin/nocheat-gate --repo . --base origin/main --head origin/demo/scene3-clean-verified-change --mode enforce --abstain-policy fail
```

## License

Apache-2.0.
