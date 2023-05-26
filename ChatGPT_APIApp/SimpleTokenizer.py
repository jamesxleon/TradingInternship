import re

class Stream:
    def __init__(self, title):
        self.title = title
        self.parts = []
        self.current_part_words = 0
        self.current_part = []

    def add_words(self, words):
        for word in words:
            if self.current_part_words + len(word.split()) > 1700:
                self.parts.append(' '.join(self.current_part))
                self.current_part = [word]
                self.current_part_words = len(word.split())
            else:
                self.current_part.append(word)
                self.current_part_words += len(word.split())

    def finalize(self):
        if self.current_part:
            self.parts.append(' '.join(self.current_part))

def parse_file(filename):
    with open(filename, 'r', encoding='cp1252') as file: #Here you should choose the right encoding for your text, this one worked for me 
        content = file.readlines()

    streams = []
    current_stream = None
    #counter = 0

    for line in content:
        line = line.strip()  # remove leading/trailing whitespace
        if line.startswith("Stream name:"):
            if current_stream is not None:
                current_stream.finalize()
                streams.append(current_stream)
                #counter += 1
            current_stream = Stream(line[len("Stream name:"):].strip())
        elif current_stream is not None and line != '':  # ignore blank lines
            current_stream.add_words(re.split(r'\s+', line))

    if current_stream is not None:
        current_stream.finalize()
        streams.append(current_stream)

    #print("Total streams: ", counter)
    return [{'title': stream.title, 'parts': stream.parts} for stream in streams]


#filename = 'transcripts.txt'  # replace with your filename
#parsed_data = parse_file(filename)
#for stream in parsed_data:
#    print(f'Title: {stream["title"]}')
#    for i, part in enumerate(stream["parts"]):
#        print(f'Part {i+1}: {part[:100]}...')  # print first 100 characters of each part

