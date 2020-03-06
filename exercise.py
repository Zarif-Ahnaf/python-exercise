
def repeat_stuff(stuff,num_repeats=10):
  return stuff * num_repeats

repeat_stuff("Row ", 3)
new_string = "Your Boat. "

lyrics = repeat_stuff("Row ",3) + new_string

song = repeat_stuff(lyrics)

print(song)
