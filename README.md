# PUNish

A Discord bot that delivers puns on demand. Type `PUNish` in any channel and the bot will respond with a random pun fetched from [JokeAPI](https://v2.jokeapi.dev/).

## Background

I have a love of puns and stumbled across JokeAPI while looking for something fun to build with. It gave me the perfect excuse to create my first Discord bot.

## How it works

The bot listens for any message containing the word `PUNish`. When triggered, it makes a request to JokeAPI's pun endpoint and posts the result back to the channel.

## Setup

### Prerequisites

- Python 3.x
- A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications)


### Environment variables

The bot reads your Discord token from an environment variable:

```
DISCORD_TOKEN=your_token_here
```

### Challenges Faced

I had some trouble entering the service variable through the GUI for Railway, so I configured it using the Railway CLI instead.

## Deployment

This bot is deployed on [Railway](https://railway.app). The `DISCORD_TOKEN` environment variable is set via Railway's service variables.

## Usage

In any Discord channel the bot has access to, type:

```
PUNish
```

The bot will respond with a pun. That's it. Just something for my personal discord server. 

<img width="704" height="130" alt="image" src="https://github.com/user-attachments/assets/463a0120-12ef-43a8-af4d-0a45531964e1" />

