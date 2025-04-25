import argparse
import asyncio
from Project1.currency import get_currency_for_last_days
from Project1.logger import log_exchange_command

def parse_args():
    parser = argparse.ArgumentParser(description="Currency exchange rate tool.")
    parser.add_argument("days", type=int, help="Number of last days to retrieve exchange rates")
    parser.add_argument("--currencies", nargs='+', default=['USD', 'EUR'], help="Currencies to fetch")
    return parser.parse_args()

async def main():
    args = parse_args()
    
    if args.days < 1 or args.days > 10:
        print("You can only retrieve rates for the last 10 days.")
        return

    try:
        data = await get_currency_for_last_days(args.days)
        
        await log_exchange_command(f"Requested exchange rates for the last {args.days} days: {data}")

        print(data)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
