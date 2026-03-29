import re

def extract_features(url, feature_names):
    features = []

    for feature in feature_names:
        f = feature.lower()

        if "ip" in f:
            features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)

        elif "length" in f:
            features.append(len(url))

        elif "@" in f:
            features.append(1 if "@" in url else 0)

        elif "https" in f or "ssl" in f:
            features.append(1 if url.startswith("https") else 0)

        elif "dash" in f or "prefix" in f:
            features.append(1 if "-" in url else 0)

        elif "dot" in f or "subdomain" in f:
            features.append(url.count("."))

        elif "short" in f:
            features.append(1 if "bit.ly" in url else 0)

        elif "redirect" in f:
            features.append(1 if "//" in url[7:] else 0)

        else:
            features.append(0)

    return features