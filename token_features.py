def affix_feats(token, length, type_aff):
    """Find affix features."""
    if len(token) < length:
        return 'NULL'
    else:
        if type_aff == 0:
            return token[:length]
        else:
            return token[len(token) - length:]


prefix_len = 4
suffix_len = 7
token_features = ''
token = 'दियें'
print(len(token))
print('Prefix')
for i in range(1, prefix_len + 1):
    print(i, affix_feats(token, i, 0))
    token_features += affix_feats(token, i, 0) + '\t'
print(token_features)
print('Suffix')
for i in range(1, suffix_len + 1):
    print(i, affix_feats(token, i, 1))
    token_features += affix_feats(token, i, 1) + '\t'
token_features = token_features + 'LESS\t' if len(token) <= 4 else token_features + 'MORE\t'
print(token_features)
