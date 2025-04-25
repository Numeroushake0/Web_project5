import aiohttp
import asyncio
from datetime import datetime, timedelta

API_URL = "https://api.privatbank.ua/p24api/exchange_rates"
CURRENCY_PAIRS = ['USD', 'EUR']

async def fetch_currency_data(date: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"{API_URL}?date={date}") as response:
                response.raise_for_status()
                data = await response.json()
                return {date: {currency['currency']: {
                    'sale': currency['saleRate'],
                    'purchase': currency['purchaseRate']
                } for currency in data['exchangeRate'] if currency['currency'] in CURRENCY_PAIRS}}
        except aiohttp.ClientError as e:
            print(f"Error fetching data for {date}: {e}")
            return None

async def get_currency_for_last_days(days: int):
    today = datetime.today()
    dates = [(today - timedelta(days=i)).strftime('%d.%m.%Y') for i in range(days)]
    tasks = [fetch_currency_data(date) for date in dates]
    results = await asyncio.gather(*tasks)
    return results
