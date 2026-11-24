import os

def main():
    """
    Dad Joke Showdown Entry:
    'My wife told me to stop impersonating a flamingo. I had to put my foot down.'
    Pun explanation: Flamingos stand on one leg, so 'putting your foot down' is both 
    a firm stance and a literal physical necessity for a flamingo!
    """
    joke = "My wife told me to stop impersonating a flamingo. I had to put my foot down."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
