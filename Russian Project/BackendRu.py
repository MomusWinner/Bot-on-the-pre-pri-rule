import requests
from Definition import SearchWordDefinition


class Grammar:
    def __init__(self, word: str, letterToCheck1: str, letterToCheck2: str):
        self.word = word
        self.letterToCheck1 = letterToCheck1
        self.letterToCheck2 = letterToCheck2
        self.number = 0

    def _CheckForExistence(self, _word) -> bool:
        _word += "\n"
        with open('russian.txt', 'r', encoding="utf-8") as ru:
            a = ru.readlines()
            if _word in a:
                return True
            else:
                return False

    def _Replacement(self, _word: list, value) -> str:
        n = 0
        wordList_word = _word.copy()
        for i in wordList_word:
            if i == "_":
                wordList_word.remove("_")
                wordList_word.insert(n, value)
                self.number = n
                return "".join(wordList_word)

            n += 1
        return "underscore not found"

    def _HighlightingALostLetter(self, _word) -> str:
        _wordList = list(_word)
        _wordList[self.number] = _wordList[self.number].upper()
        return "".join(_wordList)

    def FindTheRightWord(self):
        self.word = list(self.word)
        modifiedWord1 = self._Replacement(self.word, self.letterToCheck1)
        modifiedWord2 = self._Replacement(self.word, self.letterToCheck2)

        if modifiedWord1 != "underscore not found":
            if self._CheckForExistence(modifiedWord1) and self._CheckForExistence(modifiedWord2):
                return 'В данном слове написение ПРЕ- и ПРИ- зависит от значения слова.\n' \
                       'Значение данного слова с приставками ПРЕ- и ПРИ-:\n'\
                       + f'{SearchWordDefinition(modifiedWord1, 210)} \n {SearchWordDefinition(modifiedWord2, 210)}'

            elif self._CheckForExistence(modifiedWord1):
                return self._HighlightingALostLetter(modifiedWord1)
            elif self._CheckForExistence(modifiedWord2):
                return self._HighlightingALostLetter(modifiedWord2)
        return "Ошибка: Слово не распознано"


if __name__ == "__main__":

    a = Grammar('пр_емник', 'и', 'е')
    print(a.FindTheRightWord())

