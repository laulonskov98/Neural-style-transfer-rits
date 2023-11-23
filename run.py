import subprocess


dir_path = "Neural-Style-Transfer"
NETWORK = 'INetwork.py'

# Image size
IMAGE_SIZE = 60

# Loss Weights
CONTENT_WEIGHT = 0.025
STYLE_WEIGHT = 1.0
STYLE_SCALE = 1.0
TOTAL_VARIATION_WEIGHT = 8.5e-5
CONTENT_LOSS_TYPE = 0

# Training arguments
NUM_ITERATIONS = 10
MODEL = 'vgg19'
RESCALE_IMAGE = 'false'
MAINTAIN_ASPECT_RATIO = 'false'  # Set to false if OOM occurs

# Transfer Arguments
CONTENT_LAYER = 'conv' + '5_2'  # only change the number 5_2 to something in a similar format
INITIALIZATION_IMAGE = 'content'
POOLING_TYPE = 'max'

# Extra arguments
PRESERVE_COLOR = 'false'
MIN_IMPROVEMENT = 0.0

RESULT_DIR = "generated/"
RESULT_PREFIX = RESULT_DIR + "gen"
path1 = "/home/laurits/Desktop/neural-transfer/1.jpg"
path2 = "/home/laurits/Desktop/neural-transfer/horse2.jpeg"

path3 = "/home/laurits/Desktop/neural-transfer/2.jpeg"
path4 = "/home/laurits/Desktop/neural-transfer/horse1.jpg" 

path5 = "/home/laurits/Desktop/neural-transfer/3.jpeg"
path6 = "/home/laurits/Desktop/neural-transfer/horse2.jpeg" 


command = f"""python3 {dir_path}/{NETWORK} {path1} {path2} {path3} {path4} {path5} {path6}  {RESULT_PREFIX} \
    --image_size {IMAGE_SIZE} --content_weight {CONTENT_WEIGHT} --style_weight \
    {STYLE_WEIGHT} --style_scale {STYLE_SCALE} --total_variation_weight \
    {TOTAL_VARIATION_WEIGHT} --content_loss_type {CONTENT_LOSS_TYPE} --num_iter \
    {NUM_ITERATIONS} --model {MODEL} --rescale_image {RESCALE_IMAGE} \
    --maintain_aspect_ratio 'true' --content_layer {CONTENT_LAYER} \
    --init_image {INITIALIZATION_IMAGE} --pool_type {POOLING_TYPE} --preserve_color \
    {PRESERVE_COLOR} --min_improvement {MIN_IMPROVEMENT}"""

result = subprocess.run(command, shell=True)

print("HEY")