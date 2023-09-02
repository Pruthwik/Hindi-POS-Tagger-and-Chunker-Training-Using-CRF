"""Create features for CRF from conll pos data."""
from argparse import ArgumentParser


def read_lines_from_file(file_path):
    """Read lines from a file."""
    with open(file_path, 'r', encoding='utf-8') as file_read:
        return file_read.readlines()


def find_sentences_in_text(lines):
    """Find sentences in conll lines."""
    temp_line, sentences = [], []
    for line in lines:
        line = line.strip()
        if line:
            temp_line.append(line)
        else:
            if temp_line:
                sentences.append('\n'.join(temp_line))
            temp_line = []
    if temp_line:
        sentences.append('\n'.join(temp_line))
        temp_line = []
    print(len(sentences))
    return sentences


def read_file_and_find_features_from_sentences(file_path):
    """Read a file and find features from sentences in the text."""
    features_string = ''
    lines = read_lines_from_file(file_path)
    sentences_found = find_sentences_in_text(lines)
    features_string = find_features_from_sentences(sentences_found)
    return features_string


def find_features_from_sentences(sentences):
    """Find features from sentences."""
    prefix_len = 4
    suffix_len = 7
    features = ''
    for sentence in sentences:
        sentence_features = ''
        for line in sentence.split('\n'):
            if line:
                token = line.split('\t')[0]
                tag = line.split('\t')[1]
                sentence_features += token + '\t'
                for i in range(1, prefix_len + 1):
                    sentence_features += affix_feats(token, i, 0) + '\t'
                for i in range(1, suffix_len + 1):
                    sentence_features += affix_feats(token, i, 1) + '\t'
                sentence_features = sentence_features + 'LESS\t' if len(token) <= 4 else sentence_features + 'MORE\t'
                sentence_features += tag.replace('__', '_').replace('-', '_') + '\n'
        if sentence_features.strip():
            features += sentence_features + '\n'
    return features


def affix_feats(token, length, type_aff):
    """Find affix features."""
    if len(token) < length:
        return 'NULL'
    else:
        if type_aff == 0:
            return token[:length]
        else:
            return token[len(token) - length:]


def write_file(data, out_path):
    """Write text to a file."""
    with open(out_path, 'w', encoding='utf-8') as fout:
        fout.write(data)


def main():
    """Pass arguments and call functions here."""
    parser = ArgumentParser()
    parser.add_argument('--input', dest='inp', help="Add the input path from where tokens and its features will be extracted")
    parser.add_argument('--output', dest='out', help="Add the output file where the features will be saved")
    args = parser.parse_args()
    features_extracted = read_file_and_find_features_from_sentences(args.inp)
    write_file(features_extracted, args.out)


if __name__ == '__main__':
    main()
