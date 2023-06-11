# Whatsapp_chat_analyzer
This is the link for demo of this project:  https://pallabpal-nlp-project-chat-analyzer-app-bpxbm9.streamlit.app/ ( copy and paste the link into the browser. Plesae don't use directly)
This project aims to extract important features from a WhatsApp chat text using regular expressions. It allows for the extraction of information such as names, messages, dates, and times from the chat, enabling further analysis both on a group level and individual level.

## Table of Contents
 1. Introduction
 2. Installation
 3. Usage
 4. Features
 5. Examples
## Introduction
Analyzing WhatsApp chat data can provide valuable insights into communication patterns, group dynamics, and individual behavior. This project provides a toolkit for extracting important features from a WhatsApp chat text file using regular expressions. By leveraging the power of regular expressions, it becomes possible to extract relevant information such as names, messages, dates, and times from the chat data.

The extracted features can then be used to perform various analyses on the chat data. This includes group-level analysis, such as identifying the most active participants, measuring the frequency of messages over time, or determining the sentiment of conversations. Additionally, individual-level analysis can be performed to gain insights into specific participants' contributions, engagement levels, or even language patterns.

## Installation
To use this project, follow these steps:

Clone the repository: git clone https://github.com/Pallabpal/nlp_project_chat_analyzer.git
Navigate to the project directory: cd whatsapp-chat-analysis
Install the required dependencies: pip install -r requirements.txt
## Usage
Place your WhatsApp chat text file in the project directory.
Modify the regular expressions in the extract_features.py file to match your chat's format and extract the desired features.
Run the script: python extract_features.py
The extracted features will be saved in a structured format, ready for further analysis.
## Features
The project currently supports the extraction of the following features from the WhatsApp chat text:

 1. Name: Extracts the name of the participant sending the message.
 2. Message: Extracts the content of the message.
 3. Date: Extracts the date of the message.
 4. Time: Extracts the time of the message.
 5. Day:  Extracts Day and Month of the message
You can customize the regular expressions in the extract_features.py file to match your specific chat format and extract additional features if needed.

## Examples
Here are a few examples of how you can leverage the extracted features:

 ## Group-Level Analysis:

Generate a word cloud to visualize the most frequently used words in the chat.
Calculate and compare the message count of different participants to identify the most active contributors.
Identify most busy user, most busy day, most frequently used word, Emoji analysis.
Plot the message frequency over time to identify patterns or periods of increased activity.

## Individual-Level Analysis:

Calculate the average message length for each participant to understand their communication style.
Identify specific keywords or phrases used by an individual participant.
These examples are just the tip of the iceberg. Feel free to explore further and adapt the analysis to your specific needs.


Happy analyzing! If you have any questions or need further assistance, please don't hesitate to contact us.






