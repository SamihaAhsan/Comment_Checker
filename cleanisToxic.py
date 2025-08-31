import pandas as pd


def dropem(keep, name):
    df = pd.read_csv('data.csv')

    df.drop("CommentId", axis=1, inplace=True)
    df.drop("VideoId", axis=1, inplace=True)

    if keep != "IsToxic":
        df.drop("IsToxic", axis=1, inplace=True)
    if keep != "IsAbusive":
        df.drop("IsAbusive", axis=1, inplace=True)
    if keep != "IsThreat":
        df.drop("IsThreat", axis=1, inplace=True)
    if keep != "IsProvocative":
        df.drop("IsProvocative", axis=1, inplace=True)
    if keep != "IsObscene":
        df.drop("IsObscene", axis=1, inplace=True)
    if keep != "IsHatespeech":
        df.drop("IsHatespeech", axis=1, inplace=True)
    if keep != "IsRacist":
        df.drop("IsRacist", axis=1, inplace=True)
    if keep != "IsNationalist":
        df.drop("IsNationalist", axis=1, inplace=True)
    if keep != "IsSexist":
        df.drop("IsSexist", axis=1, inplace=True)
    if keep != "IsHomophobic":
        df.drop("IsHomophobic", axis=1, inplace=True)
    if keep != "IsReligiousHate":
        df.drop("IsReligiousHate", axis=1, inplace=True)
    if keep != "IsRadicalism":
        df.drop("IsRadicalism", axis=1, inplace=True)
    df.to_csv(name, index=False)


dropem("IsToxic", "toxic.csv")
dropem("IsAbusive", "abusive.csv")
dropem("IsThreat", "threat.csv")
dropem("IsProvocative", "provocative.csv")
dropem("IsObscene", "obscene.csv")
dropem("IsHatespeech", "hate.csv")
dropem("IsRacist", "racist.csv")
dropem("IsNationalist", "national.csv")
dropem("IsSexist", "sexist.csv")
dropem("IsHomophobic", "homophob.csv")
dropem("IsReligiousHate", "religious.csv")
dropem("IsRadicalism", "racicalism.csv")


