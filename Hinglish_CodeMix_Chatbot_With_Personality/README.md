# Code-Mixed Personality Chatbot
 Varun Lalwani and Aman Gupta<br>
 CS 591: NLP<br>
 Professor Wijaya<br>

<h2>Usage</h2>

Step 1: create a data folder in your project directory, download
the Cornell Movie-Dialogs Corpus from
https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html
Unzip it

Step 2: update config.py file<br>
Change DATA_PATH to where you store your data

Step 3: python3 data.py<br>
This will do all the pre-processing for the Cornell dataset.

Step 4:
python3 chatbot.py --mode [train/chat] <br>
If mode is train, then you train the chatbot. By default, the model will
restore the previously trained weights (if there is any) and continue
training up on that.

If you want to start training from scratch, please delete all the checkpoints
in the checkpoints folder.

If the mode is chat, you'll go into the interaction mode with the bot.

By default, all the conversations you have with the chatbot will be written
into the file output_convo.txt in the processed folder. If you run this chatbot,
I kindly ask you to send me the output_convo.txt so that I can improve
the chatbot.


Thank you very much!

## Work Division
Varun: Worked on Data Extraction and Chatting Part
Aman: Worked on Train Model Part

## Results
These are our results after training the model:
#### Chatbot's Chatting after 600 iterations
![Image](./test_at_600_iters_chatbot.PNG)
#### Chatbot's Chatting after 1300 iterations
![Image](./test_at_1300_iters_chatbot.PNG)
#### Chatbot's Chatting after 2000 iterations
![Image](./test_at_2000_iters_chatbot.PNG)
#### Chatbot's Loss vs Iteration function
![Image](./chabot_iter_vs_loss.PNG)
