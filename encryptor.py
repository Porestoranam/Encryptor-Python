import argparse
import encode_and_decode
import pickle
import hack_and_train


def get_args(args):
    arguments = {}
    if args.method == 'train':
        if args.text_file is not None:
            with open(args.text_file, 'r') as file:
                text_for_train = file.read()
        else:
            text_for_train = input()
        arguments['text_for_train'] = text_for_train

    else:
        if args.method == 'hack':
            with open(args.model_file, 'rb') as file:
                ideal_allocation_in_model = pickle.load(file)
            arguments['ideal_allocation_in_model'] = ideal_allocation_in_model
        input_ = None
        output = None
        if args.input_file is not None:
            with open(args.input_file) as file:
                input_ = file.read()
        else:
            input_ = input()

        if args.output_file is not None:
            output = args.output_file
        arguments['input'] = input_
        arguments['output'] = output
    return arguments


def write_text(cur_answer_text, arguments):
    if answer_text is None:
        return
    else:
        if arguments['output'] is None:
            print(answer_text)
        else:
            with open(arguments['output'], 'w') as file:
                file.write(cur_answer_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers()

    encode_parser = subs.add_parser('encode', description='Encode this object')
    encode_parser.set_defaults(method='encode')
    encode_parser.add_argument('--cipher', required=True, help='cipher')
    encode_parser.add_argument('--key', required=True, help='Key')
    encode_parser.add_argument('--input-file', required=False)
    encode_parser.add_argument('--output-file', required=False)

    decode_parser = subs.add_parser('decode', description='Decode this object')
    decode_parser.set_defaults(method='decode')
    decode_parser.add_argument('--cipher', required=True, help='cipher')
    decode_parser.add_argument('--key', required=True, help='Key')
    decode_parser.add_argument('--input-file', required=False)
    decode_parser.add_argument('--output-file', required=False)

    train_parser = subs.add_parser('train', description='Learn using text')
    train_parser.set_defaults(method='train')
    train_parser.add_argument('--text-file', required=False, help='Text to learn')
    train_parser.add_argument('--model-file', required=True, help='help to count')

    hack_parser = subs.add_parser('hack', description='hack text')
    hack_parser.set_defaults(method='hack')
    hack_parser.add_argument('--input-file', required=False, help='string from')
    hack_parser.add_argument('--output-file', required=False, help='write there')
    hack_parser.add_argument('--model-file', required=True, help='Text to learn')

    args = parser.parse_args()
    user_args = get_args(args)

    answer_text = None

    if args.method == 'encode':
        if args.cipher == 'caesar':
            answer_text = encode_and_decode.caesar_encode_string(user_args['input'], int(args.key))
        elif args.cipher == 'vigenere':
            answer_text = encode_and_decode.vigenere_encode_and_decode(user_args['input'], args.key, 'encode')

    elif args.method == 'decode':
        if args.cipher == 'caesar':
            answer_text = encode_and_decode.caesar_decode_string(user_args['input'], int(args.key))

        elif args.cipher == 'vigenere':
            answer_text = encode_and_decode.vigenere_encode_and_decode(user_args['input'], args.key, 'decode')

    elif args.method == 'hack':
        answer_text = hack_and_train.changed_text(user_args['input'], user_args['ideal_allocation_in_model'])

    elif args.method == 'train':
        allocation_in_model = hack_and_train.count_ideal_allocation(user_args['text_for_train'])
        with open(args.model_file, 'wb') as file:
            pickle.dump(allocation_in_model, file)

    write_text(answer_text, user_args)
