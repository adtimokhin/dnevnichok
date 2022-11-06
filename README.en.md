# _**Dnevnichok**_

___

## Table of contents

* [What this project is](#Section-1.-What-this-project-is)
    * [Summary](#Summary)
    * [What do you track with Dnevnichok](#What-do-you-track-with-Dnevnichok)
    * [What to do with collected data](#What-to-do-with-collected-data)
* [Installment](#Section-2.-Installment)
* [Operating Dnevnichok](#Section-3.-Operating-Dnevnichok)

---

## Section 1. What this project is

### Summary

This is a digital diary that you can access though terminal to record your current psychological state.

I find it useful to keep track of how do I feel during the day in order to realise if there are any patters to why I
feel down. That helps to overcome the anxieties faster.

The ultimate goal is to make a list of events that correlate with how well you are doing. Having such a list that you
can use to predict your future happiness is very useful. I believe that such _**"events"**_ can be identified by taking
a record of what you are doing during a day as well as what thoughts enter your mind.

### What do you track with Dnevnichok

Every day, you will access the program to record information in the following categories:

1) Emotional Happiness
2) Security Protocol
3) Thoughts
4) Things done during the day

#### Emotional Happiness:

That is the relative measure that you use to tell how overall do you feel. It is a number in range from 0 to 10. The
meaning of each of the values for this spectrum I believe to be open to interpretation of the user of Dnevnichok I,
personally, set 5 to be a neutral state. Anything above - I feel happy.

#### Security protocol:

That is a list of the special events that signify how your emotional happiness is changing. Originally you might have
some believes to what those events might be. Go ahead and add them to the security_protocol.json file (more on it
later)!

If you do not know what these events are, do not worry. Idea is that after analysing your emotional patterns and things
that you do and experience during the day, you will be able to update the security protocol.

#### Thoughts:

That is a list of thoughts that you had about the day. That list does not have to be very descriptive. Include only
those things that you consider to be of some significance.

#### Things done:

That is a list of activities that you engaged during the day. Again, list only those that are of some significance to
you.

Bedsides providing a description to what have you done, you will also answer to two questions:

* How odd (unusual) was the activity that you were engaged in? Measured on a scale from 0 to 10
* How happy did you feel while doing that thing. Also on a range from 0 to 10. I suggest to set 5 as a neutral state,
  but it is totally up to you what meaning this numbers will have.

### What to do with collected data

As for now, you will have to analyse it manually. The goal you are trying to achieve is to identify your, as I call
it, "Security protocol".

## Section 2. Installment

### Step One: Clone the repository

Go ahead and clone `main` branch from the [github](https://github.com/adtimokhin/dnevnichok) to your computer

### Step Two: Install Python packages

Install required dependencies, that are used in this project:

```text
python -m pip install rich 
```

If you have trouble installing the dependency, use the
following [documentation](https://github.com/Textualize/rich/blob/master/README.es.md)

If you do not have `pip` installed on your computer use
this [website](https://www.geeksforgeeks.org/how-to-install-pip-in-macos/)

## Section 3. Operating Dnevnichok

To start Dnevnichok, open up the terminal and navigate to the folder where you stored the repository and enter command:

```text
python3 main.py
```

You should be presented with this message:
![Picture that contains a welcome message from the program](/Users/atimokhina/Desktop/Screenshot 2022-11-05 at 8.50.41 PM.png "This is what you should see when you launch the program")

You are presented with the following command options:

`1` - will print a list of all dates for which the diary entries exist

`2` - will prompt you to enter information about one of the days. You can update information for other dates, not only
for the current date

`3` - will print a summary that describes how the program works (currently - this feature does not work, so rely on the
documentation)

`help` - will do the same as `3`

`exit` - will terminate the program execution