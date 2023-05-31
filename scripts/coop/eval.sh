#!/bin/bash

# custom config
DATA='$DATA'
TRAINER=CoOp
SHOTS=16
NCTX=16
CSC=False
CTP=end

DATASET=$1
CFG=$2
PROMPTS=$3

for RUN in $(seq 1 3);
do
    for PROMPTS in 1 2 4 8 16 32
    do
        for SEED in 1 2 3
        do
            for (( i=0; i < PROMPTS; i++ ))
            do  
                python train.py \
                --root ${DATA} \
                --seed ${SEED} \
                --trainer ${TRAINER} \
                --dataset-config-file configs/datasets/${DATASET}.yaml \
                --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
                --output-dir output/single_logs/${DATASET}/${SHOTS}shots/${RUN}run/${PROMPTS}prompts/seed${SEED}/index${i} \
                --model-dir output/${DATASET}/${SHOTS}shots/${RUN}run/${PROMPTS}prompts/seed${SEED} \
                --load-epoch 50 \
                --eval-only \
                TRAINER.COOP.N_CTX ${NCTX} \
                TRAINER.COOP.CSC ${CSC} \
                TRAINER.COOP.CLASS_TOKEN_POSITION ${CTP} \
                TRAINER.COOP.TEST_INDEX ${i} \
                TRAINER.COOP.PROMPTS ${PROMPTS}
            done
        done
    done
done