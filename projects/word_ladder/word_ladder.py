f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors

class Queue():
    def __init__(self):
        self.queue =[]
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def find_word_ladder(begin_word, end_word):
    visited = set()
    queue = Queue()
    queue.enqueue([begin_word])
    while queue.size() > 0:
        path = queue.dequeue()
        vert = path[-1]
        if vert not in visited:
            visited.add(vert)
            if vert == end_word:
                return path
            for neighbor in get_neighbors(vert):
                new_path = list(path)
                new_path.append(neighbor)
                queue.enqueue(new_path)


print(find_word_ladder("sail", "boat"))
