import discord
from discord.ext import commands

from alttprbot.alttprgen.generator import ALTTPRMystery
from pyz3r.alttpr import ALTTPR


class Aqttp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aqttp(self, ctx, count=3):
        mystery = await ALTTPRMystery('aqttp').generate_test_game()
        settings_map = await ALTTPR().randomizer_settings()

        for c in range(count):
            settings = mystery.settings
            meta = settings

            embed = discord.Embed(
                title=f"Seed #{c + 1}",
                color=discord.Colour.blue()
            )

            embed.add_field(
                name='Item Placement',
                value="**Glitches Required:** {logic}\n**Item Placement:** {item_placement}\n**Dungeon Items:** {dungeon_items}\n**Accessibility:** {accessibility}".format(
                    logic=meta['glitches'],
                    item_placement=settings_map['item_placement'][meta['item_placement']],
                    dungeon_items=settings_map['dungeon_items'][meta['dungeon_items']],
                    accessibility=settings_map['accessibility'][meta['accessibility']],
                ),
                inline=True)

            embed.add_field(
                name='Goal',
                value="**Goal:** {goal}\n**Open Tower:** {tower}\n**Ganon Vulnerable:** {ganon}".format(
                    goal=settings_map['goals'][meta['goal']],
                    tower=meta['crystals'].get(
                        'tower', 'unknown'),
                    ganon=meta['crystals'].get(
                        'ganon', 'unknown'),
                ),
                inline=True)
            embed.add_field(
                name='Gameplay',
                value="**World State:** {mode}\n**Boss Shuffle:** {boss}\n**Enemy Shuffle:** {enemy}\n**Hints:** {hints}".format(
                    mode=settings_map['world_state'][meta['mode']],
                    boss=settings_map['boss_shuffle'][meta['enemizer']
                    ['boss_shuffle']],
                    enemy=settings_map['enemy_shuffle'][meta['enemizer']
                    ['enemy_shuffle']],
                    hints=meta['hints']
                ),
                inline=True)
            embed.add_field(
                name='Difficulty',
                value="**Swords:** {weapons}\n**Item Pool:** {pool}\n**Item Functionality:** {functionality}".format(
                    weapons=settings_map['weapons'][meta['weapons']],
                    pool=settings_map['item_pool'][meta['item']['pool']],
                    functionality=settings_map['item_functionality'][meta['item']
                    ['functionality']],
                ),
                inline=True)

            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Aqttp(bot))
