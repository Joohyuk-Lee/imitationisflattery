import multiprocessing
import os

class CFG:
  
  # Ref : https://github.com/ybabakhin/kaggle-feedback-effectiveness-1st-place-solution/blob/main/yaml/efficiency_model.yaml
  
  # ------------------- Architecture ------------------- # 
  aux_type = False
  backbone = "microsoft/deberta-v3-large
  dropout = 0.0
  gradient_checkpointing = False
  
  experiment_name = "exp_01"
  
  
  
  # ------------------- dataset ------------------- # 
  label_cols = ""
  
