# Paper portfolio ledger (virtual money, NSE, 19 Oct – 19 Nov 2026)

Public, append-only record of a one-month paper-trading exercise. Nothing here is a real order.

**Live dashboard:** https://akash-modi104.github.io/paper-ledger/ (rebuilt from this repository on every push; the page itself reads `marks.csv`, `trades.csv` and `positions.json`).

**What proves "no cheating"**
1. `rules.md` was fixed before the first trade. Any later edit shows in the commit history.
2. `trades.csv` and `marks.csv` are pushed after every NSE close. GitHub records when each push arrived; a trade can only be added after the day it happened.
3. Each trading day is also posted as a comment on the "Daily log" issue. GitHub stamps those server-side and marks any edit.
4. A GitHub Action (`.github/workflows/verify.yml`) runs on GitHub's own servers every weekday evening. It reads `trades.csv`, fetches closes from Yahoo Finance itself and writes its own portfolio value to `verify/`. If it disagrees with `marks.csv` by more than ₹500 it fails the run.

**Files**
- `rules.md` selection, exit, cost and marking rules
- `trades.csv` every buy and sell: date, time, symbol, qty, price, cost
- `marks.csv` one row per trading day: cash, positions value, total, return, Nifty 50, Nifty 500
- `tracker.md` current one-page standing; `log.md` run log; `universe.txt` the 100-name universe
- `verify/` independent recomputation by GitHub Actions
