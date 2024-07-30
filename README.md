# Paraphrased Essay Detector Application

This repository contains the implementation of a web-based application designed to detect paraphrased essays using word embedding techniques and classification algorithms. The application is developed using the Python Django framework.

## Abstract

With the rapid development of artificial intelligence, tools like QuiltBot AI, ChatGPT, Bing AI, and Google Bard can rewrite essays, potentially deceiving plagiarism detection systems. These rewritten essays, often not representing original thoughts, can claim the work of others as their own. Simple similarity checks are insufficient due to vocabulary changes, making more advanced methods necessary.

## Approach

This project leverages word embedding and classification algorithms to detect paraphrased essays. The techniques used include:
- **Word Embedding**: word2vec and fastText
- **Classification Algorithms**: Support Vector Machine (SVM) and Logistic Regression

## Methodology

1. **Data Collection**: English scientific papers on Informatics from the ScienceDirect website.
2. **Data Cleaning**: Removal of equations, tables, and reference lists.
3. **Paraphrasing**: Using Azure Open AI's GPT-3.5 Turbo model to create paraphrased versions of the papers.
4. **Model Building**: Developing word embedding models from both original and paraphrased papers and converting them into numerical data for classification model training.
5. **Model Selection**: The best word embedding model (word2vec) and the best classification model (Logistic Regression) were selected based on evaluation metrics.
6. **Integration**: The models were integrated into a web-based application using the Django framework.

## Results

- **Word2vec Model**: Relatedness value of 0.2426.
- **Logistic Regression Model**: 
  - Accuracy: 0.922
  - Precision: 0.923
  - Recall: 0.923
  - F1-Score: 0.923
  - AUC: 0.976

These results indicate that the models can predict paraphrased essays with a low error rate of 7.8%.

## Keywords

- Paraphrased Essay
- Word Embedding
- Word2vec
- FastText
- Support Vector Machine
- Logistic Regression
