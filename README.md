# Domain Adaptation in Computer Vision Using Correlation Realignment (CORAL)

This research investigates the effectiveness of Domain Adaptation techniques in the field of Computer Vision. Specifically, it evaluates the performance of Deep CORAL (Correlation Alignment), a method designed to minimize domain shift by aligning the second-order statistics (covariances) of feature representations across different domains.


## How this model works:

The CORAL CNN builds off of the ResNet-18 model, implementing CORAL Loss as a loss function. The loss function measures the distance between two second-order statistics (covariances) in a multi-dimensional plane. These two covariance matrices are called source and target, where the model aims to minimize this distance by tuning the model to extract the features equivalent to the target.

The CORAL function is as follows:

$$
\documentclass{article}
\usepackage{amsmath}

\begin{document}

\section*{CORAL Loss}

The CORAL (Correlation Alignment) loss is defined as:

\begin{equation}
\mathcal{L}_{\text{CORAL}} = \frac{1}{4d^2} \left\| C_S - C_T \right\|_F^2
\end{equation}

where:
\begin{itemize}
  \item \( C_S \in \mathbb{R}^{d \times d} \) is the covariance matrix of the source features,
  \item \( C_T \in \mathbb{R}^{d \times d} \) is the covariance matrix of the target features,
  \item \( \|\cdot\|_F \) denotes the Frobenius norm,
  \item \( d \) is the dimensionality of the feature representations.
\end{itemize}

The covariance matrix \( C \) for a domain with feature matrix \( X \in \mathbb{R}^{n \times d} \) (with \( n \) samples) is computed as:

\begin{equation}
C = \frac{1}{n - 1} (X^\top X - \frac{1}{n} (X^\top \mathbf{1}) (X^\top \mathbf{1})^\top)
\end{equation}

where \( \mathbf{1} \in \mathbb{R}^{n \times 1} \) is a column vector of ones.

\end{document}
$$
