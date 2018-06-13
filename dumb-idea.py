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
        "Instagram"
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
        "Crowd Sourcing"
]

print("It's like", popularProductOrCompany[random.randint(0, \
    len(popularProductOrCompany) - 1)], "for", \
    industryOrPopularTech[random.randint(0, len(industryOrPopularTech) - 1)])
