#!/bin/bash

python3 openfunctions_evaluation.py --model /raid/channel/pretrained_models/Meta-Llama-3-70B-Instruct --model-type "meta-llama/Meta-Llama-3-70B-Instruct" --test-category all


cd eval_checker
python3 ./eval_runner.py --model pretrained_models_Meta-Llama-3-70B-Instruct --model-type "meta-llama/Meta-Llama-3-70B-Instruct" --test-category simple relevance parallel_function multiple_function parallel_multiple_function java javascript
