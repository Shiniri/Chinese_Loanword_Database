# Chinese_Loanword_Database / 中文借词数据库


This database contains loanwords in various Chinese varieties from other languages.
这个数据库包含了从其他语言中借来的各种中文品种的词汇。

## Introduction

Probably due to the restrictive phonotactic structure of Chinese its varieties contain
relatively few loanwords from other languages. Additionally, loanwords are sometimes
very hard to identify because they are highly integrated into the Chinese morpho-phonemic
system. Thus, I have made this database to aid the research of Chinese loanwords (and out of
personal interest). Currently, it contains all loanwords that I have come across myself
in various Chinese varities and their:
  - Hanzi representation
  - Pinyin Representation
  - Original form in donor language
  - English translation
  - Donor language
  - Semantic Category (in congruence with the [WOLD](https://wold.clld.org/))
  - Additional information, e.g. what kind of loanword it is

## How to use

I have included the following functions in the `Database_Tools`-class to
interact with the database file:
  - `create_connection`, connects to the chinese_loanword_database.db
  - `execute_query`, executes a SQlite query on the database
  - `add_word`, accepts a list which will be inserted into the database as new row
  - `update_txt_from_database`, copies the database to a txt for better readability

## Suggest additions

On the off chance that someone takes interest in this project (you, for example!):
my contact email address is mariebauer2610@gmail.com. There you can suggest loanwords
you came accross, ideally with a quotation if you took them from an available corpus
and the meta-information also included in my database. Alternatively, you can just
make a request to edit the repository itself. Same goes for changes to already existing
words.
