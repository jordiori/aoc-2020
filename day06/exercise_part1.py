import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    answers = input_txt.split('\n\n')
    total_sum = 0
    for answer in answers:
        diff_answers = set()
        for one_answer in answer.split():
            for question in one_answer:
                diff_answers.add(question)
        total_sum += len(diff_answers)
    return total_sum

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    if not args.input_file:
        raise ValueError('Missing input_file!')

    with open(args.input_file) as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()