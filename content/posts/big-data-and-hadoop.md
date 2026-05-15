+++
title = "Big Data and Hadoop"
date = "2013-02-28T14:16:00.001Z"
slug = "big-data-and-hadoop"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/02/big-data-and-hadoop.html"
bloggerID = "1841076477405711307"
tags = ["Programming"]
[cover]
  image = "/images/blogger/1841076477405711307/392332859_6d08197b35_b.jpg"
+++

[![](/images/blogger/1841076477405711307/392332859_6d08197b35_b.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisXOeZtJtfHaSiH7YNWnOUhcNLVmWnq0Yf_BO-oRpaAcdw2aDvkjZ3dz9KbHeF0In2PepfiyzBR_yqwYOpwiHkELfWnd2b7QCNGfUxZ79HqJ8m8buii8nUYxo_lYYhyyWJzNdpsUZAgfE/s1600/392332859_6d08197b35_b.jpg)

 Spring.Taiwan  
  
Read the book "Understanding Big Data" today. Half way done.   
Here's some excerpts from the book:  

## Understanding Big Data

2013-02-28 15:45:37

the term Big Data applies to information that can’t be processed or analyzed using tradi-tional processes or tools

2013-02-28 15:46:12

An
IBM survey found that over half of the busi-ness leaders today realize
they don’t have access to the insights they need to do their jobs

2013-02-28 15:48:45

Even
if every bit of this data was relational (and it’s not), it is all
going to be raw and have very different for-mats, which makes processing
it in a traditional relational system impractical or impossible

2013-02-28 15:49:05

variety combining to create the Big Data problem

2013-02-28 15:51:31

Three characteristics define Big Data: vol-ume, variety, and velocity.

2013-02-28 15:54:17

the
opportunity exists, with the right technology platform, to ana-lyze
almost all of the data (or at least more of it by identifying the data
that’s useful to you) to gain a better understanding of your business,
your customers, and the marketplace

2013-02-28 15:55:35

a
fundamental shift in analysis require-ments from traditional structured
data to include raw, semis-tructured, and unstructured data as part of
the decision-making and insight process

2013-02-28 15:56:27

To
capi-talize on the Big Data opportunity, enterprises must be able to
analyze all types of data, both re-lational and nonrelational: text,
sensor data,

2013-02-28 15:56:50

Dealing
effectively with Big Data requires that you perform analytics against
the volume and variety of data while it is still in motion, not just
after it is at rest

2013-02-28 15:58:11

Hadoop-based
platform is well suited to deal with semistructured and unstructured
data, as well as when a data discovery process is needed

2013-02-28 16:07:26

it is about dis-covery and making the once near-impossible possible from a scalability and analysis per-spec-t

2013-02-28 16:09:19

creator Doug Cutting’s son gave to his stuffed toy elephant

2013-02-28 16:09:44

duce)—more on these in a

2013-02-28 16:10:23

this redundancy provides fault toler-ance and a capability for the Hadoop cluster to heal itself

2013-02-28 16:10:55

Some
of the more notable Hadoop-related projects include: Apache Avro (for
data serializa-tion), Cassandra and HBase (databases), Chukwa (a
monitoring sys-tem spe-cifically designed with large distributed systems
in mind), Hive (provides ad hoc SQL-like queries for data aggregation
and summariza-tion), Mahout (a machine learning library), Pig (a
high-level Hadoop programming language that provides a data-flow
language and execution framework for parallel computation), ZooKeeper
(provides coordination services for distributed ap-plications), and more

2013-02-28 16:12:23

throughout the cluster

2013-02-28 16:13:54

For Hadoop deployments using a SAN or NAS, the extra network commu-nica-tion overhead can cause performance bottle

2013-02-28 16:14:59

an individual file is actually stored as smaller blocks that are repli-cated across multiple servers in the entire cluster

2013-02-28 16:16:09

default size of these blocks for Apache Hadoop is 64 MB

2013-02-28 16:21:41

All of Hadoop’s data placement logic is managed by a special server called **NameNode**

2013-02-28 16:28:14

All of the NameNode’s infor-mation is stored in memory, which allows it to provide quick response times

2013-02-28 16:30:33

Any data loss in this metadata will result in a permanent loss of corresponding data in the cluster

2013-02-28 16:32:25

devel-oper doesn’t have to deal with the concepts of the NameNode and where data is stored—Hadoop does that for you

2013-02-28 16:38:42

The
first is the **map** job, which takes a set of data and converts it into
another set of data, where individual elements are broken down into
tuples

2013-02-28 16:38:51

**reduce** job takes the output from a map as input and combines those data tuples into a smaller set of tuples

2013-02-28 16:41:20

All
five of these output streams would be fed into the reduce tasks, which
combine the in-put results and output a single value for each city,
producing a final result set

2013-02-28 16:43:08

MapReduce program is referred to as a job. A job is executed by subse-quently breaking it down into pieces called tasks

2013-02-28 16:43:45

An application submits a job to a specific node in a Hadoop cluster, which is running a daemon called the JobTracker

2013-02-28 16:44:39

In a Hadoop cluster, a set of continually running daemons, referred to as TaskTracker agents, monitor the status of each task

2013-02-28 16:46:39

This
direct-ing of records to reduce tasks is known as a Shuffle, which
takes input from the map tasks and directs the output to a specific
re-duce task

2013-02-28 16:47:29

under
Hadoop are written in Java, and it is the Java Archive file (jar)
that’s distributed by the JobTracker to the various Hadoop cluster nodes
to execute the map and reduce tasks

2013-02-28 16:48:00

**BigDataUniversity.com
and download Info-Sphere BigInsights Basic Edi-tion
(www.ibm.com/software/data/infosphere/ biginsights/basic.html**

2013-02-28 16:49:58

Hadoop Common Components are a set of libraries that support the var-ious Hadoop subprojects

2013-02-28 16:50:50

When
you
delete an HDFS file, the data is not actually gone (think of your MAC or
Windows-based home computers, and you’ll get the point). Deleted HDFS
files can be found in the trash, which is automatically cleaned at some
later point in time

2013-02-28 16:52:46

we cover three of the more popular ones, which admit-tedly sound like we’re at a zoo: **Pig, Hive, and Jaql**

2013-02-28 16:53:09

Pig was initially developed at Yahoo

2013-02-28 16:56:02

you
can FIL-TER out rows that are not of interest, JOIN two sets of data
files, GROUP data to build aggrega-tions, ORDER results, and much more

2013-02-28 16:58:01

**There
are three ways to run a Pig program: embedded in a script, embedded in a
Java program, or from the Pig command line, called Grunt**

2013-02-28 16:58:51

Some
folks at Face-book developed a runtime Hadoop sup-port structure that
allows anyone who is already fluent with SQL (which is commonplace for
rela-tional data-base developers) to leverage the Hadoop platform right
out of the gate. Their cre-ation, called Hive

2013-02-28 16:59:50

You can use the Hive Thrift Client within applications written in C++, Java, PHP, Python, or Ruby

2013-02-28 17:01:19

Hive is read-based and therefore not appropriate for transaction processing

2013-02-28 17:03:11

JSON is built on top of two types of struc-tures. The first is a collection of name/value pairs

2013-02-28 17:03:35

The
sec-ond JSON structure is the ability to create an or-dered list of
values much like an array, list, or se-quence you might have in your
existing applica-tion

2013-02-28 17:09:13

The
operand used to signify flow from one operand to another is an arrow:
->. Unlike SQL, where the output comes first (for example, the SELECT
list)

2013-02-28 17:15:16

Jaql
is a flexible infras-tructure for managing and analyzing many kinds of
semistructured data such as XML, CSV data, flat files, relational data,
and so on

  
REF:  
<http://www.ibm.com/developerworks/wikis/display/db2oncampus/FREE+ebook+-+Understanding+Big+Data>
