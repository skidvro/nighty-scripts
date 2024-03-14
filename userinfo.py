@bot.command()
async def userinfo(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)
        created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
        joined_at = ctx.guild.get_member(user.id).joined_at.strftime("%Y-%m-%d %H:%M:%S")
        badges = ", ".join(badge.name.replace('_', ' ').title() for badge in user.public_flags.all())
        
        info = f"ID: {user.id}\n"
        info += f"Username: {user.name}\n"
        info += f"Discriminator: {user.discriminator}\n"
        info += f"Bot?: {user.bot}\n"
        info += f"Account Creation Date: {created_at}\n"
        info += f"Server Join Date: {joined_at}\n"
        info += f"Badges: {badges or 'None'}"

        await ctx.send(f"```{info}```")
    except discord.NotFound:
        await ctx.send("User not found.")
