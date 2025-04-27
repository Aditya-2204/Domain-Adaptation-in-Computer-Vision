# Domain Adaptation in Computer Vision Using Correlation Realignment (CORAL)

This research investigates the effectiveness of Domain Adaptation techniques in the field of Computer Vision. This model uses [insert model name] for image classification. Specifically, it evaluates the performance of Deep CORAL (Correlation Alignment), a method designed to minimize domain shift by aligning the second-order statistics (covariances) of feature representations across different domains.

This research is an independent implementation of CORAL in Computer Vision

Original research paper by Sun & Saenko found [here](https://arxiv.org/pdf/1607.01719)

# Problem

In the real-life environment, models trained on one type of data (source domain) often perform poorly when used on different but related data (target domain) due to differences in data distribution, known as domain shift. This leads to poor classification

# Understanding of Domain Adaption

Domain Adaptation is a subfield of transfer learning that focuses on addressing the distributional discrepancy between a source domain (where labeled data is available) and a target domain (where labels are limited or unavailable). Traditional machine learning models assume that training and testing data are drawn from the same distribution. However, in real-world scenarios, this assumption often fails—especially when models are deployed in environments that differ from the training data. This leads to a performance drop due to the shift in data distributions, known as domain shift.

Domain adaptation techniques aim to mitigate this problem by aligning feature representations or distributions between the source and target domains. This enables models trained on the source domain to generalize well to the target domain.

# Why Domain Adaptation
Domain adaptation is important for computer vision because real-world applications often face a domain shift—a difference between the data a model was trained on and the data it encounters in practice. Domain Adaptation, specifically CORAL, prepares models for real-world usage by fixing the problem of domain shift. Domain Adaptation helps models generalize better over images in varying environments.

In the growing world of autonomous vehicles and medical imaging, In critical fields such as autonomous driving and medical imaging, even slight domain shifts—like changes in lighting, sensor type, or environmental conditions can lead to significant performance issues in computer vision systems, which can result in dangerous or life-threatening outcomes. An autonomous vehicle trained under sunny conditions may misinterpret objects when driving at night or in fog, while a diagnostic model trained on data from one hospital may fail to detect abnormalities when applied to images from a different clinic using different equipment. Domain adaptation addresses these issues by allowing models to adjust to new data distributions without requiring extensive manual labeling in the target domain.

## How this model works:

The CORAL CNN builds off of the ResNet-18 model, implementing CORAL Loss as a loss function. The loss function measures the distance between two second-order statistics (covariances) in a multi-dimensional plane. These two covariance matrices are called source and target. We aim to minimize this loss in order for the model to learn the domain-invariant features by aligning the feature extraction to be in the same environment as the target. In essence, the source images are in a different environment to the target images, however the model aims to perceive both of the sets the same by reducing the distance between their underlying features.

Full research paper found [here](https://drive.google.com/file/d/16Gz5mhpFM9PfxREZWrYSjC4fnOsGTwbf/view?usp=sharing)

# How to run
## Note: The code used for research is computationally intensive. It is recommended to use Google Colab.

The ```pip install``` commands are already on the notebook, however, for running locally:

```pip install -r requirements.txt```

And press run on the notebook
Any Questions: william1binki@gmail.com
