import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_join(member):
	role_id = 1254485361720033372
	role = member.guild.get_role(role_id)

	if role:
		await member.add_roles(role)
	else:
		await member.send("Role not found!")  # Add error handling if role is not found

	category_id = 1254485009163747402
	guild = member.guild
	category = discord.utils.get(guild.categories, id=category_id)

	if category:
		overwrites = {
			guild.default_role: discord.PermissionOverwrite(read_messages=False),
			guild.me: discord.PermissionOverwrite(read_messages=True),
			member: discord.PermissionOverwrite(read_messages=True),
			role: discord.PermissionOverwrite(read_messages=True)
		}

		channel_name = f"{member.id}s-channel"
		new_channel = await category.create_text_channel(channel_name, overwrites=overwrites)
		await new_channel.send(member.mention)

		for channel in category.channels:
			overwrite = {
				member: discord.PermissionOverwrite(read_messages=True) if channel == new_channel else discord.PermissionOverwrite(read_messages=False)
			}
			await channel.edit(overwrites=overwrite)

		def check(m):
			return m.author == member and m.channel == new_channel

		try:
			await new_channel.send(f"""```arm
			Establishing connection to the server...
			```""")
			await asyncio.sleep(2)
			await new_channel.send(f"```C:\\Users\\localuser>ping the_real_district.nu```")
			await asyncio.sleep(1)

			await new_channel.send(f"```Pinging the_real_district.nu [142.250.184.14] with 32 bytes of data:```")
			await asyncio.sleep(0.3)
			await new_channel.send(f"```Reply from 142.250.184.14: bytes=32 time=28ms TTL=116```")
			await asyncio.sleep(0.3)
			await new_channel.send(f"```Reply from 142.250.184.14: bytes=32 time=28ms TTL=116```")
			await asyncio.sleep(0.3)
			await new_channel.send(f"```Reply from 142.250.184.14: bytes=32 time=28ms TTL=116```")
			await asyncio.sleep(0.3)
			await new_channel.send(f"```Reply from 142.250.184.14: bytes=32 time=28ms TTL=116```")
			await asyncio.sleep(0.3)

			await new_channel.send(f"""```Ping statistics for 142.250.184.14:
				Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
			Approximate round trip times in milli-seconds:
				Minimum = 28ms, Maximum = 28ms, Average = 28ms```""")
			await asyncio.sleep(1)
			await new_channel.send(f"""```CONNECTED```""")
			await asyncio.sleep(1)

			await new_channel.send(f"Welcome to the security check {member.mention}, please try answering these questions with 1 or 2 words")
			await new_channel.send(f"```Which district does this network belong to? ```")
			message = await bot.wait_for('message', check=check, timeout=600)

			if "terra" in str(message.content).lower():
				await new_channel.send(f"```Who governs this district?```")
				message = await bot.wait_for('message', check=check, timeout=600)

				if "willie" in str(message.content).lower() or "crow" in str(message.content).lower():
					await new_channel.send(f"```During which era did AE-02 occur in the eastern region?```")
					message = await bot.wait_for('message', check=check, timeout=600)

					if "unification" in str(message.content).lower():
						await new_channel.send(f"```Are blights curable? ```")
						message = await bot.wait_for('message', check=check, timeout=600)

						if "no" in str(message.content).lower() and "know" not in str(message.content).lower():
							await new_channel.send(f"```At what stage are infected individuals ineligible for help?```")
							message = await bot.wait_for('message', check=check, timeout=600)

							if "incubation" in str(message.content).lower():
								await new_channel.send(f"Status: Approved")
								await member.add_roles(member.guild.get_role(1254790580832178276))
								await member.remove_roles(role)
								await new_channel.delete(reason='Timeout error')
							else:
								await member.kick(reason='{Status: Denied, Reason: Incorrect answer}')

						else:
							await member.kick(reason='{Status: Denied, Reason: Incorrect answer}')

					else:
						await member.kick(reason='{Status: Denied, Reason: Incorrect answer}')

				else:
					await member.kick(reason='{Status: Denied, Reason: Incorrect answer}')

			else:
				await member.kick(reason='{Status: Denied, Reason: Incorrect answer}')

		except asyncio.TimeoutError:
			await member.kick(reason='{Status: Denied, Reason: TimeoutError}')

	else:
		await member.send("Category not found!")  # Add error handling if category is not found


@bot.event
async def on_member_remove(member):
	# Check if the member has a private channel and delete it if exists
	category_id = 1254485009163747402
	guild = member.guild
	category = discord.utils.get(guild.categories, id=category_id)
	
	if category:
		channel_name = f"{member.id}s-channel"
		new_channel = discord.utils.get(category.text_channels, name=channel_name)

		if new_channel:
			await new_channel.delete(reason=f'{member.display_name} left the server')
		else:
			print(f"Private channel for {member.display_name} not found.")

	else:
		print("Category not found!")

@bot.event
async def on_member_ban(guild, user):
	# Check if the banned member has a private channel and delete it if exists
	category_id = 1254485009163747402
	guild = user.guild
	category = discord.utils.get(guild.categories, id=category_id)

	if category:
		channel_name = f"{user.id}s-channel"
		new_channel = discord.utils.get(category.text_channels, name=channel_name)

		if new_channel:
			await new_channel.delete(reason=f'{user.display_name} was banned from the server')
		else:
			print(f"Private channel for {user.display_name} not found.")

	else:
		print("Category not found!")

bot.run('secret-key')
