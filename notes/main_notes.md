# Notes

## Thoughts
- [ ] Define [subjects](#subjects-of-interest) of interest to infer the sources
- [ ] Define the [sources](#sources)
- [ ] Define the [steps of the process](#thoughts)
- [ ] Define the [steps of the code](#overview-of-the-steps)
- [ ] Define the [database systems](#data-base-systems)
- [ ] SOTA recommender systems papers
- [ ] SOTA [recommander systems packages](#models-packages)
- [ ] SOTA [ETL methodology](sota_etl.md) and best practices
- [ ] SOTA ETL Python framewords
- [ ] Cloud based? Which platform?
- [ ] Find non addictive distractions (videos that do not still your daily attention reserves)
- [ ] SOTA of [similar projects](#similar-projects)

## Implementations
- [ ] Create a data lake
- [ ] Create a class API connector
- [ ] Create a class DB connector
- [ ] Create a wiki along the code
- [ ] Create unit tests


## Overview of the steps
1. Extract data (videos, articles)
2. Transform data (in a digestable format for the model)
3. Make recommendations

### Detailed steps
Extract data (videos, articles)
- from applications with API 
- scrapping websites without API
- insert in database


## Subjects of interest
- AI / Data Science and Python Programming
- Objective view of politics (constantly watching an equiponderated portfolio of politics from all viewpoints)
- Ecology
- Balanced news of the world both positive and negative
- Financial crisis
- Law amandements that impact us: education, housing
- Trusted sources only
- Not relying on presence or absence of click-bait title but rather on the actual content


## Data base systems
- Flat? [Uncle Bob Clean Code](https://www.youtube.com/watch?v=7EmboKQH8lM&list=PLmmYSbUCWJ4x1GO839azG_BBw8rkh-zOj) advocate for flat format
- Postgres for tabular data and MongoDB for unstructured data?

## Models packages
- [Deep models](https://github.com/maciejkula/spotlight)
- User-based: not good since should first be based on single user only
  - [matrix factorization (SVD)](https://github.com/Quang-Vinh/matrix-factorization) (code ref to check)
  - [SVD](https://github.com/muricoca/crab)
- Item-based: similarity between new and content already seen (appreciated or not)
  - [bag of words](https://scikit-learn.org/stable/modules/feature_extraction.html#common-vectorizer-usage) (on variables: video, description and title)
  - [TF-IDF](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting)
  - graph: on variables: content creator / author



## Sources

Anything
- [Youtube](https://www.youtube.com/)

Research
- [Arxiv](https://arxiv.org/) and [Arxiv-sanity](https://arxiv-sanity-lite.com/)
- [Google Scholar](https://serpapi.com/google-scholar-api)
- [Springer Nature](https://dev.springernature.com/)

Data & AI
- [Towards Data Science](https://towardsdatascience.com/)
- [The Batch - Andrew Ng.](https://www.deeplearning.ai/the-batch/)

Politics ([ref](https://www.integrersciencespo.fr/orientations-politiques-de-la-presse-etrangere-et-francaise))
- [Left side: Le Monde](https://www.lemonde.fr/)
- [Right side: Figaro](https://www.lefigaro.fr/)
- [Liberal: Les Echos](https://www.lesechos.fr/)
- [Extreme left: L'humanité](https://www.humanite.fr/)
- [Anti system: Marianne](https://www.marianne.net/)
- [Extreme right: Valeurs actuelles](https://www.valeursactuelles.com/)
- [Russia: TASS](https://tass.com/?utm_source=google.com&utm_medium=organic&utm_campaign=google.com&utm_referrer=google.com) - Check if legit with natives
- [China: China Daily](https://www.chinadaily.com.cn/) - Check if legit with natives
- [India: The Hindu](https://www.thehindu.com/news/national/)
- TODO: find other international journals

## Similar projects
- [Portal](https://github.com/grahamjenson/list_of_recommender_systems)

