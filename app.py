from libs.openexchange import OpenExchangeClient
import time



APP_ID = "ADD_HERE_THE_APP_ID_AFTER_CREATING_THE_ACCOUNT"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
print(f'First call took {time.time() - start} seconds.')

start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
print(f'After, 10 calls took {time.time() - start} seconds.')

print(f"USD{usd_amount} is GBP{gbp_amount}")
