export PYTHONPATH=$(pwd)

# local model infer
# CUDA_VISIBLE_DEVICES=4,5,6,7 python infer/infer.py --config config/config.yaml --split logic cipher counterfactual operation puzzle --mode zero-shot --model_name Qwen2.5-7B-Instruct --output_dir results --batch_size 250 --use_accel
# CUDA_VISIBLE_DEVICES=4,5,6,7 python infer/infer.py --config config/config.yaml --split lookfowarding --mode zero-shot --model_name Qwen2.5-7B-Instruct --output_dir results --batch_size 250 --use_accel

# API calls
# python infer/infer.py --config config/config.yaml --split logic cipher counterfactual operation puzzle --mode zero-shot --model_name gpt-4o --output_dir results --num_workers 16

python infer/infer.py --config config/config.yaml --split lookfowarding --mode zero-shot --model_name gpt-4o --output_dir results --num_workers 16