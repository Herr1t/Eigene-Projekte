import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bit = response.json()
bpi = bit["bpi"]
usd = bpi["USD"]
rate_float= usd["rate_float"]

#for bpi in bit["bpi"]:
#    bpi = bit["bpi"]
#    for usd in bpi["USD"]:
#        usd = bpi["USD"]
#        rate_float = usd["rate_float"]

while True:
    try:
        i = float(sys.argv[1])
        c = 3
        out = i * rate_float
        count = len(str(int(out)))
        out = str("%.4f" % out)
        if count > 3:
            while True:
                out = out[:count-c] + ',' + out[count-c:]
                c = c + 3
                if c >= count:
                    break
            print(f"${out}")
            sys.exit()
        else:
            print(f"${out}")
            sys.exit()
    except(IndexError):
        print("Missing command-line argument")
        sys.exit(1)
    except(ValueError):
        print("Command-line argument is not a number")
        sys.exit(1)