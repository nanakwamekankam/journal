import journal


def print_header():
    print("------------------------------")
    print("        JOURNAL APP")
    print("------------------------------")
    print("")
    pass


def run_event_loop():
    journal_name = input("Journal Name: ")
    journal_data = journal.load(journal_name)

    cmd = None
    while cmd != 'x':
        cmd = input("What do you want to do? [L]ist, [E]nter, or E[x]it?: ")
        cmd = cmd.lower().strip()
        if cmd == 'l':
            journal.list_entries(journal_data)
        elif cmd == 'e':
            journal.enter(journal_data)

    print("DONE")

    journal.save(journal_name, journal_data)


def main():
    print_header()
    run_event_loop()


if __name__ = '__main__':
  main()
