import chatty

if __name__ == "__main__":
    chatty_bot = chatty.chatty()
    respond = chatty_bot.chat_respond("my name is marcin")
    print(respond)