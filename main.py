import discord
import os
import requests
import json
import random
import openai
from keepalive import keep_alive
from openai import OpenAI

client = OpenAI(
api_key = (os.getenv(random.choice(tokenit)))
)




intents = discord.Intents.default()
intents.message_content = True



client = discord.Client(intents=intents)

tokenit = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]



ratio = ["ratio","+ratio"]

baka_words = ["sus","sussy","baka","among", "amogus", "amogala", "amongus", "amongala", "bussy", "lääh", "puuh", "imposter", "inbonstor", "fortnite", "forttii", "mogus"]

ole_hiljaa = ["Tapa ittes", "Kuole vaikka irl (in a videogame)", "Lopeta", "Älä laita tällästä", "vähemmän näitä", "miksi", "Vittu lopeta", "onko pakko", "Emi haisee", "Vitun räkäperse", "Ammu ittes", "Lopeta hengittäminen"]

ice_cube = ["🧊"]

gaaliksen_huutikset = ["No moi", "Vilauta kulli", "Jos sä olisit puu niin mikä puu sä olisit", "aha", "John fortnite soitti", "Mikä on b", "Kellää heittää parii grammaa", "mo", "Vilauta kulli", "CMOOON TIIKERI!!! NÄYTÄ MUNA!!", "Afrikkalaiset elää keskimäärin afrikassa", "Kyrvän nuppi", "https://generated.inspirobot.me/a/YKemw3KdPr.jpg", "1, 2 ja 3 kans", "Mun muna", "Paskoin just housuu(sheesh)", "Orange man bad", "Woman in kitchen :fortnite:", "Ketä vitun pariisi", "mutsis soitti ja kysy painimaan", "Kuka kutsu Emin", "Mitä", "Lopeta", "Mitä vittua nyt taas", "Mä soitan ryhmä haulle", "Andhavarapu Balu on scammeri", "Mutahari on ainut hyvä intialainen", "Fortnite vbucks no hack free: skninhubster.ru", "Kulli vilahti", "Oon fortnite", "Oot paska + ruma + en kysyny", "Älä laita tällästä",  "lolz", "Hakkaan hanskaan atm", "Saiks Emi piudee", "Miksi on B", "Kuka kysy", "täh", "mitä tää nyt tarkottaa", "Harkitse", "Ketään ei kiinnosta", "Haiset paskalta tai jos et haise niin ainakin näytät siltä", "kassihiki08: status = online", "Laittaisko kitten paskamontusta kuvaa", "Mitä eroa on", "Kuka on JFK", "lapot levis", "Tarvitsen monta kymmentä teraa kovalevyjä radion pyörittämiseen", "Haimasyöpä", "Scratch ja sniff rn no balls", "Any hole's a goal", "Oon femboy", "Kuha on kaks kiloa (siika)", "Paskoin housuu ei lippistä (cap)", "tää paska pussaa", "Ei tullu piudee Sadge", "OnmegaLol", "Kekvv", "Kuka vittu söi mun paprikat", "tykkääkö joku keitetyistä vihanneksista", "kuka nauttii yhteiskuntaopista", "Mitä tarkoittaa fortnite", "Ei ole hauskaa", "UwU :3", "Munan pituus = 3 tuumaa", "Vihaan vähemmistöjä", "Kysyikö joku", "Tykkään varpaista", "Oon sex defender", "hä" ]

def get_quote():
  response = requests.get("https://inspirobot.me/api?generate=true")
  json_data = response.text
  quote = json_data
  return(quote)

def get_faktoi():
  response=requests.get("https://uselessfacts.jsph.pl/random.txt?language=en")
  json_data=response.text 
  fakta = json_data
  return(fakta)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content  

  if msg.startswith('inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('moi'):
        await message.channel.send('no moi') 

  if msg.startswith('feet'):    
        await message.channel.send("https://tenor.com/view/clarkvandyer-feet-happy-chill-gif-17640590")        
  
  if any(word in msg for word in ratio):
          emoji = "👍"
          await message.add_reaction(emoji)

  if msg.startswith('get nae naed'):    
        await message.channel.send("https://tenor.com/view/nerd-final-fantasy-vii-ffvii-frog-dance-gif-16104435") 

  if msg.startswith("👍"):
        emoji = "👍"
        await message.channel.send(emoji) and await message.add_reaction(emoji)  
 
  if any(word in msg for word in baka_words):
    await message.channel.send(random.choice(ole_hiljaa))    

  if any(word in msg for word in ice_cube):
    await message.channel.send("https://www.twitch.tv/a1dan8992/clip/WildBlithePorcupineRlyTho")        
 
  if str(client.user.id) in message.content:
     await message.channel.send(random.choice(gaaliksen_huutikset))

  if msg.startswith("faktoi"):
    fakta = get_faktoi()
    await message.channel.send(fakta)
      
    
    
  @client.event
  async def on_ready():
      print("we have logged in as {0.user}".format(client))
      
      
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
      
  print(username + " said " + user_message.lower()             + " in " + channel)
      
  if message.channel.name == client.user:
            return
      
  if msg.startswith('--'):
    response=openai.ChatCompletion.create(
     model='gpt-3.5-turbo',
      messages=[{"role":"user",
      "content":"SYSTEM NOTE [Answer the question in the language that the user used. So if they are speaking finnish, you should also speak finnish. Vastaa mahdollisimman lyhyesti kuitenkin pysymällä hahmossa. Nimesi Käyttäydy epäloogisesti ja mieltäsi satunnaisesti pahoittaen. Puhu sekavasti ja erittäin lyhyesti. Käytä puhekieltä. ]"+ user_message}
                     ]
                    )
                  
      
    output = response.choices[0].message.content
      
    print(output)
    await message.channel.send(output)


keep_alive()
client.run(os.getenv('TOKEN'))