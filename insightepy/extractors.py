from typing import Dict

from insightepy.errors import InvalidParameterException


class FeatureTypes(object):
    CHUNK = u'chunk'
    KEYWORD = u'keyword'
    LEM = u'lem'
    TOKEN = u'token'
    STEM = u'stem'
    SENTIMENT = u'sentiment'
    NGRAM = u'ngram'
    ONTOLOGY = u'ontology'
    POS = u'pos'
    HASHTAG = u'hashtag'
    MENTION = u'mention'
    URL = u'url'
    EMOTION = u'emotion'


class Extractor(object):
    def _validate_params(self) -> None:
        pass

    def to_dict(self) -> Dict[str, str]:
        return dict(
            label=self.label,
            name=self.name,
        )


class NGram(Extractor):
    label = FeatureTypes.NGRAM

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
    label = FeatureTypes.HASHTAG

    def __init__(self, name='hashtag'):
        self.name = name
        self._validate_params()


class Mention(Extractor):
    label = FeatureTypes.MENTION

    def __init__(self, name='mention'):
        self.name = name
        self._validate_params()


class Url(Extractor):
    label = FeatureTypes.URL

    def __init__(self, name='url'):
        self.name = name
        self._validate_params()


class Stemmer(Extractor):
    label = FeatureTypes.STEM

    def __init__(self, name='stem'):
        self.name = name
        self._validate_params()


class Sentiment(Extractor):
    label = FeatureTypes.SENTIMENT

    def __init__(self, name='sentiment'):
        self.name = name
        self._validate_params()


class POS(Extractor):
    label = FeatureTypes.POS

    def __init__(self, name='pos'):
        self.name = name
        self._validate_params()


class Ontology(Extractor):
    label = FeatureTypes.ONTOLOGY

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
    label = FeatureTypes.LEM

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
    label = FeatureTypes.KEYWORD

    def __init__(self, name='keyword'):
        self.name = name
        self._validate_params()
