

# AB Testing - Introduction

## Introduction

In this section, you'll get to develop your skills regarding AB testing. Before diving in, take a minute to note some key points which you should keep in mind when completing the various labs and conducting your own hypothesis tests in practice.


## Experimental Design

You've seen that a lot goes into the proper design of statistical tests. You've learned about Goodheart's law as well as the multiple comparisons problem. Additionally, you've also seen that a p-value by itself is prone to misinterpretation if not presented with other relevant design parameters such as effect size, sample size, and  <img src="https://render.githubusercontent.com/render/math?math=\alpha"> . With that, here are three overarching considerations to keep in mind.

### Well Formulated Questions

A well-formulated question is essential to a good statistical experiment. This includes careful thought of unintended consequences, as you saw in the discussion of Goodheart's law. Additionally, the question should also be specific and measurable.

### Choosing Appropriate Parameters

It cannot be stressed enough how important the relationship between  <img src="https://render.githubusercontent.com/render/math?math=\alpha"> , power, sample size and effect size is. While larger sample sizes provide more powerful tests, one should also realize that tiny effects can produce significant p-values with large samples. While this may be interesting, such small practical differences might have little to no applicable value. Furthermore, avoiding pitfalls such as the multiple comparisons problem is also important. Recall that if you perform multiple t-tests, The probability of encountering a type I error will continue to increase with additional tests. (Each test will still have the corresponding alpha value set, but collectively, the chance that a false positive type I error exists in your conclusions increases.)

### Preprocessing, Data Anomalies and Outliers

On the other end of problem formulation is formatting the data to actually answer said question. You'll encounter this most explicitly in the final lab of this section. There, you'll have to transform your data into an appropriate format before conducting the statistical test. Furthermore, it's important to note how idiosyncrasies in your data can impact results. For example, monumental outliers can drastically impact the outcome of statistical tests. Whether or not to remove these data points can be a source of contention and will vary upon the circumstance. Similarly, it should go without saying that erroneous data or faulty data will clearly degrade statistical tests. All in all, it's always important to get familiar with the structure of the data and the context of the question being asked before diving into the statistics themselves.

## Summary 

Time to have at it! Dive in and start practicing some hypothesis testing!
