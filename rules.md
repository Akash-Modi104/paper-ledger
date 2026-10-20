# Paper portfolio — ₹10 lakh, NSE only (PAPER, not real money)

Started 18 Oct 2026 at akash's ask. Nothing here is a real order. Never mixed into the real portfolio or the goal tracker.

## Window
- Entry: Monday 19 Oct 2026 at the NSE open (first daily bar's open price from Yahoo Finance).
- End: Thursday 19 Nov 2026 close. Final result = closing value after exit costs vs ₹10,00,000.
- Benchmarks: Nifty 50 (^NSEI) and Nifty 500 (^CRSLDX) price return over the same window.

## Target and honesty note
- Target rate: 30% a year = about 2.2% for one month (1.30^(1/12) − 1). One month is mostly noise; the chosen rule backtested ~25%/yr over 14 years with Nifty filter, worst month −9.8%. Without the filter (always invested, as here) expect bigger swings.

## Selection rule (fixed on 18 Oct 2026, data to 16 Oct close)
- Universe: 100 NSE large/mid caps in universe.txt (same as the 17 Oct backtests).
- Rank by 12-1 month return (price ~12 months ago to price ~1 month ago). Keep only names closing above their own 200-day average. Take the top 8.
- Equal weight ₹1,25,000 each (12.5%; cap 20%). Whole shares only; leftover stays as cash.
- No Nifty 200-day filter (it is OFF today); akash wants the money invested, so each stock's own trend is the filter instead.

## Exit rules (checked at each daily mark, executed at the next open)
- Stop: close more than 8% below entry price → sell.
- Trend: close below its own 200-day average → sell.
- Proceeds sit as cash (no re-entry) until the month ends. No other trading in the window.

## Costs (Zerodha delivery, approximated)
- 0.2% per side on every buy and sell (covers STT 0.1%, exchange, GST, stamp, DP charge). Brokerage on delivery is zero.

## Marking
- Once a day after the NSE close (16:10 IST) on trading days: prices from Yahoo Finance, written to marks.csv, tracker.md refreshed, exits for tomorrow listed.
- If Yahoo's last bar is not today's date (holiday or feed down), the run records nothing and says so in log.md.
