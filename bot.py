
import discord, random
from discord.ext import tasks, commands
import asyncio

Channel_ID =
token =''

client = commands.Bot(command_prefix = '!')

# client = discord.Client()

imgs=[
    'https://i.imgur.com/3qM31AN.png',
    'https://i.imgur.com/YuoWNz8.png',
    'https://i.imgur.com/hZQL3sW.jpg',
    'https://i.imgur.com/SadyvLu.jpg',
    'https://i.imgur.com/eTxAaJs.png',
    'https://i.imgur.com/uev1Jw8.jpg',
    'https://i.imgur.com/Iqgciwx.png',
    'https://i.imgur.com/wNJxHq5.png',
    'https://i.imgur.com/bA9gemU.png',
    'https://i.kym-cdn.com/photos/images/newsfeed/000/413/128/5a0.png',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_mZ6mpQHdygWwXs2X0RPSkYCApaRaiqD9pw&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA5tsE5YFte_MtRaMSOCqk3plgFEzdkAYbQw&usqp=CAU',
    'https://i.redd.it/b6uyy222x8i41.png',
    'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/57b6461b-d026-4553-b3fc-58e70c83f25c/d1gcs1h-288ef140-c1c8-4280-812a-69f0f65f8a09.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNTdiNjQ2MWItZDAyNi00NTUzLWIzZmMtNThlNzBjODNmMjVjXC9kMWdjczFoLTI4OGVmMTQwLWMxYzgtNDI4MC04MTJhLTY5ZjBmNjVmOGEwOS5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.JcSK2qPoYwmRd4KMII51yPSjn_r9DJFHm_M23-rUIbc',
    'https://preview.redd.it/wb9bs0zco0661.jpg?width=640&crop=smart&auto=webp&s=416acd62a9738c653c220bf0a24d74973791616b',
    'htps://i.redd.it/54k2d931hh561.jpg',
    'https://preview.redd.it/fiypdg6xgg461.jpg?width=640&crop=smart&auto=webp&s=1159c2ad52ccb68004d34af8eed60e1a79ced4c3',
    'https://preview.redd.it/024g86kzdd261.jpg?width=640&crop=smart&auto=webp&s=209913aac329106e60e30329f68e979bb40ed245',
    'https://preview.redd.it/0sk38hzb8qy51.jpg?width=640&crop=smart&auto=webp&s=d461ffe2b696f598bc4b1396ea1cbe5c28db96aa',
    'https://preview.redd.it/kjblhdvlspu51.jpg?width=640&crop=smart&auto=webp&s=11196f6a2ca2f91971653cea0996960faa17e717',
    'https://preview.redd.it/r964di9gees51.jpg?width=640&crop=smart&auto=webp&s=348b3a505ceed3b85366b5482e7514700eacfbd8',
    'https://preview.redd.it/5i1umn0yvap51.png?width=640&crop=smart&auto=webp&s=48791f2d50f8d71c37e7f93e1bbedbd7449cab3a',
    'https://preview.redd.it/8njcuznlwsn51.png?width=640&crop=smart&auto=webp&s=abd3224d90acf8abd6a99f6537945cb9b9b311c8',
    'https://preview.redd.it/qvnq5z30s5l51.jpg?width=640&crop=smart&auto=webp&s=e58e4359e7997d57f318420beeb9d04fdfb8350a',
    'https://preview.redd.it/4tpwyhvi4xh51.jpg?width=640&crop=smart&auto=webp&s=71460d1573cc3772b40b656c8e859d6d02af1b53',
    'https://preview.redd.it/hekm1p6a75751.jpg?width=640&crop=smart&auto=webp&s=268e37b9a90d109b6f2649cc994911fe29b9d2ce',
    'https://preview.redd.it/es5md28h6r151.jpg?width=640&crop=smart&auto=webp&s=d1a07a1a09a03ae9962ebfa4fac6134efd11c12f',
    'https://preview.redd.it/ojjorj256d051.jpg?width=640&crop=smart&auto=webp&s=26ca582cbca0df747d4920e48df178d914c03567',
    'https://preview.redd.it/zw457a1y9cl41.jpg?width=640&crop=smart&auto=webp&s=43a63f6b8346fe1859600d1f02367c592e00fad0'



]

#@tasks.loop(seconds=15)
@tasks.loop(hours=1)
async def test():
     channel = client.get_channel(Channel_ID)
     await channel.send("ℕ𝕖𝕧𝕖𝕣 𝕗𝕠𝕣𝕘𝕖𝕥 𝕋𝕙𝕖 𝔾𝕒𝕞𝕖")

@client.event
async def on_ready():
     test.start()

@client.command()
async def thegame(ctx):
    await ctx.send(imgs[random.randint(0, 28)])
  #  await ctx.send(file=discord.File(imgs[random.randint(0, 1)]))



client.run(token)
