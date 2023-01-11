import discord
from discord import app_commands

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'{self.user}이 시작되었습니다')
        game = discord.Game('아지 디스코드: 맛나간 아지 시스템#1404')
        await self.change_presence(status=discord.Status.online, activity=game)


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name = "아지와드", description="아지와 와드의 관계를 설명해드립니다.")
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"아지와 와드는 1월 7일부터 시작해 현재까지 사귀고있는 로블록스 논산훈련소 8사단의 화끈한 커플입니다. 아지와 와드를 응원해주세요.", ephemeral = True)

@tree.command(name = "ban", description = "유저를 밴 시켜드려요.")
async def slash2(interaction: discord.Integration, 유저ID: str, 사유: str):
    embed = discord.Embed(title="유저 밴")
    embed.add_field(name="유저가 밴 되었습니다.", value="ㅤ", color=0x4000FF)
    embed.add_field(name="사유: ", value=format(사유), inline=False)


@tree.command(name = '질문', description = '아지봇을 통해 질문을 할 수 있습니다.')
async def slash2(interaction: discord.Interaction, 질문: str):

    
    embed = discord.Embed(title="아지에 대한 질문", description="ㅤ", color=0x4000FF)
    embed.add_field(name="질문이 접수되었습니다", value="ㅤ", inline=False)
    embed.add_field(name="질문 내용", value=format(질문), inline=False)
    embed.add_field(name="ㅤ", value="**질문 내용에 대한 답장은 아지가 확인후\n빠른 시일 내에 답장이 오니 기다려 주시면 감사하겠습니다**", inline=False)
    embed.add_field(name="ㅤ", value="- **맛나간 아지 시스템#1404** -", inline=False)

    await interaction.response.send_message(embed=embed)
    
    

# 967488772579151873
# 994589245220077671
    users = await client.fetch_user("994589245220077671")
    users2 = await client.fetch_user("967488772579151873")
    await users.send("유저 아이디 {}  / 질문 내용: {}".format(interaction.user.id, 질문))
    await users2.send("유저 아이디 {}  / 질문 내용: {}".format(interaction.user.id, 질문))






@tree.command(name = '질문답변', description = '아지봇을 통해 질문에 답변을 할 수 있습니다')
async def slash2(interaction: discord.Interaction, 아이디: str, 답변: str):
    users = await client.fetch_user("994589245220077671")
    users2 = await client.fetch_user("967488772579151873")
    if interaction.user.id == users or users2:
        embed = discord.Embed(title="질문 답변", description="ㅤ", color=0x4000FF)
        embed.add_field(name="질문에 대한 답변 내용", value="{}".format(답변) , inline=False)



        await interaction.response.send_message(f"✅")


        user = await client.fetch_user("{}".format(아이디))
        await user.send(embed=embed)
        return

    await interaction.response.send_message("당신은 어드민이 아닙니다. 질문답변 시도를 하지 말아주세요.")

client.run('MTA2MjU1NTYxNTQ2NzE1NTU4Nw.G9L4qX.NQcMYsWNXuqYYZbRUL5adKKqp4vxerbKjbetAI')