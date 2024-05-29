#!/bin/bash

# 여러 디렉토리를 입력받습니다.
echo "CHECKPOINT_DIRS (여러 디렉토리를 콤마로 구분하여 입력):"
read CHECKPOINT_DIRS

# 콤마로 구분된 디렉토리 목록을 배열로 변환합니다.
IFS=',' read -r -a DIR_ARRAY <<< "$CHECKPOINT_DIRS"

# 각 디렉토리에 대해 루프를 돌립니다.
for CHECKPOINT_DIR in "${DIR_ARRAY[@]}"; do
  for checkpoint_folder in "$CHECKPOINT_DIR"/checkpoint*; do
    echo "Processing checkpoint folder: $checkpoint_folder"
    python3 openfunctions_evaluation.py --model "$checkpoint_folder" --model-type "meta-llama/Meta-Llama-3-8B-Instruct" --test-category all
  done
done

cd eval_checker
python3 ./eval_runner.py --model-type "meta-llama/Meta-Llama-3-8B-Instruct" --test-category simple relevance parallel_function multiple_function parallel_multiple_function java javascript
