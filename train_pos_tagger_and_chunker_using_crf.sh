# Train a pos tagger and chunker using CRF++ toolkit on CoNLL data.
input_file=$1
pos_model=$2
chunk_model=$3
feature_file=$input_file".feats"
python create_features_for_crf_from_conll_pos_data.py --input $input_file --output $feature_file
crf_learn -c 1.5 -f 3 -p 6 template-for-pos $feature_file $pos_model
crf_learn -c 1.5 -f 3 -p 6 template-for-chunk $input_file $chunk_model
