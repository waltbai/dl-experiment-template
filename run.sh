# run in background
nohup python scripts/train.py --config config/default.yml --device cuda:0 > temp.log 2>&1 &