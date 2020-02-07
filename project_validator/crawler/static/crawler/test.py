import re


def replace_dangling_unicode(content):
    replacement_dict = {
        "\\\\u2010": "-", "\\\\u2011": "-", "\\\\u2012": "-", "\\\\u2013": "-", "\\\\u2014": "-", "\\\\u2015": "-",
        "\\\\u2016": "", "\\\\u2017": "", "\\\\u2018": "\'", "\\\\u2019": "\'", "\\\\u201c": "\"", "\\\\u201d": "\"",
    }
    regex = re.compile("(%s)" % "|".join(map(re.escape, replacement_dict.keys())))
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], content)


print(ascii(replace_dangling_unicode("blah blasdfkjqhw friends\u2019s")))
