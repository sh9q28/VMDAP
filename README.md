# VMDAP_Vascular_Morphology-Driven_Augmentation_Pipeline_for_Vessel_Segmentation

We have open-sourced the code files presented in this paper for peer review. 
We have organized this repository into the following main blocks:

- [Background Restoration Block (BRB)](Background_Restoration_Block)
- [Vessel Structure Feature Enhancement Block (VSFEB)](Vessel_Structure_Feature_Enhancement_Block)
- [Augmented Data Generation Network (ADGN)](ANGN)
- [DAclDice](DAclDice)

For detailed information on each block, please visit the corresponding folder. Background Restoration Block (BRB), Vessel Structure Feature Enhancement Block (VSFEB), Augmented Data Generation Network (ADGN), and DAcldice.

In the Background Restoration Block (BRB), we provide a background inpainting method based on the Drive dataset samples, which is used to generate background images without blood vessels.

In the Vessel Structure Feature Enhancement Block (VSFEB), we provide examples of generating new vessel mask images by combining new vessel backgrounds with new vessel masks. Notably, this block also includes code for generating VDGN training data.

In the Augmented Data Generation Network (ADGN), we offer the code and training procedures for ADGN. For more details, please refer to the README file in the folder.

The DAclDice file contains the source code for the DAclDice Loss presented in the paper. To use it, you need to call the soft_dice_DAcldice class from the DAcldice.py file within the folder.
