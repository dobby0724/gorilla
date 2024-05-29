#!/bin/bash

cd eval_checker
python3 ./eval_runner.py --model-type "meta-llama/Meta-Llama-3-8B-Instruct" --test-category simple relevance parallel_function multiple_function parallel_multiple_function java javascript
