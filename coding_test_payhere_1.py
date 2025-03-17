# 과제1. example.txt 파일에서 아래의 요구사항에 맞는 파이썬 코드를 작성하시오.

# 1. 전체 내용에서 Rebecca 라는 단어가 몇번 나오는지 세는 가장 효율적인 파이썬 코드를 작성하시오.
with open('example.txt', 'r', encoding='utf-8') as f:
    example = f.read()
    count = example.count('Rebecca')
    print(f"1. 해당 문서에서 'Rebecca'라는 단어는 {count}번 나옵니다.")


# 2. 4글자 이상의 단어 중, 가장 많이 나온 단어(case-insensitive) Top 5를 추출하는 가장 효율적인 파이썬 코드를 작성하시오.
from collections import Counter

with open('example.txt', 'r', encoding='utf-8') as f:
    example = f.read()

    # 단어 정리
    words = []
    for word in example.split():
        clean_word = ''.join([char for char in word if char.isalpha() or char == "'"])  # 알파벳과 '만 남김
        split_words = clean_word.split("'")  # '로 단어 분리 (ex. Rebecca's 등의 단어도 Rebecca에 포함시키기 위함)
        words.extend(split_words)

    # 소문자 변환 & 4글자 이상 단어 추출
    words = [word.lower() for word in words if len(word) >= 4]

    # 빈도 계산
    word_counts = Counter(words)
    top_5 = word_counts.most_common(5)

    print(f"2. 4글자 이상의 단어 중, 가장 많이 나온 단어 5개는 {top_5}입니다")
