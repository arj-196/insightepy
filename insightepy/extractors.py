from typing import Dict

from insightepy.errors import InvalidParameterException


class Extractor(object):
    def _validate_params(self) -> None:
        pass

    def to_dict(self) -> Dict[str, str]:
        return dict(
            label=self.label,
            name=self.name,
        )


class NGram(Extractor):
    label = 'NGram'

    def __init__(self, name='ngram', n=3):
        self.name = name
        self.n = n
        self._validate_params()

    def _validate_params(self):
        if not isinstance(self.n, int):
            raise InvalidParameterException('n need to be of type integer')

    def to_dict(self):
        return dict(
            label=self.label,
            name=self.name,
            n=self.n
        )


class HashTag(Extractor):
    label = 'HashTag'

    def __init__(self, name='hashtag'):
        self.name = name
        self._validate_params()


class Mention(Extractor):
    label = 'Mention'

    def __init__(self, name='mention'):
        self.name = name
        self._validate_params()


class Url(Extractor):
    label = 'Url'

    def __init__(self, name='url'):
        self.name = name
        self._validate_params()


class Stemmer(Extractor):
    label = 'Stemmer'

    def __init__(self, name='stem'):
        self.name = name
        self._validate_params()


class Sentiment(Extractor):
    label = 'Sentiment'

    def __init__(self, name='sentiment'):
        self.name = name
        self._validate_params()


class POS(Extractor):
    label = 'POS'

    def __init__(self, name='pos'):
        self.name = name
        self._validate_params()


class Ontology(Extractor):
    label = 'Ontology'

    def __init__(self, name='ontology', from_feature='lem'):
        self.name = name
        self.from_feature = from_feature
        self._validate_params()

    def to_dict(self):
        return dict(
            label=self.label,
            name=self.name,
            from_feature=self.from_feature
        )


class Lemmer(Extractor):
    label = 'Lemmer'

    def __init__(self, name='lem', if_remove_stopwords=True, if_remove_noise=True):
        self.name = name
        self.if_remove_noise = if_remove_noise
        self.if_remove_stopwords = if_remove_stopwords
        self._validate_params()

    def to_dict(self):
        return dict(
            label=self.label,
            name=self.name,
            if_remove_noise=self.if_remove_noise,
            if_remove_stopwords=self.if_remove_stopwords
        )


class Keyword(Extractor):
    label = 'Keyword'

    def __init__(self, name='keyword'):
        self.name = name
        self._validate_params()
