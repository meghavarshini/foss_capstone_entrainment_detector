# Entrainment Detection for Two and Multi-Party Conversations

This is codebase for pre-processing the ASIST3 Dataset and running a pre-processed neural network model (trained on the Fisher English-1 Dataset) for detecting vocalic entrainment in spoken conversations. It uses sound files and transcripts to identify exchanges between pairs of players, extracts acoustic features using OpenSMILE, and finally runs the pre-trained model to check if the model can distinguish between dyads with the utterances in the correct order (preserved entrainable information) and those with utterances shuffled up (that is, without entrainable information).
