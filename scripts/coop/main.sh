#!/bin/bash

# custom config
DATA='$DATA'
TRAINER=CoOp

DATASET=$1
CFG=$2  # config file
CTP=$3  # class token position (end or middle)
NCTX=$4  # number of context tokens
SHOTS=$5  # number of shots (1, 2, 4, 8, 16)
CSC=$6  # class-specific context (False or True)
PROMPTS=$7

# for SEED in 1 2 3
# do
#     DIR=output/${DATASET}/${SHOTS}shots/${RUN}run/${PROMPTS}prompts/seed${SEED}/
#     if [ -d "$DIR" ]; then
#         echo "Oops! The results exist at ${DIR} (so skip this job)"
#     else
#         python train.py \
#         --root ${DATA} \
#         --seed ${SEED} \
#         --trainer ${TRAINER} \
#         --dataset-config-file configs/datasets/${DATASET}.yaml \
#         --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
#         --output-dir ${DIR} \
#         TRAINER.COOP.N_CTX ${NCTX} \
#         TRAINER.COOP.CSC ${CSC} \
#         TRAINER.COOP.CLASS_TOKEN_POSITION ${CTP} \
#         TRAINER.COOP.PROMPTS ${PROMPTS} \
#         DATASET.NUM_SHOTS ${SHOTS}
#     fi
# done

# TEST COMPLETO
for RUN in $(seq 1 3);
do
    for PROMPTS in 1 2 4 8 16 32
    do
        for SEED in 1 2 3
        do
            DIR=output/${DATASET}/${SHOTS}shots/${RUN}run/${PROMPTS}prompts/seed${SEED}
            if [ -d "$DIR" ]; then
                echo "Oops! The results exist at ${DIR} (so skip this job)"
            else
                python train.py \
                --root ${DATA} \
                --seed ${SEED} \
                --trainer ${TRAINER} \
                --dataset-config-file configs/datasets/${DATASET}.yaml \
                --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
                --output-dir ${DIR} \
                TRAINER.COOP.N_CTX ${NCTX} \
                TRAINER.COOP.CSC ${CSC} \
                TRAINER.COOP.CLASS_TOKEN_POSITION ${CTP} \
                TRAINER.COOP.PROMPTS ${PROMPTS} \
                DATASET.NUM_SHOTS ${SHOTS}
            fi
        done
    done
done
