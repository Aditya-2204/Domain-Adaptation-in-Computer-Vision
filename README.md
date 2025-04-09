# Domain Adaptation in Computer Vision Using Correlation Realignment (CORAL)

This research investigates the effectiveness of Domain Adaptation techniques in the field of Computer Vision. Specifically, it evaluates the performance of Deep CORAL (Correlation Alignment), a method designed to minimize domain shift by aligning the second-order statistics (covariances) of feature representations across different domains.


## How this model works:

The CORAL CNN builds off of the ResNet-18 model, implementing CORAL Loss as a loss function. The loss function measures the distance between two second-order statistics (covariances) in a multi-dimensional plane. These two covariance matrices are called source and target, where the model aims to minimize this distance by tuning the model to extract the features equivalent to the target.

The CORAL function is as follows:

![CORAL Loss](https://latex.codecogs.com/png.image?\dpi{120}L_{CORAL}=\frac{1}{4d^2}\left\|C_S-C_T\right\|_F^2)
