from urllib.parse import urlparse
url = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'
parsed_url = urlparse(url)
print(parsed_url.scheme)    #it print https
print(parsed_url.netloc)    # it print domain name
print(parsed_url.path)      #prints path to page
print(parsed_url.query)     #prints parameter values
print(parsed_url.fragment)   #prints fragments

import requests
from bs4 import BeautifulSouppython
import os
#url article
urls = ['https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/',
       'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/',
        'https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/',
        'https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/',
        'https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/',
        'https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/',
        'https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/',
        'https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/',
        'https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/',
        'https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/',
        'https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/',
        'https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/',
        'https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/',
        'https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/',
        'https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/',
        'https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/',
        'https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/',
        'https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/',
        'https://insights.blackcoffer.com/evolution-of-advertising-industry/',
        'https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/',
        'https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/',
        'https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/',
        'https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/',
        'https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/',
        'https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/',
        'https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/',
        'https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/',
        'https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/',
        'https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/',
        'https://insights.blackcoffer.com/how-we-forecast-future-technologies/',
        'https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/',
        'https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/',
        'https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/',
        'https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/',
        'https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/',
        'https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/',
        'https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/',
        'https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/',
        'https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/',
        'https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/',
        'https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/',
        'https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/',
        'https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/',
        'https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/',
        'https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/',
        'https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/',
        'https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/',
        'https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/',
        'https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/',
        'https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/',
        'https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/',
        'https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/',
        'https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/',
        'https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/',
        'https://insights.blackcoffer.com/human-rights-outlook/',
        'https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/',
        'https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/',
        'https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/',
        'https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/',
        'https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/',
        'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/',
        'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/',
        'https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/',
        'https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/',
        'https://insights.blackcoffer.com/travel-and-tourism-outlook/',
        'https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/',
        'https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/',
        'https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/',
        'https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/',
        'https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/',
        'https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/',
        'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/',
        'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis/',
        'https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding/',
        'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-2/',
        'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-3/',
        'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-3/',
        'https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work/',
        'https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding-2/',
        'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-4/',
        'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-2/',
        'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-3/',
        'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-4/',
        'https://insights.blackcoffer.com/why-scams-like-nirav-modi-happen-with-indian-banks/',
        'https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy/',
        'https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy-2/',
        'https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy-2/',
        'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-3/',
        'https://insights.blackcoffer.com/should-celebrities-be-allowed-to-join-politics/',
        'https://insights.blackcoffer.com/how-prepared-is-india-to-tackle-a-possible-covid-19-outbreak/',
        'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work/',
        'https://insights.blackcoffer.com/controversy-as-a-marketing-strategy/',
        'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry/',
        'https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets/',
        'https://insights.blackcoffer.com/what-are-the-key-policies-that-will-mitigate-the-impacts-of-covid-19-on-the-world-of-work/',
        'https://insights.blackcoffer.com/marketing-drives-results-with-a-focus-on-problems/',
        'https://insights.blackcoffer.com/continued-demand-for-sustainability/',
        'https://insights.blackcoffer.com/coronavirus-disease-covid-19-effect-the-impact-and-role-of-mass-media-during-the-pandemic/',
        'https://insights.blackcoffer.com/should-people-wear-fabric-gloves-seeking-evidence-regarding-the-differential-transfer-of-covid-19-or-coronaviruses-generally-between-surfaces/',
        'https://insights.blackcoffer.com/why-is-there-a-severe-immunological-and-inflammatory-explosion-in-those-affected-by-sarms-covid-19/',
        'https://insights.blackcoffer.com/what-do-you-think-is-the-lesson-or-lessons-to-be-learned-with-covid-19/',
        'https://insights.blackcoffer.com/coronavirus-the-unexpected-challenge-for-the-european-union/',
        'https://insights.blackcoffer.com/industrial-revolution-4-0-pros-and-cons/',
        'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy/',
        'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-2/',
        'https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy/',
        'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-global-economy/',
        'https://insights.blackcoffer.com/ensuring-growth-through-insurance-technology/',
        'https://insights.blackcoffer.com/blockchain-in-fintech/',
        'https://insights.blackcoffer.com/blockchain-for-payments/',
        'https://insights.blackcoffer.com/the-future-of-investing/',
        'https://insights.blackcoffer.com/big-data-analytics-in-healthcare/',
        'https://insights.blackcoffer.com/business-analytics-in-the-healthcare-industry/',
        'https://insights.blackcoffer.com/challenges-and-opportunities-of-big-data-in-healthcare/',
       ]
# get the content of the article

for url in urls:
    # get the content of the article
    response = requests.get(url)
    soup = BeautifulSouppython(response.content, 'html.parser')
#extract the article text
article = ''
for paragraph in soup.find_all('p'):
    article += paragraph.text + '\n'

#save the extracted text into a file
url_id = url.split('/')[-1]
file_name = f'{url_id}.txt'

with open(file_name,'w') as file:


#print the file name where the articles are saved
    print(f'The article is saved into :{os.getcwd()}/{file_name}')