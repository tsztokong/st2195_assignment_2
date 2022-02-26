#import rvest
library(rvest)
library(csv)

#Load CSV Wiki page
csv_wiki <- read_html('https://en.wikipedia.org/wiki/Comma-separated_values')

#Find table in the example by piping 
csv_table <- csv_wiki %>% html_element('.wikitable') %>% html_table()

#write to csv to working directory
write.csv(csv_table, "csv_example_r.csv", quote = TRUE, row.names = FALSE)