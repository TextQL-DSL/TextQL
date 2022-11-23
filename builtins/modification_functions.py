class ModdificationFunctions:

    def __init__(self) -> None:
        pass


    def toUpperCase(self, word: str) -> str:
        return str.upper(word)


    def toUpperCase(self, wordList: list[str]) -> list[str]:
        upperList = [str.upper(word) for word in wordList]

        return upperList


    def tolowerCase(self, word: str) -> str:
        return str.lower(word)


    def toLowerCase(self, wordList: list[str]) -> list[str]:
        lowerList = [str.lower(word) for word in wordList]

        return lowerList


    def wordSlice(self, word: str, length: int) -> str:
        return word[:length]

    
    def wordSlice(self, wordList: list[str], length: int) -> list[str]:
        slicedWords = [word[:length] for word in wordList]

        return slicedWords


    
    

