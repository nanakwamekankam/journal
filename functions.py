import os


def get_full_pathname(name):

    filename = os.path.abspath(os.path.join('' + name + '.rtf'))

    return filename


def load(name):
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):

    filename = get_full_pathname(name)
    print("...saving to {}.".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def list_entries(data):
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("{}. {}".format(idx+1, entry))


def enter(data):
    text = input("Enter text: ")
    data.append(text)
