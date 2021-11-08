

# The text that you want to convert to audio
mytext = 'your text to speak '

# Language in which you want to convert
language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file

myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")