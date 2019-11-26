from nltk.chat.util import Chat, reflections
from talk import pairs,speach

class chatty():
    def chat_converse(self):
        print(speach.initial_spich)
        pairs_library = pairs.get_pairs()
        chat = Chat(pairs_library, reflections)
        chat.converse()

    def chat_respond(self,message):
        pairs_library = pairs.get_pairs()
        chat = Chat(pairs_library, reflections)
        return chat.respond(message)