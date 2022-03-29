#!/usr/bin/env python3
# add imports, if necessary
from public.exchange_rates import EXCHANGE_RATES as xr


def convert(amount, from_currency, to_currency):

    if to_currency not in xr or from_currency not in xr:
        raise Warning('Not a valid currency')
    if not isinstance(amount, (float, int)):
        raise Warning('Not a valid amount')
    if amount < 0: 
        raise Warning('It is a negative amount')

    if to_currency == from_currency: 
        return amount
    for e in xr:
        if e == from_currency:
            try: r = xr[from_currency][to_currency]
            except KeyError: continue
        elif e == to_currency:
            try: r = 1 / xr[to_currency][from_currency]
            except KeyError: continue

    return r*amount 