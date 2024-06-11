import os
from tqdm import tqdm
import subprocess

def find_merged_subdirs(root_dir):
    merged_subdirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'merged' in dirnames:
            merged_dir = os.path.join(dirpath, 'merged')
            for subdir in os.listdir(merged_dir):
                subdir_path = os.path.join(merged_dir, subdir)
                if os.path.isdir(subdir_path):
                    merged_subdirs.append(subdir_path)
    return merged_subdirs

def main():
    path = "/raid/channel/dobby/function_calling/ckpts"
    dir_array = find_merged_subdirs(path)

    # 각 디렉토리에 대해 루프를 돌립니다.
    for checkpoint_dir in dir_array:
        save_base_path = os.path.join('result', '/'.join(checkpoint_dir.split('/')[-3:]).replace('/', '_'))
        if os.path.exists(save_base_path):
            print(f'Skipped {save_base_path} ckpt!')
            continue
        print(f"Processing checkpoint folder: {checkpoint_dir}")
        subprocess.run([
            'python3', 'openfunctions_evaluation.py',
            '--model', checkpoint_dir,
            '--model-type', 'meta-llama/Meta-Llama-3-8B-Instruct',
            '--test-category', 'all'
        ])

    os.chdir('eval_checker')
    subprocess.run([
        'python3', './eval_runner.py',
        '--model-type', 'meta-llama/Meta-Llama-3-8B-Instruct',
        '--test-category', 'simple', 'relevance', 'parallel_function', 
        'multiple_function', 'parallel_multiple_function', 'java', 'javascript'
    ])

if __name__ == '__main__':
    main()
