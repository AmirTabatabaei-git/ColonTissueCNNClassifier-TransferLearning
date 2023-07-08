In this task, you will design a convolutional neural network (CNN) classifier for colon tissue image classification. For that, you will make use of transfer learning by finetuning the pretrained AlexNet network
on a colon tissue image dataset.

### **Implementation details**

Specify the platform that you used for your implementation.

Explain how you made use of the pretrained AlexNet to design your own classifier:

- How did you make the input size compatible with the AlextNet network?
- How did you normalize the input?
- What parts of the AlextNet architecture did you modify? How did you modify the last layer?
- What loss function did you use in backpropagation?
- How did you select the parameters related to backpropagation? For example, did you use any optimizers? If so, what were the parameters of this optimizer and how did you select their values?
- How did you address the class-imbalance problem?

You may want to use Google Colab to implement the code. Here are the instructions for **How to Use Google Colab**?

Google Colab allows you to write and execute Python code in your browser with no configuration required,
also with free access to GPUs. Training neural networks take shorter time on GPUs, so if you do not have
a machine with a GPU, you can use Google Colab. If you have used Jupyter Notebook before, you can think
of Google Colab as a Jupyter Notebook stored in Google Drive.

You may follow the following steps to run your codes on Google Colab:
- Go to your Google Drive.
- Upload the dataset for the homework to your Google Drive.
- Create a new Colab notebook by clicking on New → More → Google Colaboratory. The “new” button is on the top left corner, below the “Drive” logo.
- Write your code on the notebook.
- To use a GPU, click on “edit” at the bar above and then choose “notebook settings”. Choose the hardware accelerator as GPU and save changes.
- To use the dataset you uploaded to your Drive, you need to mount your Drive to Colab. To do that, add a new cell to your notebook by clicking on the “+ Code” button at the top and write the following
code in the cell and run it:

<p align="center">from google.colab import drive
<p align="center">drive.mount("/content/gdrive")

- Open the link.
- Choose your Google account.
- Allow access to your Google account.
- Copy the code and paste it in the text box, and press enter.
- While accessing the dataset, the directory address should start with "/content/gdrive/..."

