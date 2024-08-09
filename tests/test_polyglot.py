# -*- coding: utf-8 -*-
from polyglot.detect import Detector
from polyglot.text import Text

if __name__ == '__main__':
    text = "สวัสดีครับ"
    detector = Detector(text)
    language_code = detector.language.code

    t = Text(text, hint_language_code=language_code)
    print(t.words)