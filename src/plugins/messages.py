from logging import getLogger
import re
from string import punctuation
from crescent import Context, Plugin, message_command
from emoji import emoji_count
from hikari import Message, RESTBot


plugin = Plugin[RESTBot, None]()
log = getLogger(__name__)

@plugin.include
@message_command(name="Letter Count")
async def message_letter_count(ctx: Context, message: Message):
    letter_count = sum(not c.isspace() for c in message.content or "")
    noun = "letter" if letter_count == 1 else "letters"

    await ctx.respond(
        f"[This]({message.make_link(ctx.guild_id)}) message has {letter_count} {noun} in it.",
    )

@plugin.include
@message_command(name="Word Count")
async def message_word_count(ctx: Context, message: Message):
    word_count = len(re.findall(r"\S+", message.content or ""))
    noun = "word" if word_count == 1 else "words"

    await ctx.respond(
        f"[This]({message.make_link(ctx.guild_id)}) message has {word_count} {noun} in it.",
    )
    return

@plugin.include
@message_command(name="Emoji Count")
async def message_emoji_count(ctx: Context, message: Message):
    _emoji_count = emoji_count(message.content or "")
    noun = "emoji" if _emoji_count == 1 else "emojis"

    await ctx.respond(
        f"[This]({message.make_link(ctx.guild_id)}) message has {_emoji_count} {noun} in it.",
    )
    return

@plugin.include
@message_command(name="Punctuation Count")
async def message_punctuation_count(ctx: Context, message: Message):
    punctuation_count = re.findall(r"[^\w\s]", message.content or "")
    noun = "punctuation mark" if len(punctuation_count) == 1 else "punctuation marks"

    await ctx.respond(
        f"[This]({message.make_link(ctx.guild_id)}) message has {len(punctuation_count)} {noun} in it.",
    )
    return


@plugin.load_hook
def setup():
    log.info("Loaded %s", __name__)

@plugin.unload_hook
def teardown():
    log.info("Unloaded %s", __name__)
