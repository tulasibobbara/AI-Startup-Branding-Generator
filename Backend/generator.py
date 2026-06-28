import random

def generate_branding(description):

    desc = description.lower()

    prefixes = [
        "Smart", "Next", "Neo", "Ultra", "Quick",
        "Bright", "Blue", "Future", "Prime", "Cloud"
    ]

    suffixes = [
        "Tech", "Hub", "Flow", "Labs",
        "Connect", "Works", "Solutions", "AI"
    ]

    if "food" in desc:
        colors = "Red, Orange"
        logo = "Fork inside a location pin"
        audience = "Food lovers"
        marketing = "Instagram Reels, Swiggy Ads"

    elif "travel" in desc:
        colors = "Blue, Green"
        logo = "Airplane with globe"
        audience = "Travelers"
        marketing = "Travel Blogs, YouTube"

    elif "health" in desc or "medical" in desc:
        colors = "Blue, White"
        logo = "Medical cross with heart"
        audience = "Patients & Hospitals"
        marketing = "Healthcare Campaigns"

    elif "education" in desc or "college" in desc:
        colors = "Purple, White"
        logo = "Graduation cap"
        audience = "Students"
        marketing = "Campus Promotions"

    elif "ai" in desc:
        colors = "Black, Cyan"
        logo = "Brain with circuit"
        audience = "Businesses"
        marketing = "LinkedIn & Tech Blogs"

    else:
        colors = "Blue, White"
        logo = "Modern abstract icon"
        audience = "General Users"
        marketing = "Social Media Marketing"

    words = description.split()

    if len(words) > 0:
        name = random.choice(prefixes) + words[0].capitalize()
    else:
        name = random.choice(prefixes) + random.choice(suffixes)

    tagline = random.choice([
        "Innovating Your Future",
        "Smart Solutions Simplified",
        "Powered by Innovation",
        "Your Success Starts Here",
        "Technology That Inspires"
    ])

    return {
        "name": name,
        "tagline": tagline,
        "colors": colors,
        "logo": logo,
        "audience": audience,
        "marketing": marketing,
        "description": description
    }