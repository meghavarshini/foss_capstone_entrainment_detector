## Code for pre-processing sound and transcript files from the ASIST3 dataset

Workflow:
- Save the entrainment trials (both .wav files and transcripts). Use `./Asist3_data_management/transcripts` if you wish to use the code's default paths.
- Run `asist3_transcript_manage.py` to extract utterances and other information from the transcripts
- Run `generate_dyads.py` on the output fromt eh previous step (saved to `.../transcripts/files_for_pipeline` by default) to extract conversational dyads from three-party conversations
- Use `create_h5_asist3.py` to create files for testing the pre-trained model on
- Finally, run `test.py` to generate the results for classification accuracy with the baseline model
