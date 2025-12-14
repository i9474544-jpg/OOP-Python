import logging
from datetime import date

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d"
)

logging.info(f"Поточна дата: {date.today().strftime('%Y-%m-%d')}")
