"""Independent check: rebuild the paper portfolio value from trades.csv with Yahoo Finance closes.
Runs on GitHub Actions. Writes verify/<date>.json and exits 1 if it disagrees with marks.csv by > 500 INR."""
import csv, json, sys, datetime, pathlib
import yfinance as yf
START=1_000_000.0; TOL=500.0
trades=list(csv.DictReader(open('trades.csv')))
marks=list(csv.DictReader(open('marks.csv')))
if not marks: print('no marks yet'); sys.exit(0)
last=marks[-1]; day=last['date']
cash=START; pos={}
for t in trades:
    if t['date']>day: continue
    q=int(t['qty']); v=float(t['value']); c=float(t['cost'])
    if t['side']=='BUY': cash-=v; pos[t['symbol']]=pos.get(t['symbol'],0)+q
    else: cash+=v; pos[t['symbol']]=pos.get(t['symbol'],0)-q
pos={k:v for k,v in pos.items() if v}
closes={}
for s in pos:
    h=yf.Ticker(s).history(start=day,end=(datetime.date.fromisoformat(day)+datetime.timedelta(days=1)).isoformat())
    if h.empty: print('no bar for',s,day); sys.exit(2)
    closes[s]=float(h['Close'].iloc[-1])
value=sum(closes[s]*pos[s] for s in pos); total=cash+value
diff=total-float(last['total'])
out=dict(date=day,checked_at=datetime.datetime.utcnow().isoformat()+'Z',cash=round(cash,2),positions_value=round(value,2),
         total=round(total,2),ledger_total=float(last['total']),difference=round(diff,2),closes=closes,ok=abs(diff)<=TOL)
pathlib.Path('verify').mkdir(exist_ok=True)
json.dump(out,open(f'verify/{day}.json','w'),indent=1); print(json.dumps(out,indent=1))
sys.exit(0 if out['ok'] else 1)
