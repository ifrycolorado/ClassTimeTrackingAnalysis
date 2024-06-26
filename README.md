# Available Data 🕒

### Full Semesters
| Semester (Report) | Per Work Type (png) | Per Day of Week (png) | Plaintext (txt)    | Dataset (csv) |
|-------------------|---------------|-----------------|--------------|-----------|
| [S2023](reports/S2023_Toggl.pdf) | ❌ Not tracked| ✅ [Available](images/S2023_per_day.png) | ✅ [Available](logs/S2023_raw_stats.txt) | ✅ [Available](data/S2023_cleaned.csv) |
| [F2023](reports/F2023_Toggl.pdf) | ✅ [Available](images/F2023_per_type.png)| ✅ [Available](images/F2023_per_day.png) | ✅ [Available](logs/F2023_raw_stats.txt) | ✅ [Available](data/F2023_cleaned.csv) | 
| [S2024](reports/S2024_Toggl.pdf) | ✅ [Available](images/S2024_per_type.png)| ✅ [Available](images/S2024_per_day.png) | ✅ [Available](logs/S2024_raw_stats.txt) | ✅ [Available](data/S2024_cleaned.csv) | 

### Individual Courses
  
  | Course Name (Report)                | Department | Code   | Semester | Per Work Type (png) |
  |-------------------------------------|------------|--------|----------|---------------|
  | [Software Engineering](reports/SOFTWARE-ENGINEERING_CSCI306_F2023.pdf)                | CSCI       | 306    | F2023    | ✅ [Available](images/course_SWE_F2023.png)|
  | [Computer Organization](reports/COMPUTER-ORGANIZATION_CSCI341_S2023.pdf)               | CSCI       | 341    | S2023    | ❌ Not tracked|
  | [Database Management](reports/DATABASE-MANAGEMENT_CSCI403_S2023.pdf)                 | CSCI       | 403    | S2023    | ❌ Not tracked|
  | [Algorithms](reports/ALGORITHMS_CSCI406_F2023.pdf)                          | CSCI       | 406    | F2023    | ✅ [Available](images/course_Algorithms_F2023.png)|
  | [Operating Systems](reports/OPERATING-SYSTEMS_CSCI442_F2023.pdf)                   | CSCI       | 442    | F2023    | ✅ [Available](images/course_OS_F2023.png)|
  | [Network Sciences](reports/NETWORK-SCIENCES_CSCI498D_S2024.pdf) | CSCI | 498D | S2024 | ✅ [Available](images/course_Network-Sciences_S2024.png)|
  | [Theory of Cryptography](reports/THEORY-OF-CRYPTOGRAPHY_CSCI574_S2024.pdf)  | CSCI       | 574    | S2024    | ✅ [Available](images/course_Cryptography_S2024.png)|
  | [Computing Beyond CPUs (Heterogeneous Computing)](reports/COMPUTING-BEYOND-CPUs_CSCI582_S2024.pdf) | CSCI | 582 | S2024 | ✅ [Available](images/course_Beyond-CPUs_S2024.png)|
  | [Principles of Chemistry I](reports/CHEMISTRY-I_CHGN121_S2023.pdf)           | CHGN       | 121    | S2023    | ❌ Not tracked|
  | [Music Technology](reports/MUSIC-TECHNOLOGY_HASS327_S2023.pdf)                    | HASS       | 327    | S2023    | ❌ Not tracked| 
  | [Explorations in Modern World](reports/EXPLORATION-IN-MODERN-WORLD_HNRS315_S2023.pdf)        | HNRS       | 315    | S2023    | ❌ Not tracked|
  | [McBride Practicum](reports/MY-PRACTICUM_HNRS405_S2024.pdf) | HNRS | 405 | ONGOING | ✅ [Available](images/course_Practicum---My-Practicum_S2024.png)|
  | [Generative AI and Graphic Novels](reports/GENAI-ART_HNRS435A_F2023.pdf)    | HNRS       | 435A   | F2023    | ✅ [Available](images/course_GenAI-&-Art.png)|
  | [Social Media and Misinformation](reports/SOCIAL-MEDIA-AND-MISINFORMATION.pdf) | HNRS | 445 | S2024 | ✅ [Available](images/course_Social-Media-and-Misinformation_S2024.png)|
  

Reports include individual assignment times _and_ time investments per semester. If you're looking for how long an assignment will relative to other assignments or when in a semester a course will require more time, that's where to look. They're pretty great. 

### Other Resources
* [Course information](data/ClassInfo.csv)
  * Can be joined to a semester dataset on [semester].Project == [classinfo].Toggl Name
* [Hours per credit per week](images/hours_per_credit.png)
  * Shows hours of non-lecture work per credit per week

# How I Track my Time

Since Spring of 2023, I've tracked my out-of-class time (i.e. everything except lectures) spent for each course I've taken. All of this was done through [Toggl](https://track.toggl.com/timer), which I thought was intuitive (and, most importantly, free). 

In Fall of 2023, I added tags that specified the type of work being done for a specific assignment.

* **Writing**: Any type of writing done that was not note-taking. This includes essays, discussions, presentations, and reports.
  * Any technical reports or analyses on code that I created are considered a type of writing.
  * Note-taking is not a type of writing.
* **Coding**: Any type of coding that is not a simple configuration task (like setting up an IDE).
* **Practice**: Any non-coding and non-note-taking work that increased my understanding of the material. This could also be considered Studying. 
  * All homework worksheets are considered a type of practice.
  * Any type of studying, including reviewing my notes, is a type of practice.
  * This category is intentionally broad and serves as a catch-all for ambiguous work. 
* **Reading**: Any note-taking activity. This includes watching videos and reading lesson materials.
* **Research**: Any type of open-ended, exploratory research.
  * This includes literature reviews, searching journal databases, etc.
  * This is not the same as reading. Reading distills content without the creation of new ideas, while research synthesizes topics and creates something new.
  * _Generally_, Writing is a separate activity from Research. However, there are some gray areas. Consider the act of writing an outline for a research paper: I will need to be searching for ideas (researching) while also structuring them logically (writing). For graduate courses that are research intensive, this becomes quite ambigious.
* **Implementing**: Any configuration task that does not require specific skills.
  * This includes IDE configuration, LMS configuration, etc.
* **Assessments**: Any assessment taken outside of class. This includes quizzes and exams.

I do not track lecture time. I attend most lectures, so I can figure out how much time I've spent in lecture if needed. Furthermore, the benchmark of "3 hours per 1 hour of lecture" was a compelling relationship to explore (and, for me, it's untrue). 

I have a few rules for when I track time: 
* Looking at my phone for more than 15 seconds forces the timer to stop.
  * This is long enough to switch music and make sure that any texts were not emergencies. 
* Checking email/news/etc. forces the timer to stop (unless this is apart of the task).
* Any breaks (snack, stretch, etc.) forces the timer to stop.
* Switching tasks forces the timer to switch with me.

# Why I Track my Time

There's a few reasons why I track the time I spend on classes: 

### 1. Tracking assignments early in the semester helps me project my workload for later in the semester. 
> Generally, if assignments are well-formatted and well-balanced, the time spent on subsequent assignments of the same type in a class will decrease throughout the semester. This is not always the case, but it at least provides a benchmark. Using historical data allows me to calculate burndown rates as finals approach and helps me manage final projects. 
### 2. Tracking assignments provides a measure of difficulty
> Time gives an objective measure of difficulty - it's not a great measure, but it is at least a metric. For example, the start of a paper is always tough, so I'll force myself to sit and write for an hour. Or, if I'm working on a frustrating project, I can check my time and say, "Wow, I've invested a lot of time into this. I'm probably working on a difficult problem." This recognition allows me to take pride in doing difficult work. 
### 3. Tracking classes keeps me accountable
> One of my biggest pet peeves is hearing other students say, "I spent ALL day working on this assignment." Really? ALL day? Hyperbolic complaints about classwork commitments can be taken literally, forcing unncessary concessions from professors and creating a negative student culture. Tracking my own time allows me to recognize inordinate time use on an assignment and change my strategy. Maybe, I need to change my approach. Maybe, I need to spend less time on a certain aspect of the assignment. Maybe, I just need to take a break because I've been working for too long. Or, in a worst case scenario, I disagree with the pedagogy of the assignment because my time-to-learning ratio is high, and I abandon the assignment. 
### 4. Tracking my time keeps me focused
> Starting a timer means that I am engaging in deep work. There's a mindset shift when that timer starts. It prevents me from getting distracted or otherwise increasing the amount of time I spend on an assignment. I would much rather write music or go on a run than procrastinate my homework by scrolling YouTube.

# Why I'm Releasing this Data

When I'm registering for classes and preparing for a semester, I usually have 2 questions about a class: 
1. Will this be interesting?
2. How much time will this take?

Furthermore, when I start an assignment, I have two similar questions:
1. How much will I learn from this?
2. How much time will this take? 

I've decided to release my time tracking because I believe that it's helpful for: 
* Students at my school: seeing the overall time spent on a class is generally beneficial for course registration. However, it would also be useful to see individual assignment breakdowns. While it's always the hope that the personal time commitment for previous assignments in a class will the predict time commitment for subsequent assignments, there's significant variability. I know **I** would personally appreciate seeing how long it took for other students to actually complete these assignments instead of forecasting my own expectations.
* Students at other schools: there's a pervasive hustle culture that glorifies the poor usage of time. Spending time on something you hate is entertaining, but certainly not encouraging (or healthy). I'm hoping this project demonstrates that academic success is possible without being miserable. 
* Faculty: It's easy for students to overexaggerate their time usage, especially if it's for a class they didn't enjoy. Being able to see how a student spends their time outside of class may be beneficial to course planning and content management.

# Interesting Things About this Data

1. Some classes are spiky with irregular time contributions, like [OS](reports/OPERATING-SYSTEMS_CSCI442_F2023.pdf). Some classes are relatively flat, like [Principles of Chemistry I](reports/CHEMISTRY-I_CHGN121_S2023.pdf).
2. My time use falls _very_ short of the "3 hours of outside work per credit per week" metric (see [graph](images/hours_per_credit.png)). If I spent an average of 12 hours per week on homework and spent about 12 hours in lecture every week, that's only 24 hours a week, as opposed to the "expected" 48 hours a week.
3. My [time per day](images/F2023_per_day.png) is very slanted. Generally, I have very few commitments in the first half of the week, so I complete the majority of my work Monday-Wednesday.

# My Learning Style

Everybody learns (and works) differently, so my data will undoubtedly differ from other students. 

My learning style has a few characteristics: 
1. **Trust and In-Person**: I absolutely prefer to learn from a lecturer that I trust rather than read something online, so attending lectures is a priority. This will reduce the amount of time an assignment takes because the work of understanding the concepts will have been completed in lecture. 
2. **Individual**: I hate studying or doing homework in groups, so the vast majority of tracked entries describe individual, solo work.
3. **Writing**: I take hand-written notes for every lecture and most readings. It keeps me engaged in the content and helps me actively organize my thoughts. 

# Toggl Details

For those of you who are Toggl power users: each course was designated as its own project, each assignment was as its own time entry, and each semester was organized as a client. Domains and Types are tags.  

I use the free version of Toggl. Maybe Toggl has the per-tag analytics in the pro version, but I wouldn't know. 

# About Me

I am a Junior at the Colorado School of Mines studying Computer Science with a minor in Public Affairs through the McBride Honors Program. I've maintained a 4.0 in all of my coursework. This time tracking data is indicative of what it took me to get an As in all of my classes. This will not be the same for everybody. 
