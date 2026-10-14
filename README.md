# contract-checklist-cli

Scan a freelance contract (plain text or Markdown) for commonly-missing clauses — payment terms, late fees, IP ownership, termination, liability, and more. A 2-second sanity check before you sign or send.

```bash
python3 check.py my-contract.md
```

```
Checked my-contract.md — 3/10 common clauses detected.

Found:
  [x] payment terms / due date
  [x] scope of work / deliverables
  [x] revision limit

Possibly missing — worth double-checking:
  [ ] late payment fee / interest
  [ ] intellectual property / ownership
  [ ] termination clause
  ...
```

Exits non-zero if anything looks missing, so you can wire it into a pre-send checklist or CI step.

### Install (optional)

```bash
pip install git+https://github.com/kleogeos/contract-checklist-cli
contract-checklist my-contract.md
```

### Use as a pre-commit hook

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/kleogeos/contract-checklist-cli
    rev: main
    hooks:
      - id: contract-checklist
```

By default it only runs on files whose path matches `contract|agreement|sow` (case-insensitive) — adjust `files:` in your config if your filenames differ.

## What it checks

Payment terms, late fees, scope of work, revision limits, IP/ownership, termination, confidentiality, deposit/kill fee, liability, governing law.

**This is a keyword heuristic, not legal advice.** It won't catch clauses phrased unusually, and finding a keyword doesn't mean the clause is actually good — read your contract.

## Zero dependencies

Python 3 standard library only.

## More freelance tools

Free web tools: [invoice generator](https://kleogeos.github.io/freelancer-tools/invoice.html) · [rate calculator](https://kleogeos.github.io/freelancer-tools/rate-calculator.html) · [this tool as a web form](https://kleogeos.github.io/freelancer-tools/contract-checklist.html)

CLI invoice generator: [freelance-invoice-cli](https://github.com/kleogeos/freelance-invoice-cli) · CLI rate calculator: [freelance-rate-cli](https://github.com/kleogeos/freelance-rate-cli)

Full paperwork kit — a ready-to-use contract plus proposal, invoice, and client scripts: [Freelancer Starter Kit ($15)](https://kleogeos.gumroad.com/l/nvjec)

## License

MIT
