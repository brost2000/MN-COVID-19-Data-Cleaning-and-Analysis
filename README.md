# MN-COVID-19-Data-Cleaning-and-Analysis
This project uses a dataset obtained from https://www.health.state.mn.us/diseases/respiratory/stats/hosp.html in order to understand hospitalizations over time within Minnesota from 2020 - 2025. 

## 1  Introduction
This project analyzes data obtained from the Minnesota Department of Health in order to understand continued patterns of hospitalization due to repiratory illness, especially COVID-19 over a five year period from 1/3/2023 - 2/2/2025. This data is valuable because it allows us to cross reference hospitalization patterns with vaccination rates (against the COVID-19 virus), allowing us to draw some preliminary conclusions on the long term effectiveness of the virus.
  This project will seek to analyze a few specific pieces of data. First, I analyze total rates of hospitalization by age group (figure 1). Next, I analyze rates of hospitalization over time for each age group. Finally, I cross reference both total hospitalization per age group and immunization rates in order to see whether there is any change in long-term hospitalization rates based on vaccination status. 

## 2  Background
The COVID-19 pandemic was a significant time period in world history. It saw the development of a number of different vaccination options with unprecedented speed. A study from the [NIH](https://pmc.ncbi.nlm.nih.gov/articles/PMC7889064/) notes that: 

>While typical vaccine development can take upwards of 10–15 years, COVID-19 vaccines were developed in less than a year after the identification of COVID-19. 

The [Minnesota Department of Health](https://www.health.state.mn.us/diseases/respiratory/stats/vaccine.html) publishes a number of useful datasets which track respiratory illness by hospitalization over time, vaccination rates over time, and vaccination rates by county. They also provide clear [guidelines and recommendations](https://www.health.state.mn.us/diseases/coronavirus/stats/vbt.html) for vaccination against repiratory illnesses. They note that:

>People who have completed at least a primary series are less likely to be hospitalized or die than people with similar risk factors who are not vaccinated. People who have received their bivalent booster have an even lower risk of hospitalization or death than people with similar risk factors who have only received monovalent doses of vaccine or people who are not vaccinated.

This project takes pre-existing data and connects it together to draw conclusions about the ongoing state of Minnesota public health in regard to respiratory illness. Especially noteable is the treatment of vaccination as a public health issue. On this topic, the [European Commission of Public Health](https://health.ec.europa.eu/vaccination/overview_en) notes that: 

>Vaccination is the main tool for primary prevention of disease and one of the most cost-effective public health measures available.

This marks vaccination primarily as a 'public health' issue, not as an issue of personal autonomy. The intersection of these competing philosophies of immunization is the concept of vaccine hesitancy. The [European Center for Disease Prevention and Control](https://www.ecdc.europa.eu/en/immunisation-vaccines/vaccine-hesitancy) describes vaccine hesitancy as:

>Vaccine hesitancy refers to delay in acceptance or refusal of vaccines despite availability of vaccination services.

## 3  Methodology
My goal with this project was to investigate the potential connections between vaccination status and hospitalization over time. In doing so, I believe that more informed policy decisions regarding the future of vaccine development can be informed by medium term effectiveness studies. In beginning this study, I obtained datasets from the Minnesota Department of Health. Specifically I obtained three different datasets: vaxot (measuring % of people up to date on vaccinations by pathogen), vacounty (measuring total people up to date on vaccinations by county and pathogen), and respnetage (measuring hospitalization over time by age group and pathogen). 

Each of these datasets tells part of the story, but so far, there is no clear study combining the separate datasets into one actionable conclusion. In order to get at this conclusion, I first cleaned each dataset using the Pandas package in Python 3. Fortunately, these datasets are well-maintained. Where necessary, I replaced NaN values with a calculated mean value using:

```
mean_value = df.["column"].mean()
df.fillna(value=mean_value, inplace=True)
```

Regarding the actual analysis, I used Matplotlib.pyplot to plot different series against one another. Where necessary, different columns were combined to make the data vizualizable. For example, in the case of the first visualization (more details in section 4), it was necessary to group df.["Age Group"] and df.["Count of Hospitalizations"] in order to be able to visualize by age group specifically. Regard below:

```
df_grouped = df.groupby("Age Group")["Count of Hospitalizations"].sum().reset_index()

age_order = ["0-4", "5-17", "18-49", "50-64", "65"]
df_grouped["Age Group"] = pd.categorical(
  df_grouped["Age Group"], categories = age_order, ordered = True
)
```
I also used basic 
