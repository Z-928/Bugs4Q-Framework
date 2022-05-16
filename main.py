import argparse


def info(args):
    if args.repo and args.bug_id:
        path = f"./{args.repo}/{args.bug_id}/info_{args.bug_id}.csv"
        # print(path)
        import csv
        with open(path, 'r') as file:
            csv_file = csv.DictReader(file, delimiter=';')
            for row in csv_file:
                d = dict(row)
                formatted_info = f"\tBug id: {d['BugID']}\n\tURL: {d['Url']}\n\tBug type: {d['Bug-Type']}\n\tModfied part: ./{args.repo}/{args.bug_id}/{d['Mod']}"
                print(formatted_info)
    elif args.repo:
        import os
        l = os.listdir(f"./{args.repo}/")
        print(f"The total number of bugs in {args.repo}: {len(l)}")
    elif args.bug_id:
        print(
            "Please specify the repo name [qiskit...]:\nFormat: python main.py info -r repo_name -b bug_id")
    else:
        print(
            "Please specify the repo name [qiskit...] and bug id:\nFormat: python main.py info -r repo_name -b bug_id")


def checkout(args):
    if args.repo and args.bug_id and args.version and args.output:
        import os
        import shutil
        if not os.path.isdir(args.output):
            os.mkdir(args.output)
        else:
            print(f"./{args.output} exists.")
        if args.version == 'test':
            path1 = f"./{args.repo}/{args.bug_id}/test_b{args.bug_id}.py"
            path2 = f"./{args.repo}/{args.bug_id}/test_f{args.bug_id}.py"
            shutil.copy2(path1, args.output)
            shutil.copy2(path2, args.output)
            print(f"Test files are copied into directory: ./{args.output}")
        else:
            path = f"./{args.repo}/{args.bug_id}/{args.version}_{args.bug_id}.py"
            shutil.copy2(path, args.output)
            print(
                f"The {args.version} file is copied into directory: ./{args.output}")
    else:
        print(
            "Please specify the repo name, bug id and the version of the program[buggy, fixed, test]. Besides you can specify the location of the output using -o/--ouput directory_name.")


def run(args):
    print("run")
    if args.repo and args.bug_id and args.version:
        path = f"./{args.repo}/{args.bug_id}/{args.version}_{args.bug_id}.py"
        print(path)
        exec(open(path).read())
    else:
        print("Please specify repo name, bug id and version [buggy, fixed].")


def test(args):
    print("test")
    if args.repo and args.bug_id and args.version:
        if args.version == 'buggy':
            v = "b"
        else:
            v = "f"

        path = f"./{args.repo}/{args.bug_id}/test_{v}{args.bug_id}.py"

        print(path)

        print("start executing...")

        #import os
        #os.system(f'python3 {path}')
        exec(open(path).read())

    else:
        print("Please specify repo name, bug id and version [buggy, fixed].")


parser = argparse.ArgumentParser(
    description="A command-line inteface for Bugs4Q benchmark.")
subparsers = parser.add_subparsers(dest="sub_cmd", description="Four commands")

bug_id_help = "specify the id of the bug which you want to access"
repo_help = "specify the quantum programming platform [qiskit, Q#, Cirq...]"
version_help = "specify the version of the bug [buggy or fixed]"

parser_info = subparsers.add_parser(
    "info", help="print the information of a given bug.")
parser_info.add_argument("-b", "--bug_id", help=bug_id_help, type=int)
parser_info.add_argument("-r", "--repo", help=repo_help)
parser_info.set_defaults(func=info)

parser_checkout = subparsers.add_parser(
    "checkout", help="generate the source code (buggy version and fixed version) and test cases for a given bug. default location = current directory. You can use -o or --output to indicate the location of the files.")
parser_checkout.add_argument("-r", "--repo", help=repo_help)
parser_checkout.add_argument("-b", "--bug_id", type=int, help=bug_id_help)
parser_checkout.add_argument(
    "-v", "--version", choices=["buggy", "fixed", "test"], help=version_help)
parser_checkout.add_argument(
    "-o", "--output", help="the location of all generated files", default="./output")
parser_checkout.set_defaults(func=checkout)

parser_run = subparsers.add_parser("run", help="run the specified program.")
parser_run.add_argument("-r", "--repo", help=repo_help)
parser_run.add_argument("-b", "--bug_id", help=bug_id_help)
parser_run.add_argument(
    "-v", "--version", choices=["buggy", "fixed"], help=version_help)
parser_run.set_defaults(func=run)

parser_test = subparsers.add_parser(
    "test", help="run the tests for a given bug.")
parser_test.add_argument("-r", "--repo", help=repo_help)
parser_test.add_argument("-b", "--bug_id", type=int, help=bug_id_help)
parser_test.add_argument(
    "-v", "--version", choices=["buggy", "fixed"], help=version_help)
parser_test.set_defaults(func=test)

args = parser.parse_args()
args.func(args)
