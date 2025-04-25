from aiofile import AIOFile
from aiopath import Path

async def log_exchange_command(message: str):
    log_path = Path("exchange.log")
    
    try:
        # Перевірка, чи існує шлях, і створення його, якщо він відсутній
        if not await log_path.exists():
            await log_path.touch()  # Створення файлу, якщо його немає

        # Асинхронне відкриття файлу для додавання запису
        async with AIOFile(log_path, 'a') as afp:
            await afp.write(f"{message}\n")
        print(f"Message logged: {message}")

    except Exception as e:
        print(f"An error occurred while writing to log file: {e}")
