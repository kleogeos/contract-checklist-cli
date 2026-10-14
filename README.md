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

## What it checks

Payment terms, late fees, scope of work, revision limits, IP/ownership, termination, confidentiality, deposit/kill fee, liability, governing law.

**This is a keyword heuristic, not legal advice.** It won't catch clauses phrased unusually, and finding a keyword doesn't mean the clause is actually good — read your contract.

## Zero dependencies

Python 3 standard library only.

## More freelance tools

Free web tools: [invoice generator](https://kleogeos.github.io/freelancer-tools/invoice.html) · [rate calculator](https://kleogeos.github.io/freelancer-tools/rate-calculator.html)

CLI invoice generator: [freelance-invoice-cli](https://github.com/kleogeos/freelance-invoice-cli)

Full paperwork kit — a ready-to-use contract plus proposal, invoice, and client scripts: [Freelancer Starter Kit ($15)](https://kleogeos.gumroad.com/l/nvjec)

## License

MIT
