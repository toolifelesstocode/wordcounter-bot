from asyncio import run
from logging import INFO, basicConfig, getLogger
from os import environ
from pathlib import Path

from disnake.ext.commands.errors import ExtensionError
from dotenv import load_dotenv

from src import Bot


async def main():
    load_dotenv()
    basicConfig(
        format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
        level=INFO,
        datefmt="%Y-%m-%d - %H:%M:%S",
    )

    bot = Bot()
    log = getLogger(__name__)

    for extension in Path("src/exts").glob("**/*.py"):
        if extension.name.startswith("_"):
            continue

        ext = ".".join(extension.parts)[:-3]

        try:
            bot.load_extension(ext)
        except ExtensionError as e:
            log.error("error loading extension (%s): %s", e.name, e)
            log.warning("exiting...")
            exit(1)

    await bot.start(environ["BOT_TOKEN"])

if __name__ == "__main__":
    run(main())