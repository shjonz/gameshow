# ![GameShow (2)](https://user-images.githubusercontent.com/81726240/236750476-c56a3e3b-da98-48da-bdc3-eb34745125dc.png)

10.014 Computational Thinking for Design Project

## Features

- Multiplayer Text interface game
- 3 stages of gameplay, quiz, hangman and time based quiz
- Easy to install

## Overview
This game is similar to game shows where competing contestants gain points by answering questions. 

There are 3 stages of questions to answer in the game.

![1](https://user-images.githubusercontent.com/81726240/236749822-bb5149b9-4cd6-40fa-8fc7-10b77e0c90b2.png)
![2](https://user-images.githubusercontent.com/81726240/236749862-790e5f88-a240-46ea-9c40-b445d8c37e6d.png)
At the top we start out with the 3 different users who will enter their names. After a few seconds, the prompter will load stage 1 which is a series of multiple choice questions. If the contestant chooses the right answer, he will be awarded the points accordingly, else the question will be given to the next player

![3](https://user-images.githubusercontent.com/81726240/236749954-b3c08c99-9382-4ce6-846a-eae78e5cb23c.png)
In this picture, stage 2 starts, this round is a round of hangman. Guessing the correct letter will reveal how many lives the player has to live and how many points left. The words are revealed when guessed correctly. Players who are eliminated will not make it to the 3rd stage. 

![4](https://user-images.githubusercontent.com/81726240/236750066-3bc62743-9322-4b5a-b60b-df06015b7152.png)
In this image, stage 3 starts where they undergo the same questions, however if they both answer correctly, the point is awarded by how fast the person selects the right answer. In the next image, we can see how long the person takes to enter the answer with respect to time.

![5](https://user-images.githubusercontent.com/81726240/236750146-d6b937c3-9bbd-4047-9dc0-2a3abb51425a.png)
![6](https://user-images.githubusercontent.com/81726240/236750166-3fef459f-3920-4ba9-aa2a-562ff1f0ed81.png)
Here the previous player answer the question in 0.8175 seconds and also we display the winner of the entire game. 


In this project, I learnt several new concepts:
1. object oriented programming
2. using classes for the players
3. learning to use python to interact with csv files

## Installation

Download the files
1. finalbackup2021.py
2. stage1.csv
3. stage2lesser.csv
4. stage3lesser.csv

```sh
run finalbackup2021.py
```

## Tech

Gameshow uses simple python modules:

- Random
- Time
- Csv
- Os

## Footer
icon taken from <a href="https://www.flaticon.com/free-icons/simon" title="simon icons">Simon icons created by Freepik - Flaticon</a>
