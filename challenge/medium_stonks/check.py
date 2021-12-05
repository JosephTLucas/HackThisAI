import argparse


def check(path) -> bool:
    with open("setup/answers", "r") as f:
        answers = f.readlines()

    with open(path, "r") as f:
        submit = f.readlines()

    if answers == submit:
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    if check(args.path):
        print("Diamond Hands! FLAG{ILIKETHESTOCK}")
    else:
        print("Not quite the same")
