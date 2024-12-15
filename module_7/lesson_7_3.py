class WordsFinder:

    def __init__(self, *names):
        self.file_names = names

    def get_all_words(self):
        all_words = {}
        for i in range(len(self.file_names)):
            text = []
            with open(self.file_names[i], 'r', encoding='utf-8') as file:
                line = file.read().lower()
                line.replace(',', ' ')
                line.replace('.', ' ')
                line.replace('=', ' ')
                line.replace('!', ' ')
                line.replace('?', ' ')
                line.replace(';', ' ')
                line.replace(':', ' ')
                line.replace(' - ', ' ')
                text = line.split()
                all_words.update({self.file_names[i] : text})
        return all_words

    def find(self, word):
        counter = 0
        for name, words in self.get_all_words().items():
            for i in words:
                counter += 1
                if i.lower() == word.lower():
                    return  {name : counter}


    def count(self, word):
        counter = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if i.lower() == word.lower():
                    counter += 1
        return {name : counter}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего