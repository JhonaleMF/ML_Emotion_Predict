import re
enlaces = re.compile(r"http\S+")
signos = re.compile("(@TheBridge_Tech)|(ready)|(\%)|(\⬇)|(\;)|(\:)|(\/)|(\!)|(\¡)|(\?)|(\¿)|(\@)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\d+)|(\#)|(\”)|(\➡)|(\⤵)|(\▪)|(\ª)|(\▶)|(\')|(\.)|(\_)|(\’)")
theb = re.compile("(thebridgetech)")
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\🥵"
        u"\🤗"
        u"\🧑"
        u"\🤩"
        u"\🤸"
        u"\🤯"
        u"\✅"
        u"\⚽"
        u"\🤓"
        u"\🤔"
        u"\⚔"
        u"\❤️"
        u"\🧡"
        u"\🧵"
        u"\🦸‍♂🦸‍♀"
        
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

