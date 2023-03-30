# Entrainment Detection for Two and Multi-Party Conversations

This is codebase for pre-processing the Multicats Dataset and running a pre-processed neural network model (trained on the Fisher English-1 Dataset) for detecting vocalic entrainment in spoken conversations. It uses sound files and transcripts to identify exchanges between pairs of players, extracts acoustic features using OpenSMILE, and finally runs the pre-trained model to check if the model can distinguish between dyads with the utterances in the correct order (preserved entrainable information) and those with utterances shuffled up (that is, without entrainable information).

1. Download the pre-trained model using: `wget https://kraken.sista.arizona.edu/tomcat/models/entrainment_baseline/`
2. Download the entrainment section of the Multicats dataset using: `ToDo`
3. Pre-process the ASIST3 dataset and use it for testing the entrainment baseline model, with scripts in the `Asist3_data_management` directory. Details for running the codebase are in a ReadME within the folder.
4. `Feats` contains all the code using for pre-processing the Fisher Dataset, as well as training the neural network model.
5. `Scripts` and `Praat_scripts` contain other scripts for pre-processing used for working with different extensions, and for structuring the transcript files.
