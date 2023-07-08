# ColonTissueCNNClassifier-TransferLearning
This repository contains a transfer learning-based CNN classifier using fine-tuned AlexNet for accurate colon tissue image classification.

## Introduction:
In this report, we present the results of our code implementation focused on designing a CNN classifier for colon tissue image classification. The objective of this assignment was to employ transfer learning techniques by fine-tuning a pretrained AlexNet network on a colon tissue image dataset. To tackle this assignment, we used a pretrained model and applied it to our task. By fine-tuning the weights of a pretrained AlexNet, which has demonstrated remarkable performance on large-scale image classification challenges, we aimed to leverage its learned features for the specific task of colon tissue image classification. The implementation for this assignment was done using the Python programming language and the PyTorch deep learning framework. PyTorch provides a flexible and efficient platform for building and training neural networks.

## Utilizing pre-trained AlexNet:
To design our own classifier, we employed transfer learning by leveraging a pretrained AlexNet model. The pretrained AlexNet network was initially trained on a large-scale image classification task and had learned general features that could be relevant for our colon tissue image classification task.

## Input Size Compatibility:
To make the input size compatible with the AlexNet network, the input image will be first converted to the size 256×256 pixels and then cropped to the size 227×227 pixels as the AlexNet model require the input images with size 227×227.

## Input Normalization:
To ensure effective training, we normalized the input data. We applied standard normalization techniques by subtracting the mean of the dataset and dividing by the standard deviation. This normalization step helps to bring the input data to a similar scale, reducing the impact of varying image intensities. In our case, we calculated the mean and standard deviation values from the colon tissue image dataset and used those values for normalization.

## Modification of AlexNet Architecture:
We made modifications to the last fully connected layer of the AlexNet architecture to adapt it to our specific classification task. The original AlexNet model was designed for a different set of classes, so we replaced the last fully connected layer with a new layer that had the 3 output neurons corresponding to the number of classes in our colon tissue dataset. Also we used LogSoftmax with a dimension of 1 as the last layer.

## Loss Function:
For backpropagation, we employed the Negative Log-Likelihood Loss (NLLLoss) function. The NLLLoss function is commonly used for multi-class classification tasks, where each input sample is assigned to a single class. It measures the negative logarithm of the predicted probability of the correct class, encouraging the model to minimize the loss and improve its classification accuracy.

## Backpropagation Parameters and Optimizer:
To optimize the network's weights during backpropagation, we utilized an optimizer called Stochastic Gradient Descent (SGD). We selected the learning rate and momentum parameters for SGD through experimentation and hyperparameter tuning. These parameters control the step size during gradient descent, the influence of previous updates, and the regularization of the weights, respectively.

## Addressing Class-Imbalance Problem:
To address the class-imbalance problem, where certain classes have a significantly larger or smaller number of samples compared to others, we coded a script named “Aug.py” to augment images. To do so, we used oversampling method to generate new images from classes with smaller size. By doing this we could address the impact of class imbalance in our database.

# Visual Results:

<p align="center">
  <img src="https://github.com/AmirTabatabaei-git/ColonTissueCNNClassifier-TransferLearning/assets/132440248/cf6b5067-8d55-4237-91f5-2a6186285b3e">
</p>


<p align="center">
  <img src="https://github.com/AmirTabatabaei-git/ColonTissueCNNClassifier-TransferLearning/assets/132440248/52b122a2-fcb5-45c7-8905-2a352fef5609">
</p>



