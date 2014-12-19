from mrjob.job import MRJob


class MRAnagram(MRJob):

    def mapper(self, _, line):
        letters = list(line)
        letters.sort()
        yield letters, line

    def reducer(self, key, words):
        anagrams = [w for w in words]
        if len(anagrams) > 1:
            yield len(anagrams), anagrams


if __name__ == '__main__':
    MRAnagram.run()