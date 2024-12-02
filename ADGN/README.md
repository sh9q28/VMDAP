# Augmented Data Generation Network(ADGN)
 
See [INSTALL.md](INSTALL.md) for the installation of dependencies required.

## Training

Modified the dataset rootpath in 
```
ADGN/VesselGen/Options/vessel_gen_former.yml
```
and run
```
sh train.sh
```
The training process uses Vessel Detail Enhancement Loss by default. You can also find the source code for this loss function VDE_Loss in the file

```
ADGN/basicsr/models/losses/losses.py
```

## Demo

To test the pre-trained Restormer models on vessel mask images, you can command line as following after changeing the checkpoint path:
```
python demo.py --task VesselGen --input_dir './demo/input/' --result_dir './demo/result/'
```


## Output Images
Output images could be found in "--result_dir" in demo.py.
