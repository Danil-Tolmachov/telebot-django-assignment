## Setup steps:

1. Clone repository.
```git clone https://github.com/Danil-Tolmachov/telebot-django-assignment```

2. Get inside.
```cd telebot-django-assignment```

3. Create and setup *.env* file.


**.env file example content:**
```

BOT_TOKEN=*Telegram bot token*
SECRET_KEY=django-insecure-9f$m(!ytqco8+s7ag2sc2+hh2=5t4kn)9)ebodrcrh&8^pt@ps
DEBUG=True

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=accumulation_db
POSTGRES_PORT=5433

API_URL=http://api:8000/

```

4. Start docker-compose file.
```docker compose -f "docker-compose.yaml" up -d --build```

5. Start chat with your telegram bot.