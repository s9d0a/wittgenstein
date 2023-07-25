#단어 검색
import csv
import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

def process_csv_file(file_path):
    trie = Trie()

    if not os.path.exists(file_path):
        print("File does not exist.")
        return trie

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for cell_value in row:
                if cell_value:
                    words = cell_value.split()
                    for word in words:
                        trie.insert(word)

    return trie

def find_words(node, prefix, data_list):
    if node.is_end_of_word:
        data_list.append(prefix)
    for char, child in node.children.items():
        find_words(child, prefix + char, data_list)

# CSV 파일 경로 불러오기
file_path = '/content/drive/MyDrive/Colab Notebooks/scienceTopic.csv의 사본'

# CSV 파일 처리하여 트라이 구조 생성
trie = process_csv_file(file_path)

# 트라이에서 특정 키워드를 검색합니다.
search_keyword = input("검색할 키워드를 입력하세요: ")
node = trie.search(search_keyword)

if node is not None:
    print(f"'{search_keyword}'와(과) 관련된 데이터:")
    data_list = []
    find_words(node, search_keyword, data_list)
    for word in data_list:
        print(word)
else:
    print(f"'{search_keyword}'와(과) 관련된 데이터가 존재하지 않습니다.")
