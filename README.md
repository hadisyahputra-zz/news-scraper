# News Scraper

## Project setup
```
cd news scraper
pip install requirements.txt
```

## Chrome Driver
```
You can download the driver here: https://chromedriver.chromium.org/downloads
Download the one which suits with your chrome version and OS
Current driver is located in chromedriver_linux64 folder 
```

## Scraper scripts
```
The scripts is located in scraper folder. The available scripts:
1. antaranews.py, scrapes popular news in https://www.antaranews.com/#tab-popular
2. detik.py, scrapes popular news in https://www.detik.com/terpopuler
3. inilah.py, scrapes popular news in https://inilah.com
4. jawapos.py, scrapes trending news in https://www.jawapos.com
5. jpnn.py, scrapes popular news in https://www.jpnn.com/populer
6. kapanlagi.py, scrapes trending news in https://www.kapanlagi.com/trending
7. kompas_populer.py, scrapes popular news in https://www.kompas.com
8. kompas_trending.py, scrapes treding news in certain date
9. kumparan.py, scrapes trending news in https://kumparan.com/trending
10. liputan6.py, scrapes popular news in https://www.liputan6.com/indeks/terpopuler
11. merdeka.py, scrapes trending news in https://www.merdeka.com/trending
12. okezone.py, scrapes popular news in https://www.okezone.com
13. republica.py, scrapes popular news in https://republika.co.id/kanal/news
14. sindonews.py, scrapes popular news in https://www.sindonews.com
15. suara.py, scrapes popular news in https://suara.com
16. tempo.py, scrapes popular news in https://www.tempo.co/populer
17. tirto.py, scrapes popular news in https://tirto.id
18. tribunnews.py, scrapes popular news in https://www.tribunnews.com/populer
19. viva.py, scrapes popular news in https://www.viva.co.id
```

## Run the scraper scripts
```
1. All scripts, except kompas_trending:
python [script_name].py (ex: merdeka.py)
2 Script kompas_trending:
python kompas_trending 2020-11-22
```

## Scraping results
```
The scraping results are stored in scrape result folder.
In that folder, there are folders that each of them has a name, which represents the scrapped news portal.
For instance, if you run merdeka.py, the scraping result on merdeka.com website is stored in scrape result/merdeka folder. 
```