# Classification-Project
NCKU DataMining Project2
P76051072 林嘉源

My dataset simulate a imaginary country and 100(number of data: M = 100) civilian. This project try to predict whether people can live longer than the HALE (health-adjusted life expectancy) of not.
In my simulation, 100 civilian are sampled, and the HALE of this country is set to 76 years old. Each row in my dataset can be viewed as the basic information about a person in that country. 
The features are listed as following (number of attributes: K = 6):
a.	Sex: female: 0, male: 1
b.	Drink: drinking alcohol frequently or not: yes/ no
c.	Smoke: taking cigarettes frequently or not: yes/ no
d.	Eat_betel_nuts: 很常吃檳榔嗎? yes/ no
e.	Marriage: Marriage: 2, Divorced: 1, Unmarried: 0
f.	Num_children: the number of children this person has. Here I don’t want to talk about why an unmarried person has children. Maybe, he/she is an unmarried father/mother.
My Target: their age of death is longer than HALE of this country (= 76) or not: yes/ no
Note:
a.	the attached GenerateData.py can generate my simulated dataset.
b.	The split ratio of training and testing are 7:3.
