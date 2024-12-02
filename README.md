# VMDAP_Vascular_Morphology-Driven_Augmentation_Pipeline_for_Vessel_Segmentation

We sincerely thank the reviewers for their time and thoughtful feedback. Your insights have greatly improved the quality of this work, and we hope the open-source code will be a valuable resource for future research.


We have open-sourced the code files presented in this paper for peer review. 
We have organized this repository into the following main blocks:

- [Background Restoration Block (BRB)](Background_Restoration_Block)
- [Vessel Structure Feature Enhancement Block (VSFEB)](Vessel_Structure_Feature_Enhancement_Block)
- [Augmented Data Generation Network (ADGN)](ADGN)
- [DAclDice](DAclDice)

For detailed information on each block, please visit the corresponding folder. Background Restoration Block (BRB), Vessel Structure Feature Enhancement Block (VSFEB), Augmented Data Generation Network (ADGN), and DAcldice.

##Background Restoration Block (BRB)

We provide a background inpainting method based on the Drive dataset samples. The training inputs and training labels of the Drive dataset, as specified in the paper, are prepared in the following folders.

```
Background_Restoration_Block/train_input Background_Restoration_Block/train_label
```

You can synthesize the background with a vessel mask and background inpainting according to the following instructions.

```
cd Background_Restoration_Block
python bg_with_mask.py
```

```
python bg_inpainting.py
```


##Vessel Structure Feature Enhancement Block (VSFEB)

We provide examples of generating new vessel mask images by combining new vessel backgrounds with new vessel masks. Notably, this block also includes code for generating VDGN training data.

The data in the same-named subfolders of the Vessel Structure Feature Enhancement Block folder and the Background Restoration Block folder can be shared. To proceed with subsequent operations, you need to complete the background inpainting process and copy the relevant files into the Vessel Structure Feature Enhancement Block folder.

After this, you can generate training data for ADGN based on the current vascular segmentation dataset using the following command.

```
cd Vessel_Structure_Feature_Enhancement_Block
python inpainted_bg_with_texture_mask.py
```

After the ADGN training is completed, construct vascular mask images with new features as the input to ADGN in order to generate new vascular images using the following command.


```
python mask_expand_with_texture.py
```


##Augmented Data Generation Network (ADGN)

We offer the code and training procedures for ADGN with proposed Vessel Detail Enhancement Loss. For more details, please refer to the README file in the folder.


##DAclDice
The DAclDice file contains the source code for the DAclDice Loss presented in the paper. To use it, you need to call the soft_dice_DAcldice class from the DAcldice.py file within the folder.

```
DAclDice/DAcldice.py
```

Thank you again to the reviewers for your careful review and constructive comments. Your feedback has been invaluable, and I hope this open-source code will contribute to further advancements in the field.
