import discord
import re

class Wheatley(discord.Client):

    re_check_nickname = re.compile("^[\w\s]+ \(\w{2,4}\)$")

    async def on_ready(self):
        """ Callback for when the bot successfully logged in."""
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        """ Callback for when any message is send in the server.

            Args:
                message (discord.Message): The Discord message object received.
        """
        author = message.author

        # We ignore bot's own messages, and consider only messages from a server's member
        if author != self.user and isinstance(message.author, discord.member.Member):

            # Send DM is the user name is not correctly formatted
            if not self.re_check_nickname.match(author.display_name):
                await self._warn_wrong_nickname(author)
                

    # ------------------------------
    # Direct Messages methods
    #-------------------------------
    async def _warn_wrong_nickname(self, member):
        """ Sends a DM about a wrongly formatted nickname.

            Args:
                member (discord.Member): The recipient of the message.
            Await:
                message sent to the member's dm_channel.
         """
        
        wrong_nick_message = "Dear %s,\n\nPlease set your nickname properly on the Odoo Discord Server !" \
                            "\nIt should be only your firstname followed by your trigram between parentheses, like the following:" \
                            "\n\n**Firstname (abc)**" \
                            "\n\nIn order to do that, simply **Right Click** on the **Server Logo** > **Change Nickname**" % member.display_name
        change_nickname_img = discord.File('wheatley/res/img/change_nickname.png')

        # DM Channel must be created the first time a message is send to someone.
        if member.dm_channel is None:
            await member.create_dm()

        await member.dm_channel.send(content=wrong_nick_message, file=change_nickname_img)
