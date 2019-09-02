import configparser
import os
import sys


def unwrap_quotes(value):
    """Remove eventual quotes around the string."""
    QUOTE_CHARS = ["'", '"']
    if value and value[0] in QUOTE_CHARS and value[0] == value[-1]:
        value = value[1:-1]
    return value


def parse_ini_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError

    ini = configparser.ConfigParser()
    ini.read(filename)

    return ini


def extract_value(ini, section, key):
    try:
        ini_section = ini[section]
    except KeyError as e:
        print("Section '{}' doesn't exists".format(section), file=sys.stderr)
        raise e

    try:
        value = ini_section[key]
    except KeyError as e:
        print(
            "Key '{}' is section '{}' doesn't exists".format(key, section),
            file=sys.stderr,
        )
        raise e

    return value


def main():
    if len(sys.argv) < 4:
        print(
            "Usage: {} <filename> <section> <key>".format(
                os.path.basename(sys.argv[0])
            ),
            file=sys.stderr,
        )
        sys.exit(1)

    filename = sys.argv[1]
    section = sys.argv[2]
    key = sys.argv[3]

    try:
        ini = parse_ini_file(filename)
        value = extract_value(ini, section, key)
        print(unwrap_quotes(value))
    except KeyError:
        sys.exit(2)
    except FileNotFoundError:
        print(
            "Filename '{}' doesn't exists or is not a valid file".format(filename),
            file=sys.stderr,
        )
        sys.exit(3)
    except Exception as e:
        print("Unknown error: {}".format(e.__doc__), file=sys.stderr)
        sys.exit(4)


if __name__ == "__main__":
    main()
