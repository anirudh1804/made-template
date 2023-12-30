# Methods of Advanced Data Engineering Template Project

This project provides a structure for my open data project in the MADE module at FAU. This repository contains (a) a data science project that was developed by me over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).


## Project Work: Analyze the correlation between Co2 emissions and temperature in India during a certain period of time.
This data engineering project aims to determine whether Co2 emissions and temperature are related to each other or not.
The analysis is performed on the basis of a common base of time - year. Various statistical metrics and visualisation graphs are used to determine and depict the relation between both the factors.

This project aims to investigate the following aspects:
1. Is there any change in temperature between 2010 and 2017?
2. Is there any change in Co2 emissions between 2010 and 2017?
3. Is there any correlation between Co2 emmissions and temperatures during a certain time period?

As downloading and extracting the dataset was not possible directly. I have added the datasets in the 'data' folder. Please download my MADE project from github if you want to run my project.

All project work submissions are present in the `project` folder.

Insights to my project:
1. Link to my project report: 
2. Link to my project presentation video: [presentation-video.mp4](https://github.com/anirudh1804/made-template/blob/main/project/presentation-video.mp4)
3. Link to my project presentation slides: [slides.pdf](https://github.com/anirudh1804/made-template/blob/main/project/slides.pdf)

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv` or `./exercises/exercise1.py`
2. `./exercises/exercise2.jv` or `./exercises/exercise2.py`
3. `./exercises/exercise3.jv` or `./exercises/exercise3.py`
4. `./exercises/exercise4.jv` or `./exercises/exercise4.py`
5. `./exercises/exercise5.jv` or `./exercises/exercise5.py`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
