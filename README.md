# retinopathy-desktop

Implementation of the diabetic retinopathy screening project in desktop form. (GTK)

Diabetic retinopathy screening w/ Tensorflow

Diabetic retinopathy is one of the leading causes of blindness in the the world and affects up to 40% of diabetic patients, with nearly 100 million cases worldwide as of 2010. However, with proper detection and treatment, the effects of diabetic retinopathy can be properly addressed. For people who are diabetic but are unable to visit an optometrist, due to lack of proper healthcare infrastructure, diagnosing this dangerous condition is often difficult, costly, and time consuming. Additionally, offering a way to more quickly detect diabetic retinopathy in a primary care setting would save time and money as well. Using the freely available machine learning software library Tensorflow, this experiment aims to allow a computerized, preliminary detection based on the retinal image of a patient's eye. This Tensorflow-based implementation uses convolutional neural networks to take a retinal image, analyze it, and learn the characteristics of an eye that shows signs of diabetic retinopathy in order to detect this condition in a primary care setting.

To run, install Tensorflow and the associated GTK environment dependencies. Then run `python3 retinopathy-app.py` followed by a picture directory (something like `/home/user/Pictures/retinopathy.jpg`). After the script is in memory, you can use the built in folder function to find other images. 

Images used to train Tensorflow are from Kaggle's Diabetic Retinopathy detection challenge: https://www.kaggle.com/c/diabetic-retinopathy-detection

Main repository here: https://github.com/Nomikxyz/diabetic-retinopathy-screening

Note: This is not to be used in any situation other than software testing. This should not be used in any medical circumstances. We are not responsible for any damage that occurs with use of this project. 

# Dependencies

- Tensorflow
- Diabetic Retinopathy image dataset
- GTK dependencies (GLADE, etc.)
