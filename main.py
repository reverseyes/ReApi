import random
import httpx
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AutoSwipe & Roast Core Engine",
    version="1.1.0"
)

LOCAL_ROASTS = [
    # --- original list ---
    "you so big whenever you jump even earths magnetic force cant keep up",
    "roses are red, monsters are green, look in the mirror and youll see what i mean",
    "if you went and stepped on a scale right now it would probably end in ...",
    "2 + 2 = 4, go and try and learn some more",
    "your wifi router gets tired just trying to process your logic",
    "you look like a person who claps when the airplane lands",
    "you are the human equivalent of a software update that breaks everything",
    "if i wanted to listen to a joke id just ask you to talk about your plans",
    "somewhere out there is a tree working hard to make your oxygen go apologize to it",
    "light travels faster than sound which is why you looked bright until you opened your mouth",
    "your brain has an out of order sign permanently taped to it",
    "you bring absolute nothing to the table and the table is still disappointed",
    "your text messages are the reason people turn off read receipts",
    "you are the default skin of real life",
    "if ignorance is bliss you must be living in absolute paradise",
    "you look like the loading screen of an offline video game",
    "you are proof that anyone can get an internet connection these days",
    "i would try to insult you but nature already did a flawless job",
    "you are like a cloud when you disappear the day gets ten times better",
    "your life is like a movie but it went straight to dvd and got left on the dollar shelf",
    "you are the reason instructions are printed on shampoo bottles",
    "if i had a single dollar for every smart thing you said id be completely broke",
    "you have miles and miles to go before you even reach baseline mediocre",
    "your secrets are always safe because literally nobody is listening anyway",
    "you are the human version of a participation trophy that got stepped on",
    "your thoughts enter a black hole and never find their way back out",
    "you look like a background character in a game that has no dialogue options",
    
    # --- massive expansion (75 more roasts) ---
    "you have a face made for radio and a voice made for silent films",
    "your processing speed is slower than internet explorer on a dial up connection",
    "you bring an extreme lack of flavor to every single conversation",
    "if brains were dynamite you wouldnt even have enough to blow your nose",
    "you are the human equivalent of a wet paper towel",
    "you look like someone drew you with their non dominant hand",
    "your family tree must be a straight vertical line",
    "you are about as useful as a screen door on a submarine",
    "i would call you an alpha tester but you are barely pre alpha",
    "you are the reason the back space key on my keyboard is entirely worn out",
    "your opinions are like a recipe for ice water completely useless",
    "you could throw a rock at the ground and still miss completely",
    "you have the attention span of a goldfish that forgot to wake up",
    "your memory is like a sieve that got ran over by a lawnmower",
    "you are the physical embodiment of the word loading",
    "if you were any more generic you would be sold in a plain white box",
    "you look like a captcha puzzle that nobody can solve",
    "your logic is like a circular maze with no entrance",
    "you are about as bright as a broken flashlight in a cave",
    "you have the survival instincts of a cartoon character",
    "your personality is like unflavored gelatin left in the sun",
    "you are the reason they have to write keep out on empty rooms",
    "if you were an app you would require an immediate force close",
    "you look like you belong in the background of a low resolution video game",
    "your conversation style is just typing error error error over and over",
    "you are the human equivalent of a typographical error",
    "if you were an ingredient you would be lukewarm tap water",
    "you have the depth of a microscopic puddle on a sunny day",
    "your internal clock is stuck on dial up speed forever",
    "you look like a sketch that the artist gave up on halfway through",
    "you are about as dynamic as a brick wall in a black and white movie",
    "your presence is like a pop up ad that won't go away",
    "you have the charisma of a wet cardboard box in a basement",
    "if you were a color you would be slightly off white grey",
    "you are proof that time can be wasted completely automatically",
    "your jokes are like bad code they just don't compile at all",
    "you look like the default avatar of an abandoned internet forum",
    "your brain is currently operating on safe mode with no network connectivity",
    "you bring a whole new definition to the concept of baseline text",
    "you are about as sharp as a completely round bowling ball",
    "if you were a font you would be poorly spaced comic sans",
    "your life tracking bar is stuck at zero percent compilation link",
    "you look like you got generated by an artificial intelligence engine that crashed",
    "your critical thinking skills could easily fit inside a thimble with room to spare",
    "you are the reason they put do not drink warnings on liquid soap",
    "your strategy is like trying to catch smoke with a fishing net",
    "you have all the presence of a ghost that forgot how to haunt",
    "if you were a tool you would be a plastic hammer that bends",
    "you look like a character model before the textures are applied",
    "your communication style is just static noise and static feedback",
    "you are about as complex as a game of tic tac toe against yourself",
    "your social battery was built using a leaky double a cell",
    "you look like you walk into closed glass doors on a daily basis",
    "your brain processing loop is just an endless empty while loop",
    "you are the human version of a low signal strength indicator",
    "if you were an object you would be a single unlabelled button",
    "you have the spatial awareness of a roomba with a broken bumper",
    "your thought process is like a ball rolling down a completely flat hallway",
    "you look like you struggle to open zip lock bags",
    "your standard response is just a blank stare and blinking",
    "you are about as deep as a dry sheet of paper",
    "if you were a sound you would be a very quiet humming noise",
    "your main asset is that you are highly efficient at occupying physical space",
    "you look like you type with only your index fingers while looking at the keys",
    "your logic tree is just a single twig stuck in the mud",
    "you are the human equivalent of a blank sheet of printer paper",
    "if you were a plant you would be artificial grass that gathered dust",
    "your ideas are like vaporware they get announced but never show up",
    "you look like a character from a movie that got cut in the first edit",
    "your mental processing unit runs entirely on AAA batteries",
    "you are about as exciting as watching paint dry on a rainy afternoon",
    "if you were a custom skin you would be the default one everyone skips",
    "your layout parameters are entirely out of alignment with reality",
    "you look like you forget your own zip code when under pressure",
    "your system framework has completely reached its end of life support cycle"
]


class UserInput(BaseModel):
    name: str

@app.get("/")
def home():
    return {"message": "Welcome to my custom API!"}

@app.post("/api/greet")
def greet_user(data: UserInput):
    return {"message": f"Hello, {data.name}! Your Python API is working perfectly."}

# --- NEW ROAST ENDPOINT ---
@app.get("/roast", tags=["Fun Tools"])
async def get_roast():
    """
    Returns a random roast. 
    Flips a coin to pick from your custom list or grab a joke/roast from the internet!
    """
    # 50% chance to use your list, 50% chance to fetch from the web
    use_online_source = random.choice([True, False])

    if use_online_source:
        try:
            # We use an async HTTP client to pull a clean, programming/misc joke from the web
            async with httpx.AsyncClient() as client:
                response = await client.get("https://jokeapi.dev")
                joke_data = response.json()
                
                if joke_data["type"] == "single":
                    return {"source": "internet", "roast": joke_data["joke"]}
                else:
                    # If it's a two-part joke, combine setup and delivery
                    combined_joke = f"{joke_data['setup']} ... {joke_data['delivery']}"
                    return {"source": "internet", "roast": combined_joke}
        except Exception:
            # If the internet fetch fails or times out, fall back safely to your local list
            pass

    # Default fallback to your custom local list
    random_roast = random.choice(LOCAL_ROASTS)
    return {"source": "local_database", "roast": random_roast}
