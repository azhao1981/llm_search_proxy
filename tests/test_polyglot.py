# -*- coding: utf-8 -*-
from polyglot.detect import Detector
from polyglot.text import Text

if __name__ == '__main__':
    text = "สวัสดีครับ"
    detector = Detector(text)
    language_code = detector.language.code

    t = Text(text, hint_language_code=language_code)
    print(t.words)

    text = (
        "Japan's last pager provider has announced it will end its service in "
        "September 2019 - bringing a national end to telecommunication beepers, "
        "50 years after their introduction. Around 1,500 users remain subscribed "
        "to Tokyo Telemessage, which has not made the devices in 20 years."
    )
    print(Text(text).words)
