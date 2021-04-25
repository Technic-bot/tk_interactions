# Twokinds interaction analyzer.
Small repo consisting on my work on monitoring number of interactions related to the Twokinds comic, this is done via web scraping of 3 main sources
Official forum, official twitter handle and non-official, but largest, reddit community. 

## Web Scraping layer
Please check each folder for a small explanation an examples on how to run the scrapers. They are all based on python with the following requirements:

Requirements
- python>=3.5
- requests>=2.8
- beautifulsoup4>=4.6.0

## Data Layer
Scraped results are stored here for convenience, since they are relatively small for now. If ever manage to create a giant csv file with the data-set it will be hosted elsewhere but in the meantime this is a 'batteries included' repo. No need to run the scrapers to get the data and then clean it.

## Analysis layer
You are here, based on python pandas, matplotlib and sci-py interactions graphs are generated. They highlight events or extrema, all instances when the measurement is over 2 standard deviations away from the mean. It also marks the mean and standard deviation as horizontal lines. But these parameters are configurable please consult the analyze_interactions.py help for a full breakdown of the available options.

Usage examples can be found on the get<platform>.sh scripts. 

Requirements
- pandas==1.1.0
- matplotlib==3.2.1
- numpy==1.18.2
- pandas==1.1.0
- scipy==1.4.1

## Graphs.
Added examples of the outputs. These particular images are create via running the get_platform.sh scripts. 



