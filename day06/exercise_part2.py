import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    answers = input_txt.split('\n\n')
    total_sum = 0
    for answer in answers:
        diff_answers = {}
        for one_answer in answer.split():
            for question in one_answer:
                if diff_answers.get(question):
                    diff_answers[question] += 1
                else:
                    diff_answers[question] = 1
        answer_sum = [k for k, v in diff_answers.items() if v == len(answer.split())]
        total_sum += len(answer_sum)
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