import re

def variableName(name):

    m = re.search("^\d|[^\d\w_]", name)

    try:
        if m.group(0):
            return False
    except:
        return True

if __name__ == '__main__':
    print variableName("wwwww2222")