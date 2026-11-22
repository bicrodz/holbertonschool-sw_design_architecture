#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional, Protocol


class Observer(Protocol):

    def update(self, topic: str, data: str) -> None:
        ...


class NewsSubject:

    def __init__(self) -> None:
        self._observers: dict[Observer, Optional[set[str]]] = {}

    def subscribe(self, observer: Observer, topics=None) -> None:
        if observer in self._observers:
            return
        self._observers[observer] = None if topics is None else set(topics)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:

    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver:

    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver:

    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    subject = NewsSubject()
    log = LogObserver()
    email = EmailObserver()
    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)

    sms = SmsObserver()
    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
