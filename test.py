import  requests, \
        selenium, \
        webbrowser, \
        bs4, \
        string, \
        re


lowercase = 'The Brown Fox'
uppercase = 'the brown fox'


def repl_func(m):
    """process regular expression match groups for word upper-casing problem"""

    return {1 : m.group(1) + m.group(2).upper(),
           2 : m.group(1) + m.group(2).lower()

uppercase = re.sub("(^|\s)(\S)", repl_func, uppercase)
#lowercase = re.sub("(^|\s)(\S)", repl_func, lowercase)

print(uppercase)







