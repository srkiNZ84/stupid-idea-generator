import random

popularProductOrCompany = ["AirBnB", \
        "Uber", \
        "Apple", \
        "Netflix", \
        "Google", \
        "Facebook", \
        "Twitter", \
        "Spotify", \
        "SpaceX", \
        "Snapchat", \
        "Instagram", \
        "Juicero", \
        "Tinder", \
        "Tesla", \
        "Pinterest", \
        "SalesForce", \
        "WhatsApp", \
        "Slack", \
        "Lyft", \
        "YouTube", \
        "Siri"
]

industryOrPopularTech = ["Big Data", \
        "SaaS", \
        "IoT", \
        "FaaS", \
        "Kubernetes", \
        "Docker", \
        "Secrets Management", \
        "Crowdsourcing", \
        "On-Demand", \
        "Cloud", \
        "Machine Learning", \
        "AI", \
        "Data Mining", \
        "Distributed Teams", \
        "Observability", \
        "Distributed Systems", \
        "DevOps", \
        "Serverless", \
        "Progressive Web Apps", \
        "Crowd Sourcing", \
        "Cryptocurrency", \
        "BitCoin", \
        "3D Printing", \
        "Virtual Reality", \
        "Augmented Reality", \
        "the Gig Economy", \
        "Voice Interfaces"
]

print("It's like", popularProductOrCompany[random.randint(0, \
    len(popularProductOrCompany) - 1)], "for", \
    industryOrPopularTech[random.randint(0, len(industryOrPopularTech) - 1)])
