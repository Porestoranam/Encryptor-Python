import argparse
import encode_and_decode
import pickle
import hack_and_train

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
if args.input_file is not None:
    with open(args.input_file) as file:
        input_ = file.read()
else:
    input_ = input()
if args.method == 'encode':
    if args.cipher == 'caesar':
        if args.output_file is not None:
            output = open(args.output_file, 'w')
            output.write(encode_and_decode.caesar_encode_string(input_, int(args.key)))
            output.close()
        else:
            print(encode_and_decode.caesar_encode_string(input_, int(args.key)))
    elif args.cipher == 'vigenere':
        if args.output_file is not None:
            output = open(args.output_file, 'w')
            output.write(encode_and_decode.vigenere_encode(input_, args.key))
            output.close()
        else:
            print(encode_and_decode.vigenere_encode(input_, args.key))

elif args.method == 'decode':
    if args.cipher == 'caesar':
        if args.output_file is not None:
            output = open(args.output_file, 'w')
            output.write(encode_and_decode.caesar_decode_string(input_, int(args.key)))
            output.close()
        else:
            print(encode_and_decode.caesar_decode_string(input_, int(args.key)))
    elif args.cipher == 'vigenere':
        if args.output_file is not None:
            output = open(args.output_file, 'w')
            output.write(encode_and_decode.vigenere_decode(input_, args.key))
            output.close()
        else:
            print(encode_and_decode.vigenere_decode(input_, args.key))

elif args.method == 'train':
    if args.text_file is not None:
        with open(args.text_file, 'r') as file:
            text_for_train = file.read()
    else:
        text_for_train = input()
    allocation_in_model = hack_and_train.count_ideal_allocation(text_for_train)
    pickle.dump(allocation_in_model, open(args.model_file, 'wb'))


elif args.method == 'hack':
    file = open(args.model_file, 'r')
    ideal_allocation_in_model = pickle.load(open(args.model_file, 'rb'))
    if args.output_file is not None:
        output = open(args.output_file, 'w')
        output.write(hack_and_train.answer(input_, ideal_allocation_in_model))
        output.close()
    else:
        print(hack_and_train.answer(input_, ideal_allocation_in_model))
