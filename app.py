from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()

# Configurando templates e arquivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Variáveis do jogo
words = ["java", "javascript"]
sorted_word = random.choice(words)
hidden_word = "-" * len(sorted_word)
guessed_letters = []
max_tries = 6


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "hidden_word": hidden_word,
            "guessed_letters": guessed_letters,
            "max_tries": max_tries,
        },
    )


@app.post("/guess", response_class=HTMLResponse)
async def guess(request: Request, letter: str = Form(...)):
    global hidden_word, guessed_letters, max_tries, sorted_word

    if letter in guessed_letters:
        message = "You already typed this letter. Try again!"
    else:
        guessed_letters.append(letter)

        if letter in sorted_word:
            hidden_word_list = list(hidden_word)
            for i in range(len(sorted_word)):
                if letter == sorted_word[i]:
                    hidden_word_list[i] = letter
            hidden_word = "".join(hidden_word_list)
            message = f"Correct! {hidden_word}"
        else:
            max_tries -= 1
            message = f"Wrong guess! You have {max_tries} tries left."

    if hidden_word == sorted_word:
        message = f"Congratulations! You guessed the word '{sorted_word}'!"
    elif max_tries == 0:
        message = f"You lost! The word was '{sorted_word}'."

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "hidden_word": hidden_word,
            "guessed_letters": guessed_letters,
            "max_tries": max_tries,
            "message": message,
        },
    )
